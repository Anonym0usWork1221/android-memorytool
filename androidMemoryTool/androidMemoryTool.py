"""
 *  @date   : 2022/03/23
 *  Version : 0.1
 *  @author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# ! /usr/bin/env python
from .libsDirectWriter import *
from .libsDirectRead import *
from .DataClasses import *
from .ThreadingController import *
from .search_and_readers import *
from .search_and_writers import *


class AndroidMemoryTool:
    def __init__(self):
        pass

    @staticmethod
    def read_value(read):
        speed_mode = get_variables(is_speed=True)
        data_types = get_variables(is_data_byte=True)
        proc_id = get_variables(is_pid=True)

        if data_types != -1:
            maps_addr = get_variables(is_map_addr=True)
            value_to_read = DataTypeEncoding(read)

            if data_types == 0:

                if speed_mode:
                    fast_search_algorithms_text(proc_id, maps_addr, value_to_read)
                    return get_readers_values()

                else:
                    search_and_read_text(proc_id, maps_addr, value_to_read)
                    return get_readers_values()

            else:
                if speed_mode:
                    fast_search_algorithms_value(proc_id, maps_addr, value_to_read,
                                                 data_types)
                    return get_readers_values()

                else:
                    return search_and_read(proc_id, maps_addr, data_types, value_to_read)

        return None

    @staticmethod
    def read_write_value(read, write):
        speed_mode = get_variables(is_speed=True)
        data_types = get_variables(is_data_byte=True)
        proc_id = get_variables(is_pid=True)

        if data_types != -1:
            maps_addr = get_variables(is_map_addr=True)
            value_to_read, value_to_write = DataTypeEncoding(read, write)

            if data_types == 0:

                if speed_mode:
                    fast_search_algorithms_text(proc_id, maps_addr, value_to_read, value_to_write)
                    return get_writer_values()

                else:
                    return search_and_write_text(proc_id, maps_addr, value_to_read, value_to_write)

            else:
                if speed_mode:
                    fast_search_algorithms_value(proc_id, maps_addr, value_to_read,
                                                 data_types,
                                                 value_to_write)
                    return get_writer_values()

                else:
                    return search_and_write(proc_id, maps_addr, data_types, value_to_read,
                                            value_to_write)

        return None

    # Float Writers
    @staticmethod
    def write_float_xa(PID: str, read: float, write: float) -> int:
        details_xa = mappingXA(PID)
        return search_and_write_float_XA(PID, details_xa, read, write)

    @staticmethod
    def write_float_ca(PID: str, read: float, write: float) -> int:
        details_ca = mappingCA(PID)
        return search_and_write_float_CA(PID, details_ca, read, write)

    @staticmethod
    def write_float_a(PID: str, read: float, write: float) -> int:
        details_a = mappingA(PID)
        return search_and_write_float_A(PID, details_a, read, write)

    @staticmethod
    def write_float_all(PID: str, read: float, write: float) -> int:
        details_all = mappingALL(PID)
        return search_and_write_float_ALL(PID, details_all, read, write)

    # Double Writers
    @staticmethod
    def write_double_xa(PID: str, read: float, write: float) -> int:
        details_xa = mappingXA(PID)
        return search_and_write_double_XA(PID, details_xa, read, write)

    @staticmethod
    def write_double_ca(PID: str, read: float, write: float) -> int:
        details_ca = mappingCA(PID)
        return search_and_write_double_CA(PID, details_ca, read, write)

    @staticmethod
    def write_double_a(PID: str, read: float, write: float) -> int:
        details_a = mappingA(PID)
        return search_and_write_double_A(PID, details_a, read, write)

    @staticmethod
    def write_double_all(PID: str, read: float, write: float) -> int:
        details_all = mappingALL(PID)
        return search_and_write_double_ALL(PID, details_all, read, write)

    # Dword Writers
    @staticmethod
    def write_dword_xa(PID: str, read: int, write: int) -> int:
        details_xa = mappingXA(PID)
        return search_and_write_dword_XA(PID, details_xa, read, write)

    @staticmethod
    def write_dword_ca(PID: str, read: int, write: int) -> int:
        details_ca = mappingCA(PID)
        return search_and_write_dword_CA(PID, details_ca, read, write)

    @staticmethod
    def write_dword_a(PID: str, read: int, write: int) -> int:
        details_a = mappingA(PID)
        return search_and_write_dword_A(PID, details_a, read, write)

    @staticmethod
    def write_dword_all(PID: str, read: int, write: int) -> int:
        details_all = mappingALL(PID)
        return search_and_write_dword_ALL(PID, details_all, read, write)

    # UTF-8 Writers
    @staticmethod
    def write_utf8_xa(PID: str, read: str, write: str) -> int:
        details_xa = mappingXA(PID)
        return search_and_write_utf8_XA(PID, details_xa, read, write)

    @staticmethod
    def write_utf8_ca(PID: str, read: str, write: str) -> int:
        details_ca = mappingCA(PID)
        return search_and_write_utf8_CA(PID, details_ca, read, write)

    @staticmethod
    def write_utf8_a(PID: str, read: str, write: str) -> int:
        details_a = mappingA(PID)
        return search_and_write_utf8_A(PID, details_a, read, write)

    @staticmethod
    def write_utf8_all(PID: str, read: str, write: str) -> int:
        details_all = mappingALL(PID)
        return search_and_write_utf8_ALL(PID, details_all, read, write)

    # UTF-16LE Writers
    @staticmethod
    def write_utf16le_xa(PID: str, read: str, write: str) -> int:
        details_xa = mappingXA(PID)
        return search_and_write_utf16LE_XA(PID, details_xa, read, write)

    @staticmethod
    def write_utf16le_ca(PID: str, read: str, write: str) -> int:
        details_ca = mappingCA(PID)
        return search_and_write_utf16LE_CA(PID, details_ca, read, write)

    @staticmethod
    def write_utf16le_a(PID: str, read: str, write: str) -> int:
        details_a = mappingA(PID)
        return search_and_write_utf16LE_A(PID, details_a, read, write)

    @staticmethod
    def write_utf16le_all(PID: str, read: str, write: str) -> int:
        details_all = mappingALL(PID)
        return search_and_write_utf16LE_ALL(PID, details_all, read, write)

    # Qword Writers
    @staticmethod
    def write_qword_xa(PID: str, read: int, write: int) -> int:
        details_xa = mappingXA(PID)
        return search_and_write_qword_XA(PID, details_xa, read, write)

    @staticmethod
    def write_qword_ca(PID: str, read: int, write: int) -> int:
        details_ca = mappingCA(PID)
        return search_and_write_qword_CA(PID, details_ca, read, write)

    @staticmethod
    def write_qword_a(PID: str, read: int, write: int) -> int:
        details_a = mappingA(PID)
        return search_and_write_qword_A(PID, details_a, read, write)

    @staticmethod
    def write_qword_all(PID: str, read: int, write: int) -> int:
        details_all = mappingALL(PID)
        return search_and_write_qword_ALL(PID, details_all, read, write)

    # Word Writers
    @staticmethod
    def write_word_xa(PID: str, read: int, write: int) -> int:
        details_xa = mappingXA(PID)
        return search_and_write_word_XA(PID, details_xa, read, write)

    @staticmethod
    def write_word_ca(PID: str, read: int, write: int) -> int:
        details_ca = mappingCA(PID)
        return search_and_write_word_CA(PID, details_ca, read, write)

    @staticmethod
    def write_word_a(PID: str, read: int, write: int) -> int:
        details_a = mappingA(PID)
        return search_and_write_word_A(PID, details_a, read, write)

    @staticmethod
    def write_word_all(PID: str, read: int, write: int) -> int:
        details_all = mappingALL(PID)
        return search_and_write_word_ALL(PID, details_all, read, write)

    # Byte Writers
    @staticmethod
    def write_byte_xa(PID: str, read: int, write: int) -> int:
        details_xa = mappingXA(PID)
        return search_and_write_byte_XA(PID, details_xa, read, write)

    @staticmethod
    def write_byte_ca(PID: str, read: int, write: int) -> int:
        details_ca = mappingCA(PID)
        return search_and_write_byte_CA(PID, details_ca, read, write)

    @staticmethod
    def write_byte_a(PID: str, read: int, write: int) -> int:
        details_a = mappingA(PID)
        return search_and_write_byte_A(PID, details_a, read, write)

    @staticmethod
    def write_byte_all(PID: str, read: int, write: int) -> int:
        details_all = mappingALL(PID)
        return search_and_write_byte_ALL(PID, details_all, read, write)

    # Xor Writers
    @staticmethod
    def write_xor_xa(PID: str, read: int, write: int) -> int:
        details_xa = mappingXA(PID)
        return search_and_write_xor_XA(PID, details_xa, read, write)

    @staticmethod
    def write_xor_ca(PID: str, read: int, write: int) -> int:
        details_ca = mappingCA(PID)
        return search_and_write_xor_CA(PID, details_ca, read, write)

    @staticmethod
    def write_xor_a(PID: str, read: int, write: int) -> int:
        details_a = mappingA(PID)
        return search_and_write_xor_A(PID, details_a, read, write)

    @staticmethod
    def write_xor_all(PID: str, read: int, write: int) -> int:
        details_all = mappingALL(PID)
        return search_and_write_xor_ALL(PID, details_all, read, write)

    """ ################################################################################################## """
    """                                 Readers Block                          """

    # Float Readers
    @staticmethod
    def read_float_xa(PID: str, read: float) -> tuple[list, int]:
        details_xa = mappingXA(PID)
        return search_and_read_float_XA(PID, details_xa, read)

    @staticmethod
    def read_float_ca(PID: str, read: float) -> tuple[list, int]:
        details_ca = mappingCA(PID)
        return search_and_read_float_CA(PID, details_ca, read)

    @staticmethod
    def read_float_a(PID: str, read: float) -> tuple[list, int]:
        details_a = mappingA(PID)
        return search_and_read_float_A(PID, details_a, read)

    @staticmethod
    def read_float_all(PID: str, read: float) -> tuple[list, int]:
        details_all = mappingALL(PID)
        return search_and_read_float_ALL(PID, details_all, read)

    # Double Readers
    @staticmethod
    def read_double_xa(PID: str, read: float) -> tuple[list, int]:
        details_xa = mappingXA(PID)
        return search_and_read_double_XA(PID, details_xa, read)

    @staticmethod
    def read_double_ca(PID: str, read: float) -> tuple[list, int]:
        details_ca = mappingCA(PID)
        return search_and_read_double_CA(PID, details_ca, read)

    @staticmethod
    def read_double_a(PID: str, read: float) -> tuple[list, int]:
        details_a = mappingA(PID)
        return search_and_read_double_A(PID, details_a, read)

    @staticmethod
    def read_double_all(PID: str, read: float) -> tuple[list, int]:
        details_all = mappingALL(PID)
        return search_and_read_double_ALL(PID, details_all, read)

    # Dword Readers
    @staticmethod
    def read_dword_xa(PID: str, read: int) -> tuple[list, int]:
        details_xa = mappingXA(PID)
        return search_and_read_dword_XA(PID, details_xa, read)

    @staticmethod
    def read_dword_ca(PID: str, read: int) -> tuple[list, int]:
        details_ca = mappingCA(PID)
        return search_and_read_dword_CA(PID, details_ca, read)

    @staticmethod
    def read_dword_a(PID: str, read: int) -> tuple[list, int]:
        details_a = mappingA(PID)
        return search_and_read_dword_A(PID, details_a, read)

    @staticmethod
    def read_dword_all(PID: str, read: int) -> tuple[list, int]:
        details_all = mappingALL(PID)
        return search_and_read_dword_ALL(PID, details_all, read)

    # UTF-8 Readers
    @staticmethod
    def read_utf8_xa(PID: str, read: str) -> tuple[list, int]:
        details_xa = mappingXA(PID)
        return search_and_read_utf8_XA(PID, details_xa, read)

    @staticmethod
    def read_utf8_ca(PID: str, read: str) -> tuple[list, int]:
        details_ca = mappingCA(PID)
        return search_and_read_utf8_CA(PID, details_ca, read)

    @staticmethod
    def read_utf8_a(PID: str, read: str) -> tuple[list, int]:
        details_a = mappingA(PID)
        return search_and_read_utf8_A(PID, details_a, read)

    @staticmethod
    def read_utf8_all(PID: str, read: str) -> tuple[list, int]:
        details_all = mappingALL(PID)
        return search_and_read_utf8_ALL(PID, details_all, read)

    # UTF-16LE Readers
    @staticmethod
    def read_utf16le_xa(PID: str, read: str) -> tuple[list, int]:
        details_xa = mappingXA(PID)
        return search_and_read_utf16LE_XA(PID, details_xa, read)

    @staticmethod
    def read_utf16le_ca(PID: str, read: str) -> tuple[list, int]:
        details_ca = mappingCA(PID)
        return search_and_read_utf16LE_CA(PID, details_ca, read)

    @staticmethod
    def read_utf16le_a(PID: str, read: str) -> tuple[list, int]:
        details_a = mappingA(PID)
        return search_and_read_utf16LE_A(PID, details_a, read)

    @staticmethod
    def read_utf16le_all(PID: str, read: str) -> tuple[list, int]:
        details_all = mappingALL(PID)
        return search_and_read_utf16LE_ALL(PID, details_all, read)

    # Qword Readers
    @staticmethod
    def read_qword_xa(PID: str, read: int) -> tuple[list, int]:
        details_xa = mappingXA(PID)
        return search_and_read_qword_XA(PID, details_xa, read)

    @staticmethod
    def read_qword_ca(PID: str, read: int) -> tuple[list, int]:
        details_ca = mappingCA(PID)
        return search_and_read_qword_CA(PID, details_ca, read)

    @staticmethod
    def read_qword_a(PID: str, read: int) -> tuple[list, int]:
        details_a = mappingA(PID)
        return search_and_read_qword_A(PID, details_a, read)

    @staticmethod
    def read_qword_all(PID: str, read: int) -> tuple[list, int]:
        details_all = mappingALL(PID)
        return search_and_read_qword_ALL(PID, details_all, read)

    # Word Readers
    @staticmethod
    def read_word_xa(PID: str, read: int) -> tuple[list, int]:
        details_xa = mappingXA(PID)
        return search_and_read_word_XA(PID, details_xa, read)

    @staticmethod
    def read_word_ca(PID: str, read: int) -> tuple[list, int]:
        details_ca = mappingCA(PID)
        return search_and_read_word_CA(PID, details_ca, read)

    @staticmethod
    def read_word_a(PID: str, read: int) -> tuple[list, int]:
        details_a = mappingA(PID)
        return search_and_read_word_A(PID, details_a, read)

    @staticmethod
    def read_word_all(PID: str, read: int) -> tuple[list, int]:
        details_all = mappingALL(PID)
        return search_and_read_word_ALL(PID, details_all, read)

    # Byte Readers
    @staticmethod
    def read_byte_xa(PID: str, read: int) -> tuple[list, int]:
        details_xa = mappingXA(PID)
        return search_and_read_byte_XA(PID, details_xa, read)

    @staticmethod
    def read_byte_ca(PID: str, read: int) -> tuple[list, int]:
        details_ca = mappingCA(PID)
        return search_and_read_byte_CA(PID, details_ca, read)

    @staticmethod
    def read_byte_a(PID: str, read: int) -> tuple[list, int]:
        details_a = mappingA(PID)
        return search_and_read_byte_A(PID, details_a, read)

    @staticmethod
    def read_byte_all(PID: str, read: int) -> tuple[list, int]:
        details_all = mappingALL(PID)
        return search_and_read_byte_ALL(PID, details_all, read)

    # Xor Readers
    @staticmethod
    def read_xor_xa(PID: str, read: int) -> tuple[list, int]:
        details_xa = mappingXA(PID)
        return search_and_read_xor_XA(PID, details_xa, read)

    @staticmethod
    def read_xor_ca(PID: str, read: int) -> tuple[list, int]:
        details_ca = mappingCA(PID)
        return search_and_read_xor_CA(PID, details_ca, read)

    @staticmethod
    def read_xor_a(PID: str, read: int) -> tuple[list, int]:
        details_a = mappingA(PID)
        return search_and_read_xor_A(PID, details_a, read)

    @staticmethod
    def read_xor_all(PID: str, read: int) -> tuple[list, int]:
        details_all = mappingALL(PID)
        return search_and_read_xor_ALL(PID, details_all, read)
