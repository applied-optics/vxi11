from ctypes import *
import ctypes.util

DEFAULT_TIMEOUT = 10000
READ_TIMEOUT = 2000
NULL_READ_RESP = 50
NULL_WRITE_RESP = 51

class Vxi11(object):
    def __init__(self, address, device="inst0"):
        if address is None or address == "":
            raise ValueError("address must be defined")

        self._clink = None
        self._address = address
        self._device = device
        if(_vxi11_open_device(self._clink, address, device)):
            raise IOError("unable to open device at address "+address)

    def __del__(self):
        self.close()

    def close(self):
        _vxi11_close_device(self._clink, self._address)
        self._clink = None
        self._address = None
        self._device = None

    def send(self, cmd):
        rc = _vxi11_send(self._clink, cmd, len(cmd))
        if rc:
            raise IOError("error sending to the device: "+str(rc))

    def receive(self, max_length=1024, timeout=READ_TIMEOUT):
        buf = create_string_buffer(max_length)
        rc = _vxi11_receive_timeout(self._clink, buf, max_length, timeout)
        if rc < 0:
            raise IOError("error receiving from the device: "+str(rc))
        return buf.value

    def send_data_block(self, buf):
        if _vxi11_send_data_block(self._clink, buf, len(buf)):
            raise IOError("error sending to the device: "+str(rc))

    def receive_data_block(self, max_length=1024, timeout=READ_TIMEOUT):
        buf = create_string_buffer(max_length)
        rc = _vxi11_receive_data_block(self._clink, buf, max_length, timeout)
        if rc < 0:
            raise IOError("error receiving from the device: "+str(rc))
        return buf.value

    def send_and_receive(self, cmd, max_length=1024, timeout=READ_TIMEOUT):
        buf = create_string_buffer(max_length)
        rc = _vxi11_send_and_receive(self._clink, cmd, buf, max_length, timeout)
        if rc < 0:
            raise IOError("error sending/receiving from the device: "+str(rc))
        return buf.value

    def obtain_long_value(self, cmd):
        return _vxi11_obtain_long_value(self._clink, cmd)

    def obtain_double_value(self, cmd):
        return _vxi11_obtain_double_value(self._clink, cmd)


_libvxi11 = cdll.LoadLibrary(ctypes.util.find_library("vxi11"))

_vxi11_open_device = _libvxi11.vxi11_open_device
_vxi11_open_device.argtypes = [POINTER(c_void_p), c_char_p, c_char_p]
_vxi11_open_device.restype = c_int

_vxi11_close_device = _libvxi11.vxi11_close_device
_vxi11_close_device.argtypes = [c_void_p, c_char_p]
_vxi11_close_device.restype = c_int

_vxi11_send = _libvxi11.vxi11_send
_vxi11_send.argtypes = [c_void_p, c_char_p, c_size_t]
_vxi11_send.restype = c_int

_vxi11_receive = _libvxi11.vxi11_receive
_vxi11_receive.argtypes = [c_void_p, c_char_p, c_size_t, c_ulong]
_vxi11_receive.restype = c_ssize_t

_vxi11_send_data_block = _libvxi11.vxi11_send_data_block
_vxi11_send_data_block.argtypes = [c_void_p, c_char_p, c_size_t]
_vxi11_send_data_block.restype = c_int

_vxi11_receive_data_block = _libvxi11.vxi11_receive_data_block
_vxi11_receive_data_block.argtypes = [c_void_p, c_char_p, c_size_t, c_ulong]
_vxi11_receive_data_block.restype = c_ssize_t

_vxi11_send_and_receive = _libvxi11.vxi11_send_and_receive
_vxi11_send_and_receive.argtypes = [c_void_p, c_char_p, c_size_t, c_ulong]
_vxi11_send_and_receive.restype = c_int

_vxi11_obtain_long_value = _libvxi11.vxi11_obtain_long_value_timeout
_vxi11_obtain_long_value.argtypes = [c_void_p, c_char_p, c_ulong]
_vxi11_obtain_long_value.restype = c_long

_vxi11_obtain_double_value = _libvxi11.vxi11_obtain_double_value_timeout
_vxi11_obtain_double_value.argtypes = [c_void_p, c_char_p, c_ulong]
_vxi11_obtain_double_value.restype = c_double


