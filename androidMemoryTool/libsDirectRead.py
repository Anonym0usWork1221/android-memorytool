"""
 *  @date   : 2022/03/23
 *  Version : 0.1
 *  @author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# ! /usr/bin/env python
import struct
import sys


def read_lib_offsets_DWORD(PID: str, baseAddress: hex, offset: hex) -> int:
    read_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    value_to_read = int
    try:
        mem_file.seek(read_address)
        value = mem_file.read(4)
        if sys.byteorder == 'little':
            value_to_read = struct.unpack('<i', value)[0]
        else:
            value_to_read = struct.unpack('>i', value)[0]

        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)

    return value_to_read


def read_lib_offsets_FLOAT(PID: str, baseAddress: hex, offset: hex) -> float:
    read_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    value_to_read = int

    try:
        mem_file.seek(read_address)
        value = mem_file.read(4)
        if sys.byteorder == 'little':
            value_to_read = struct.unpack('<f', value)[0]
        else:
            value_to_read = struct.unpack('>f', value)[0]

        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)

    return value_to_read


def read_lib_offsets_DOUBLE(PID: str, baseAddress: hex, offset: hex) -> float:
    read_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    value_to_read = int

    try:
        mem_file.seek(read_address)
        value = mem_file.read(8)
        if sys.byteorder == 'little':
            value_to_read = struct.unpack('<d', value)[0]
        else:
            value_to_read = struct.unpack('>d', value)[0]

        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)

    return value_to_read


def read_lib_offsets_QWORD(PID: str, baseAddress: hex, offset: hex) -> int:
    read_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    value_to_read = int

    try:
        mem_file.seek(read_address)
        value = mem_file.read(8)
        if sys.byteorder == 'little':
            value_to_read = struct.unpack('<q', value)[0]
        else:
            value_to_read = struct.unpack('>q', value)[0]

        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)

    return value_to_read


def read_lib_offsets_WORD(PID: str, baseAddress: hex, offset: hex) -> int:
    read_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    value_to_read = int

    try:
        mem_file.seek(read_address)
        value = mem_file.read(2)
        if sys.byteorder == 'little':
            value_to_read = struct.unpack('<h', value)[0]
        else:
            value_to_read = struct.unpack('>h', value)[0]

        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)

    return value_to_read


def read_lib_offsets_BYTE(PID: str, baseAddress: hex, offset: hex) -> int:
    read_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    value_to_read = int
    try:
        mem_file.seek(read_address)
        value = mem_file.read(1)
        if sys.byteorder == 'little':
            value_to_read = struct.unpack('<b', value)[0]
        else:
            value_to_read = struct.unpack('>b', value)[0]

        mem_file.close()
    except Exception as e:
        print("[*] Exception ", e)

    return value_to_read


def read_lib_offsets_XOR(PID: str, baseAddress: hex, offset: hex) -> int:
    read_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    value_to_read = int

    try:
        mem_file.seek(read_address)
        value = mem_file.read(4)
        if sys.byteorder == 'little':
            value_to_read = struct.unpack('<l', value)[0]
        else:
            value_to_read = struct.unpack('>l', value)[0]

        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)

    return value_to_read
