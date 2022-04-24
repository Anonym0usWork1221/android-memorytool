"""
 *  @date   : 2022/03/23
 *  @author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

 MIT License

 Copyright (c) 2022 AbdulMoez (abdulmoez123456789@gmail.com)

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
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
