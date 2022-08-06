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


def get_module_base_address(PID: str, module_name: str) -> hex:
    map_file = open(f"/proc/{PID}/maps", 'r')
    address = []
    if map_file is not None:
        for line in map_file.readlines():
            line_split = line.split()
            if module_name in line_split[len(line_split) - 1]:
                address.append(line_split[0].split('-'))
    if len(address) < 1:
        print("[*] Module not found")
        sys.exit()
    base_address = hex(int(address[0][0], 16))
    # end_address = hex(int(address[len(address) - 1][1], 16))

    return base_address


def write_lib_offsets_DWORD(PID: str, baseAddress: hex, offset: hex, value: int) -> None:
    write_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")

    try:
        mem_file.seek(write_address)

        if sys.byteorder == 'little':
            value_to_write = struct.pack('<i', value)
        else:
            value_to_write = struct.pack('>i', value)

        mem_file.write(value_to_write)
        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)


def write_lib_offsets_FLOAT(PID: str, baseAddress: hex, offset: hex, value: float) -> None:
    write_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")

    try:
        mem_file.seek(write_address)

        if sys.byteorder == 'little':
            value_to_write = struct.pack('<f', value)
        else:
            value_to_write = struct.pack('>f', value)

        mem_file.write(value_to_write)
        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)


def write_lib_offsets_DOUBLE(PID: str, baseAddress: hex, offset: hex, value: float) -> None:
    write_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")

    try:
        mem_file.seek(write_address)

        if sys.byteorder == 'little':
            value_to_write = struct.pack('<d', value)
        else:
            value_to_write = struct.pack('>d', value)

        mem_file.write(value_to_write)
        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)


def write_lib_offsets_QWORD(PID: str, baseAddress: hex, offset: hex, value: int) -> None:
    write_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")

    try:
        mem_file.seek(write_address)

        if sys.byteorder == 'little':
            value_to_write = struct.pack('<q', value)
        else:
            value_to_write = struct.pack('>q', value)

        mem_file.write(value_to_write)
        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)


def write_lib_offsets_WORD(PID: str, baseAddress: hex, offset: hex, value: int) -> None:
    write_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")

    try:
        mem_file.seek(write_address)

        if sys.byteorder == 'little':
            value_to_write = struct.pack('<h', value)
        else:
            value_to_write = struct.pack('>h', value)

        mem_file.write(value_to_write)
        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)


def write_lib_offsets_BYTE(PID: str, baseAddress: hex, offset: hex, value: int) -> None:
    write_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")

    try:
        mem_file.seek(write_address)

        if sys.byteorder == 'little':
            value_to_write = struct.pack('<b', value)
        else:
            value_to_write = struct.pack('>b', value)

        mem_file.write(value_to_write)
        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)


def write_lib_offsets_XOR(PID: str, baseAddress: hex, offset: hex, value: int) -> None:
    write_address = int(str(baseAddress), 16) + int(str(offset), 16)
    mem_file = open(f"/proc/{PID}/mem", "rb+")

    try:
        mem_file.seek(write_address)

        if sys.byteorder == 'little':
            value_to_write = struct.pack('<l', value)
        else:
            value_to_write = struct.pack('>l', value)

        mem_file.write(value_to_write)
        mem_file.close()

    except Exception as e:
        print("[*] Exception ", e)
