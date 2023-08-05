import difflib
import os
import io
import shutil
import struct
import sys
import tarfile
import tempfile
import warnings
import copyreg
from contextlib import closing, contextmanager

try:
    import _pickle as pickle
except:
    import pickle

import pathlib
import inspect
import tensorflow as tf
from trident.backend.tensorflow_ops import *
from trident.data.utils import unpickle, pickle_it
from trident.context import split_path, make_dir_if_need, sanitize_path

__all__ = ['save', 'load', 'load_pthtar']

string_classes = (str, bytes)


def _import_dotted_name(name):
    components = name.split('.')
    obj = __import__(components[0])
    for component in components[1:]:
        obj = getattr(obj, component)
    return obj


def get_source_lines_and_file(obj, error_msg=None):
    """
    Wrapper around inspect.getsourcelines and inspect.getsourcefile.
    Returns: (sourcelines, file_lino, filename)
    """
    filename = None  # in case getsourcefile throws
    try:
        filename = inspect.getsourcefile(obj)
        sourcelines, file_lineno = inspect.getsourcelines(obj)
    except OSError as e:
        msg = ("Can't get source for {}. TorchScript requires source access in "
               "order to carry out compilation, make sure original .py files are "
               "available. Original error: {}".format(obj, e))
        if error_msg:
            msg += '\n' + error_msg
        raise OSError(msg)

    return sourcelines, file_lineno, filename


def typename(o):
    # 'DoubleTensor', 'FloatTensor', 'LongTensor', 'IntTensor','ShortTensor', 'CharTensor', 'ByteTensor', 'BoolTensor'
    if is_tensor(o):
        if o.dtype == tf.float32:
            return 'FloatTensor'
        elif o.dtype == tf.int64:
            return 'LongTensor'
    module = ''
    class_name = ''
    if hasattr(o,
               '__module__') and o.__module__ != 'builtins' and o.__module__ != '__builtin__' and o.__module__ is not \
            None:
        module = o.__module__ + '.'

    if hasattr(o, '__qualname__'):
        class_name = o.__qualname__
    elif hasattr(o, '__name__'):
        class_name = o.__name__
    else:
        class_name = o.__class__.__name__

    return module + class_name


def is_storage(obj):
    r"""Returns True if `obj` is a PyTorch storage object.
    Args:
        obj (Object): Object to test
    """
    return type(obj) in ['DoubleStorage', 'FloatStorage', 'LongStorage', 'IntStorage',
                         'ShortStorage', 'CharStorage', 'ByteStorage', 'BoolStorage', ]


DEFAULT_PROTOCOL = 2

LONG_SIZE = struct.Struct('=l').size
INT_SIZE = struct.Struct('=i').size
SHORT_SIZE = struct.Struct('=h').size

MAGIC_NUMBER = 0x1950a86a20f9469cfc6c
PROTOCOL_VERSION = 1001
STORAGE_KEY_SEPARATOR = ','


class SourceChangeWarning(Warning):
    pass


@contextmanager
def mkdtemp():
    path = tempfile.mkdtemp()
    yield path
    shutil.rmtree(path)


_package_registry = []


def _is_zipfile(f):
    # This is a stricter implementation than zipfile.is_zipfile().
    # zipfile.is_zipfile() is True if the magic number appears anywhere in the
    # binary. Since we expect the files here to be generated by save or
    # jit.save, it's safe to only check the start bytes and avoid
    # collisions and assume the zip has only 1 file.
    # See bugs.python.org/issue28494.

    # Read the first 4 bytes of the file
    read_bytes = []
    start = f.tell()

    byte = f.read(1)
    while byte != "":
        read_bytes.append(byte)
        if len(read_bytes) == 4:
            break
        byte = f.read(1)
    f.seek(start)

    local_header_magic_number = [b'P', b'K', b'\x03', b'\x04']
    return read_bytes == local_header_magic_number


def register_package(priority, tagger, deserializer):
    queue_elem = (priority, tagger, deserializer)
    _package_registry.append(queue_elem)
    _package_registry.sort()


def check_module_version_greater_or_equal(module, req_version_tuple, error_if_malformed=True):
    """
    Check if a module's version satisfies requirements

    Usually, a module's version string will be like 'x.y.z', which would be represented
    as a tuple (x, y, z), but sometimes it could be an unexpected format. If the version
    string does not match the given tuple's format up to the length of the tuple, then
    error and exit or emit a warning.

    Args:
        module: the module to check the version of
        req_version_tuple: tuple (usually of ints) representing the required version
        error_if_malformed: whether we should exit if module version string is malformed

    Returns:
        requirement_is_met: bool
    """
    try:
        version_strs = module.__version__.split('.')
        # Cast module version fields to match the types of the required version
        module_version = tuple(
            type(req_field)(version_strs[idx]) for idx, req_field in enumerate(req_version_tuple)
        )
        requirement_is_met = module_version >= req_version_tuple

    except Exception as e:
        message = (
                      "'%s' module version string is malformed '%s' and cannot be compared"
                      " with tuple %s"
                  ) % (
                      module.__name__, module.__version__, str(req_version_tuple)
                  )
        if error_if_malformed:
            raise RuntimeError(message)
        else:
            warnings.warn(message + ', but continuing assuming that requirement is met')
            requirement_is_met = True

    return requirement_is_met


def _cpu_tag(obj):
    if type(obj).__module__ == 'tensorflow':
        return 'cpu'


def _cpu_deserialize(obj, location):
    if location == 'cpu':
        return obj


register_package(10, _cpu_tag, _cpu_deserialize)


def location_tag(storage):
    for _, tagger, _ in _package_registry:
        location = tagger(storage)
        if location:
            return location
    raise RuntimeError("don't know how to determine data location of "
                       + typename(storage))


def default_restore_location(storage, location):
    for _, _, fn in _package_registry:
        result = fn(storage, location)
        if result is not None:
            return result
    raise RuntimeError("don't know how to restore data location of "

                       + typename(storage) + " (tagged with "
                       + location + ")")


def normalize_storage_type(storage_type):
    return storage_type.__name__
    # return getattr(trident.backend, storage_type.__name__)


def storage_to_tensor_type(storage):
    storage_type = type(storage)
    module = _import_dotted_name(storage_type.__module__)
    return getattr(module, storage_type.__name__.replace('Storage', 'Tensor'))


def _is_path(name_or_buffer):
    return isinstance(name_or_buffer, str) or \
        (sys.version_info[0] == 3 and isinstance(name_or_buffer, pathlib.Path))


class _opener(object):
    def __init__(self, file_like):
        self.file_like = file_like

    def __enter__(self):
        return self.file_like

    def __exit__(self, *args):
        pass


class _open_file(_opener):
    def __init__(self, name, mode):
        super(_open_file, self).__init__(open(name, mode))

    def __exit__(self, *args):
        self.file_like.close()


class _open_buffer_reader(_opener):
    def __init__(self, buffer):
        super(_open_buffer_reader, self).__init__(buffer)
        _check_seekable(buffer)


class _open_buffer_writer(_opener):
    def __exit__(self, *args):
        self.file_like.close()


def _open_file_like(name_or_buffer, mode):
    if _is_path(name_or_buffer):
        return _open_file(name_or_buffer, mode)
    else:
        if 'w' in mode:
            return _open_buffer_writer(name_or_buffer)
        elif 'r' in mode:
            return _open_buffer_reader(name_or_buffer)
        else:
            raise RuntimeError("Expected 'r' or 'w' in mode but got {}".format(mode))


class _open_zipfile_reader(_opener):
    def __init__(self, name_or_buffer):
        super(_open_zipfile_reader, self).__init__(tarfile.open(name_or_buffer, 'r'))


class _open_zipfile_writer_file(_opener):
    def __init__(self, name):
        super(_open_zipfile_writer_file, self).__init__(tarfile.open(name, 'w'))

    def __exit__(self, *args):
        self.file_like.write_end_of_file()


class _open_zipfile_writer_buffer(_opener):
    def __init__(self, buffer):
        self.buffer = buffer
        super(_open_zipfile_writer_buffer, self).__init__(tarfile.open(buffer, 'w'))

    def __exit__(self, *args):
        self.file_like.write_end_of_file()
        self.buffer.flush()


def _open_zipfile_writer(name_or_buffer):
    if _is_path(name_or_buffer):
        container = _open_zipfile_writer_file
    else:
        container = _open_zipfile_writer_buffer
    return container(name_or_buffer)


def _is_compressed_file(f):
    compress_modules = ['gzip']
    try:
        return f.__module__ in compress_modules
    except AttributeError:
        return False


def _should_read_directly(f):
    """
    Checks if f is a file that should be read directly. It should be read
    directly if it is backed by a real file (has a fileno) and is not a
    a compressed file (e.g. gzip)
    """
    if _is_compressed_file(f):
        return False
    try:
        return f.fileno() >= 0
    except io.UnsupportedOperation:
        return False
    except AttributeError:
        return False


def _check_seekable(f):
    def raise_err_msg(patterns, e):
        for p in patterns:
            if p in str(e):
                msg = (str(e) + ". You can only load from a file that is seekable."
                       + " Please pre-load the data into a buffer like io.BytesIO and"
                       + " try to load from it instead.")
                raise type(e)(msg)
        raise e

    try:
        f.seek(f.tell())
        return True
    except (io.UnsupportedOperation, AttributeError) as e:
        raise_err_msg(["seek", "tell"], e)


def _check_dill_version(pickle_module):
    """Checks if using dill as the pickle module, and if so, checks if it is the correct version.
    If dill version is lower than 0.3.1, a ValueError is raised.

    Args:
        pickle_module: module used for pickling metadata and objects

    """
    if pickle_module.__name__ == 'dill':
        required_dill_version = (0, 3, 1)
        if not check_module_version_greater_or_equal(pickle_module, required_dill_version, False):
            raise ValueError((
                                 "'torch' supports dill >= %s, but you have dill %s."
                                 " Please upgrade dill or switch to 'pickle'"
                             ) % (
                                 '.'.join([str(num) for num in required_dill_version]),
                                 pickle_module.__version__
                             ))


def save(obj, f, pickle_module=pickle, pickle_protocol=DEFAULT_PROTOCOL, is_compressed=False):
    """Saves an object to a disk file.

    See also: :ref:`recommend-saving-models`

    Args:
        obj: saved object
        f: a file-like object (has to implement write and flush) or a string
           containing a file name
        pickle_module: module used for pickling metadata and objects
        pickle_protocol: can be specified to override the default protocol
        is_compressed:whether reuse zipfile_serialization

    .. warning::
        If you are using Python 2, :func:`save` does NOT support :class:`StringIO.StringIO`
        as a valid file-like object. This is because the write method should return
        the number of bytes written; :meth:`StringIO.write()` does not do this.

        Please use something like :class:`io.BytesIO` instead.

    Examples:
        >>> # Save to file
        >>> x = to_tensor([0, 1, 2, 3, 4])
        >>> save(x, 'tensor.pt')
        >>> # Save to io.BytesIO buffer
        >>> buffer = io.BytesIO()
        >>> save(x, buffer)
    """
    _use_new_zipfile_serialization = False
    _check_dill_version(pickle_module)

    with _open_file_like(f, 'wb') as opened_file:
        _legacy_save(obj, opened_file, pickle_module, pickle_protocol)

    if is_compressed:
        f_pickle = ''
        if isinstance(f, str):
            f_pickle = f
        elif hasattr(f, 'flush') and hasattr(f, 'write'):
            f_pickle = f.name

        fp = tarfile.open(f_pickle + '_', 'w')
        fp.add(f_pickle)
        fp.close()
        os.remove(f_pickle)
        os.rename(f_pickle + '_', f_pickle)


def _legacy_save(obj, f, pickle_module, pickle_protocol):
    if sys.version_info[0] == 2:
        import StringIO
        if isinstance(f, StringIO.StringIO):
            msg = ('save received unsupported StringIO.StringIO file object, whose '
                   'write method does not return the number of bytes written. '
                   'Please use something like io.BytesIO for save instead.')
            raise RuntimeError(msg)

    serialized_container_types = {}
    serialized_storages = {}

    def persistent_id(obj):
        # FIXME: the docs say that persistent_id should only return a string
        # but torch store returns tuples. This works only in the binary protocol
        # see
        # https://docs.python.org/2/library/pickle.html#pickling-and-unpickling-external-objects
        # https://github.com/python/cpython/blob/master/Lib/pickle.py#L527-L537
        if isinstance(obj, type) and issubclass(obj, tf.Module):
            if obj in serialized_container_types:
                return None
            serialized_container_types[obj] = True
            source_file = source = None
            try:
                source_lines, _, source_file = get_source_lines_and_file(obj)
                source = ''.join(source_lines)
            except Exception:  # saving the source is optional, so we can ignore any errors
                warnings.warn("Couldn't retrieve source code for container of "
                              "type " + obj.__name__ + ". It won't be checked "
                                                       "for correctness upon loading.")
            return 'module', obj, source_file, source

        elif is_tensor(obj):
            storage_type = type(obj).__name__
            # Offset is always 0, but we keep it for backwards compatibility
            # with the old serialization format (which supported storage views)
            offset = 0
            if hasattr(obj, '_unique_id'):
                obj_key = obj._unique_id
            elif hasattr(obj, '_id'):
                obj_key = str(obj._id)
            else:
                obj_key = ''
            location = 'cpu'
            serialized_storages[obj_key] = obj
            return ('storage',
                    storage_type,
                    obj_key,
                    location,
                    obj.shape.as_list(),
                    None)
        return None

    sys_info = dict(
        protocol_version=PROTOCOL_VERSION,
        little_endian=sys.byteorder == 'little',
        type_sizes=dict(
            short=SHORT_SIZE,
            int=INT_SIZE,
            long=LONG_SIZE,
        ),
    )

    pickle_module.dump(MAGIC_NUMBER, f, protocol=pickle_protocol)
    pickle_module.dump(PROTOCOL_VERSION, f, protocol=pickle_protocol)
    pickle_module.dump(sys_info, f, protocol=pickle_protocol)
    pickler = pickle_module.Pickler(f, protocol=pickle_protocol)
    # pickler.persistent_id = persistent_id
    pickler.dump(obj)

    # serialized_storage_keys = sorted(serialized_storages.keys())
    # pickle_module.dump(serialized_storage_keys, f, protocol=pickle_protocol)
    f.flush()
    # for key in serialized_storage_keys:
    #     serialized_storages[key]._write_file(f, _should_read_directly(f), True)


def _save(obj, zip_file, pickle_module, pickle_protocol):
    serialized_storages = {}

    def persistent_id(obj):
        # FIXME: the docs say that persistent_id should only return a string
        # but torch store returns tuples. This works only in the binary protocol
        # see
        # https://docs.python.org/2/library/pickle.html#pickling-and-unpickling-external-objects
        # https://github.com/python/cpython/blob/master/Lib/pickle.py#L527-L537

        if is_storage(obj):
            storage_type = normalize_storage_type(type(obj))
            obj_key = str(obj._cdata)
            location = location_tag(obj)
            serialized_storages[obj_key] = obj

            return ('storage',
                    storage_type,
                    obj_key,
                    location,
                    obj.size())
        return None

    # Write the pickle data for `obj`
    data_buf = io.BytesIO()
    pickler = pickle_module.Pickler(data_buf, protocol=pickle_protocol)
    pickler.persistent_id = persistent_id
    pickler.dump(obj)
    data_value = data_buf.getvalue()
    zip_file.write_record('data.pkl', data_value, len(data_value))

    # Write each tensor to a file named tensor/the_tensor_key in the zip archive
    for key in sorted(serialized_storages.keys()):
        name = 'data/{}'.format(key)
        storage = serialized_storages[key]
        if storage.device.type == 'cpu':
            # If it's on the CPU we can directly copy it into the zip file
            num_bytes = storage.size() * storage.element_size()
            buf = io.BytesIO()
            zip_file.write_record(name, storage.data_ptr(), num_bytes)
        else:
            # Copy to a buffer, then serialize that
            buf = io.BytesIO()
            storage._write_file(buf, _should_read_directly(buf))
            buf_value = buf.getvalue()
            zip_file.write_record(name, buf_value, len(buf_value))


def load_pthtar(f, pickle_module=pickle, **pickle_load_args):
    _check_dill_version(pickle_module)

    if sys.version_info >= (3, 0) and 'encoding' not in pickle_load_args.keys():
        pickle_load_args['encoding'] = 'utf-8'

    with _open_file_like(f, 'rb') as opened_file:
        deserialize_obj = None
        if '.tar' in opened_file.name:
            with closing(tarfile.open(fileobj=opened_file, mode='r:',
                                      format=tarfile.PAX_FORMAT)) as tar, mkdtemp() as tmpdir:
                members = tar.getmembers()
                tar.extract(members[0], path=tmpdir)
                deserialize_obj = load(os.path.join(tmpdir, members[0].name), 'rb')
                return deserialize_obj

        deserialize_obj = _legacy_load(opened_file, map_location=None, pickle_module=pickle_module, **pickle_load_args)
        return deserialize_obj


def load(f, map_location=None, pickle_module=pickle, **pickle_load_args):
    """Loads an object saved with :func:`save` from a file.

    :func:`load` uses Python's unpickling facilities but treats storages,
    which underlie tensors, specially. They are first deserialized on the
    CPU and are then moved to the device they were saved from. If this fails
    (e.g. because the run time system doesn't have certain devices), an exception
    is raised. However, storages can be dynamically remapped to an alternative
    set of devices using the :attr:`map_location` argument.

    If :attr:`map_location` is a callable, it will be called once for each serialized
    storage with two arguments: storage and location. The storage argument
    will be the initial deserialization of the storage, residing on the CPU.
    Each serialized storage has a location tag associated with it which
    identifies the device it was saved from, and this tag is the second
    argument passed to :attr:`map_location`. The builtin location tags are ``'cpu'``
    for CPU tensors and ``'cuda:device_id'`` (e.g. ``'cuda:2'``) for CUDA tensors.
    :attr:`map_location` should return either ``None`` or a storage. If
    :attr:`map_location` returns a storage, it will be used as the final deserialized
    object, already moved to the right device. Otherwise, :func:`load` will
    fall back to the default behavior, as if :attr:`map_location` wasn't specified.

    If :attr:`map_location` is a :class:`device` object or a string containing
    a device tag, it indicates the location where all tensors should be loaded.

    Otherwise, if :attr:`map_location` is a dict, it will be used to remap location tags
    appearing in the file (keys), to ones that specify where to put the
    storages (values).

    User extensions can register their own location tags and tagging and
    deserialization methods using :func:`serialization.register_package`.

    Args:
        f: a file-like object (has to implement :meth:`read`, :meth`readline`, :meth`tell`, and :meth`seek`),
            or a string containing a file name
        map_location: a function, :class:`device`, string or a dict specifying how to remap storage
            locations
        pickle_module: module used for unpickling metadata and objects (has to
            match the :attr:`pickle_module` used to serialize file)
        pickle_load_args: (Python 3 only) optional keyword arguments passed over to
            :func:`pickle_module.load` and :func:`pickle_module.Unpickler`, e.g.,
            :attr:`errors=...`.

    .. warning::
        :func:`load()` uses ``pickle`` module implicitly, which is known to be insecure.
        It is possible to construct malicious pickle data which will execute arbitrary code
        during unpickling. Never load data that could have come from an untrusted
        source, or that could have been tampered with. **Only load data you trust**.

    .. note::
        When you call :func:`load()` on a file which contains GPU tensors, those tensors
        will be loaded to GPU by default. You can call ``load(.., map_location='cpu')``
        and then :meth:`load_state_dict` to avoid GPU RAM surge when loading a model checkpoint.

    .. note::
        By default, we decode byte strings as ``utf-8``.  This is to avoid a common error
        case ``UnicodeDecodeError: 'ascii' codec can't decode byte 0x...``
        when loading files saved by Python 2 in Python 3.  If this default
        is incorrect, you may use an extra :attr:`encoding` keyword argument to specify how
        these objects should be loaded, e.g., :attr:`encoding='latin1'` decodes them
        to strings using ``latin1`` encoding, and :attr:`encoding='bytes'` keeps them
        as byte arrays which can be decoded later with ``byte_array.decode(...)``.

    Examples:
        >>> load('tensors.pt')
        # Load all tensors onto the CPU
        >>> load('tensors.pt', map_location=device('cpu'))
        # Load all tensors onto the CPU, using a function
        >>> load('tensors.pt', map_location=lambda storage, loc: storage)
        # Load all tensors onto GPU 1
        >>> load('tensors.pt', map_location=lambda storage, loc: storage.cuda())
        # Map tensors from GPU 1 to GPU 0
        >>> load('tensors.pt', map_location={'cuda:1':'cuda:0'})
        # Load tensor from io.BytesIO object
        >>> with open('tensor.pt', 'rb') as f:
                buffer = io.BytesIO(f.read())
        >>> load(buffer)
        # Load a module with 'ascii' encoding for unpickling
        >>> load('module.pt', encoding='ascii')
    """
    _check_dill_version(pickle_module)

    if sys.version_info >= (3, 0) and 'encoding' not in pickle_load_args.keys():
        pickle_load_args['encoding'] = 'utf-8'

    with _open_file_like(f, 'rb') as opened_file:
        if _is_zipfile(opened_file):
            with _open_zipfile_reader(f) as opened_zipfile:
                # if _is_torchscript_zip(opened_zipfile):
                #     warnings.warn("'load' received a zip file that looks like a TorchScript archive"
                #                   " dispatching to 'jit.load' (call 'jit.load' directly to"
                #                   " silence this warning)", UserWarning)
                #     return jit.load(f)
                return _load(opened_zipfile, map_location, pickle_module, **pickle_load_args)
        result = _legacy_load(opened_file, map_location, pickle_module, **pickle_load_args)
        # inp=result.input_shape
        # for module in result.modules():
        #     module._input_shape=None
        #     module._output_shape = None
        # result.input_shape=inp
        return result


# Register pickling support for layout instances such as
# sparse_coo, etc
def _get_layout(name):
    """Get layout extension object from its string representation.
    """
    cache = _get_layout.cache
    if not cache:
        import gc
        gcitems = gc.get_objects()
        for i in range(len(gcitems)):
            obj = gcitems[i]
            if 'layout' in obj.__class__.__name__:
                cache[str(obj)] = obj
    return cache[name]


_get_layout.cache = {}


# copyreg.pickle(layout, lambda obj: (_get_layout, (str(obj),)))


def _legacy_load(f, map_location, pickle_module, **pickle_load_args):
    deserialized_objects = {}

    restore_location = _get_restore_location(map_location)

    def _check_container_source(container_type, source_file, original_source):
        try:
            current_source = ''.join(get_source_lines_and_file(container_type)[0])
        except Exception:  # saving the source is optional, so we can ignore any errors
            warnings.warn("Couldn't retrieve source code for container of "
                          "type " + container_type.__name__ + ". It won't be checked "
                                                              "for correctness upon loading.")
            return
        if original_source != current_source:
            if container_type.dump_patches:
                file_name = container_type.__name__ + '.patch'
                diff = difflib.unified_diff(current_source.split('\n'),
                                            original_source.split('\n'),
                                            source_file,
                                            source_file, lineterm="")
                lines = '\n'.join(diff)
                try:
                    with open(file_name, 'a+') as f:
                        file_size = f.seek(0, 2)
                        f.seek(0)
                        if file_size == 0:
                            f.write(lines)
                        elif file_size != len(lines) or f.read() != lines:
                            raise IOError
                    msg = ("Saved a reverse patch to " + file_name + ". "
                                                                     "Run `patch -p0 < " + file_name + "` to revert your "
                                                                                                       "changes.")
                except IOError:
                    msg = ("Tried to save a patch, but couldn't create a "
                           "writable file " + file_name + ". Make sure it "
                                                          "doesn't exist and your working directory is "
                                                          "writable.")
            else:
                msg = ("you can retrieve the original source code by "
                       "accessing the object's source attribute or set "
                       "`nn.Module.dump_patches = True` and use the "
                       "patch tool to revert the changes.")
            msg = ("source code of class '{container_type}' has changed. {msg}"
                   .format(container_type=typename(container_type), msg=msg))
            warnings.warn(msg, SourceChangeWarning)

    def legacy_load(f):
        deserialized_objects = {}

        def persistent_load(saved_id):
            if isinstance(saved_id, tuple):
                # Ignore containers that don't have any sources saved
                if all(saved_id[1:]):
                    _check_container_source(*saved_id)
                return saved_id[0]
            return deserialized_objects[int(saved_id)]

        with closing(tarfile.open(fileobj=f, mode='r:', format=tarfile.PAX_FORMAT)) as tar, \
                mkdtemp() as tmpdir:
            members = tar.getmembers()
            tar.extract(members[0], path=tmpdir)

            with open(os.path.join(tmpdir, members[0].name), 'rb', 0) as f:
                num_storages = pickle_module.load(f, **pickle_load_args)
                for i in range(num_storages):
                    args = pickle_module.load(f, **pickle_load_args)
                    key, location, storage_type = args
                    obj = storage_type._new_with_file(f)
                    obj = restore_location(obj, location)
                    deserialized_objects[key] = obj

                storage_views = pickle_module.load(f, **pickle_load_args)
                for target_cdata, root_cdata, offset, size in storage_views:
                    root = deserialized_objects[root_cdata]
                    deserialized_objects[target_cdata] = root[offset:offset + size]

            tar.extract('tensors', path=tmpdir)
            with open(os.path.join(tmpdir, 'tensors'), 'rb', 0) as f:
                num_tensors = pickle_module.load(f, **pickle_load_args)
                for _ in range(num_tensors):
                    args = pickle_module.load(f, **pickle_load_args)
                    key, storage_id, original_tensor_type = args
                    storage = deserialized_objects[storage_id]
                    tensor_type = storage_to_tensor_type(storage)
                    ndim, = struct.unpack('<i', f.read(4))
                    # skip next 4 bytes; legacy encoding treated ndim as 8 bytes
                    f.read(4)
                    size = struct.unpack('<{}q'.format(ndim), f.read(8 * ndim))
                    stride = struct.unpack('<{}q'.format(ndim), f.read(8 * ndim))
                    storage_offset, = struct.unpack('<q', f.read(8))
                    tensor = tensor_type().set_(storage, storage_offset, size, stride)
                    deserialized_objects[key] = tensor

            pickle_file = tar.extractfile('pickle')
            unpickler = pickle_module.Unpickler(pickle_file, **pickle_load_args)
            unpickler.persistent_load = persistent_load
            result = unpickler.load()
            return result

    deserialized_objects = {}

    def persistent_load(saved_id):
        assert isinstance(saved_id, tuple)
        typename = _maybe_decode_ascii(saved_id[0])
        data = saved_id[1:]

        if typename == 'module':
            # Ignore containers that don't have any sources saved
            if all(data[1:]):
                _check_container_source(*data)
            return data[0]
        elif typename == 'storage':
            data_type, root_key, location, size, view_metadata = data
            location = _maybe_decode_ascii(location)
            if root_key not in deserialized_objects:
                obj = data_type(size)
                # obj._torch_load_uninitialized = True
                deserialized_objects[root_key] = restore_location(obj, location)
            storage = deserialized_objects[root_key]
            if view_metadata is not None:
                view_key, offset, view_size = view_metadata
                if view_key not in deserialized_objects:
                    deserialized_objects[view_key] = storage[offset:offset + view_size]
                return deserialized_objects[view_key]
            else:
                return storage
        else:
            raise RuntimeError("Unknown saved id type: %s" % saved_id[0])

    _check_seekable(f)
    f_should_read_directly = _should_read_directly(f)

    if f_should_read_directly and f.tell() == 0:
        # legacy_load requires that f has fileno()
        # only if offset is zero we can attempt the legacy tar file loader
        try:
            return legacy_load(f)
        except tarfile.TarError:
            if _is_zipfile(f):
                # .zip is used for jit.save and will throw an un-pickling error here
                raise RuntimeError(
                    "{filename} is a zip archive (did you mean to use jit.load()?)".format(filename=f.name))
            # if not a tarfile, reset file offset and proceed
            f.seek(0)

    if not hasattr(f, 'readinto') and (3, 8, 0) <= sys.version_info < (3, 8, 2):
        raise RuntimeError(
            "load does not work with file-like objects that do not implement readinto on Python 3.8.0 and 3.8.1. "
            "Received object of type \"{}\". Please update to Python 3.8.2 or newer to restore this "
            "functionality.".format(type(f)))

    magic_number = pickle_module.load(f, **pickle_load_args)
    if magic_number != MAGIC_NUMBER:
        raise RuntimeError("Invalid magic number; corrupt file?")
    protocol_version = pickle_module.load(f, **pickle_load_args)
    if protocol_version != PROTOCOL_VERSION:
        raise RuntimeError("Invalid protocol version: %s" % protocol_version)

    _sys_info = pickle_module.load(f, **pickle_load_args)
    unpickler = pickle_module.Unpickler(f, **pickle_load_args)
    unpickler.persistent_load = persistent_load
    result = unpickler.load()

    # deserialized_storage_keys = pickle_module.load(f, **pickle_load_args)

    # offset = f.tell() if f_should_read_directly else None
    # for key in deserialized_storage_keys:
    #     assert key in deserialized_objects
    #     deserialized_objects[key]._set_from_file(f, offset, f_should_read_directly)
    #     if offset is not None:
    #         offset = f.tell()

    return result


def _maybe_decode_ascii(bytes_str):
    # When using encoding='bytes' in Py3, some **internal** keys stored as
    # strings in Py2 are loaded as bytes. This function decodes them with
    # ascii encoding, one that Py3 uses by default.
    #
    # NOTE: This should only be used on internal keys (e.g., `typename` and
    #       `location` in `persistent_load` below!
    if isinstance(bytes_str, bytes):
        return bytes_str.decode('ascii')
    return bytes_str


def _get_restore_location(map_location):
    if map_location is None:
        restore_location = default_restore_location
    elif isinstance(map_location, dict):
        def restore_location(storage, location):
            location = map_location.get(location, location)
            return default_restore_location(storage, location)
    elif isinstance(map_location, str):
        def restore_location(storage, location):
            return default_restore_location(storage, map_location)
    elif 'device' in map_location.__class__.__name__:
        def restore_location(storage, location):
            return default_restore_location(storage, str(map_location))
    else:
        def restore_location(storage, location):
            result = map_location(storage, location)
            if result is None:
                result = default_restore_location(storage, location)
            return result
    return restore_location


def _load(zip_file, map_location, pickle_module, **pickle_load_args):
    restore_location = _get_restore_location(map_location)

    loaded_storages = {}

    def load_tensor(obj, size, key, location):
        loaded_storages[key] = restore_location(obj, location)
        name = 'data/{}'.format(key)
        size_long = struct.pack("<Q", size)
        tensor_file = io.BytesIO(size_long + zip_file.get_record(name))
        offset = None
        is_real_file = False
        loaded_storages[key]._set_from_file(tensor_file, offset, is_real_file)

    def persistent_load(saved_id):
        assert isinstance(saved_id, tuple)
        typename = _maybe_decode_ascii(saved_id[0])
        data = saved_id[1:]

        assert typename == 'storage', \
            "Unknown typename for persistent_load, expected 'storage' but got '{}'".format(typename)
        data_type, key, location, size = data
        if key not in loaded_storages:
            load_tensor(data_type(size), size, key, _maybe_decode_ascii(location))
        storage = loaded_storages[key]
        return storage

    # Load the data (which may in turn use `persistent_load` to load tensors)
    data_file = io.BytesIO(zip_file.get_record('data.pkl'))
    unpickler = pickle_module.Unpickler(data_file, **pickle_load_args)
    unpickler.persistent_load = persistent_load
    result = unpickler.load()

    return result
