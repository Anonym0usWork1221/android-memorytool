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
