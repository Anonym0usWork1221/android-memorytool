"""
 *  @date   : 2022/03/23
 *  Version : 0.1
 *  @author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# ! /usr/bin/env python
import re
import sys
import struct
import queue

returned_v = queue.Queue()


def get_readers_values():
    global returned_v
    return returned_v.get()


def storeInQueue2(f):
    def wrapper(*args):
        returned_v.put(f(*args))

    return wrapper


@storeInQueue2
def speed_search_and_read_text(PID: str, addr: list, read: any):
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0
    offsets = []

    for i in addr:
        partitions = i.split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(read, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1

    mem_file.close()
    return offsets, total_values_found


@storeInQueue2
def speed_search_and_read(PID: str, addr: list, buf: int, read: any):
    mem_file = open(f"/proc/{PID}/mem", "rb+")

    offsets = []
    total_values_found = 0

    for i in addr:
        partitions = i.split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += buf
                read_byte = mem_file.read(buf)
                if read == read_byte:
                    addr = mem_file.seek(-buf, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    return offsets, total_values_found


def search_and_read(PID: str, addr: list, buf: int, read: any):
    mem_file = open(f"/proc/{PID}/mem", "rb+")

    offsets = []
    total_values_found = 0

    for i in addr:
        partitions = i.split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += buf
                read_byte = mem_file.read(buf)
                if read == read_byte:
                    addr = mem_file.seek(-buf, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    return offsets, total_values_found


def search_and_read_text(PID: str, addr: list, read: any):
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0
    offsets = []

    for i in addr:
        partitions = i.split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(read, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1

    mem_file.close()
    return offsets, total_values_found


# UTF-8 architecture

def search_and_read_utf8_XA(PID: str, xa_dict: dict, read: str) -> tuple[list, int]:
    xa_address = xa_dict['address']
    search_value = read.encode('utf-8')

    offsets = []

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1
    mem_file.close()
    return offsets, total_values_found


def search_and_read_utf8_ALL(PID: str, all_dict: dict, read: str) -> tuple[list, int]:
    all_address = all_dict['address']
    search_value = read.encode('utf-8')

    offsets = []

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1
    mem_file.close()
    return offsets, total_values_found


def search_and_read_utf8_CA(PID: str, ca_dict: dict, read: str) -> tuple[list, int]:
    ca_address = ca_dict['address']
    search_value = read.encode('utf-8')
    offsets = []

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1
    mem_file.close()
    return offsets, total_values_found


def search_and_read_utf8_A(PID: str, a_dict: dict, read: str) -> tuple[list, int]:
    a_address = a_dict['address']
    search_value = read.encode('utf-8')
    offsets = []

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1
    mem_file.close()
    return offsets, total_values_found


# UTF-16LE architecture

def search_and_read_utf16LE_XA(PID: str, xa_dict: dict, read: str) -> tuple[list, int]:
    xa_address = xa_dict['address']
    search_value = read.encode('utf-16LE')
    offsets = []

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1
    mem_file.close()
    return offsets, total_values_found


def search_and_read_utf16LE_ALL(PID: str, all_dict: dict, read: str) -> tuple[list, int]:
    all_address = all_dict['address']
    search_value = read.encode('utf-16LE')
    offsets = []

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1
    mem_file.close()
    return offsets, total_values_found


def search_and_read_utf16LE_CA(PID: str, ca_dict: dict, read: str) -> tuple[list, int]:
    ca_address = ca_dict['address']
    search_value = read.encode('utf-16LE')
    offsets = []

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1
    mem_file.close()
    return offsets, total_values_found


def search_and_read_utf16LE_A(PID: str, a_dict: dict, read: str) -> tuple[list, int]:
    a_address = a_dict['address']
    search_value = read.encode('utf-16LE')
    offsets = []

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            offsets.append(hex(startAddr + i))
            total_values_found += 1
    mem_file.close()
    return offsets, total_values_found


# Float architecture

def search_and_read_float_XA(PID: str, xa_dict: dict, read: float) -> tuple[list, int]:
    xa_address = xa_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<f', read)
    else:
        search_value = struct.pack('>f', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_float_ALL(PID: str, all_dict: dict, read: float) -> tuple[list, int]:
    all_address = all_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<f', read)
    else:
        search_value = struct.pack('>f', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_float_CA(PID: str, ca_dict: dict, read: float) -> tuple[list, int]:
    ca_address = ca_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<f', read)
    else:
        search_value = struct.pack('>f', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_float_A(PID: str, a_dict: dict, read: float) -> tuple[list, int]:
    a_address = a_dict['address']
    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<f', read)
    else:
        search_value = struct.pack('>f', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


# Double architecture

def search_and_read_double_XA(PID: str, xa_dict: dict, read: float) -> tuple[list, int]:
    xa_address = xa_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<d', read)
    else:
        search_value = struct.pack('>d', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 8
                read_byte = mem_file.read(8)
                if search_value == read_byte:
                    addr = mem_file.seek(-8, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_double_ALL(PID: str, all_dict: dict, read: float) -> tuple[list, int]:
    all_address = all_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<d', read)
    else:
        search_value = struct.pack('>d', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 8
                read_byte = mem_file.read(8)
                if search_value == read_byte:
                    addr = mem_file.seek(-8, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_double_CA(PID: str, ca_dict: dict, read: float) -> tuple[list, int]:
    ca_address = ca_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<d', read)
    else:
        search_value = struct.pack('>d', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 8
                read_byte = mem_file.read(8)
                if search_value == read_byte:
                    addr = mem_file.seek(-8, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_double_A(PID: str, a_dict: dict, read: float) -> tuple[list, int]:
    a_address = a_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<d', read)
    else:
        search_value = struct.pack('>d', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 8
                read_byte = mem_file.read(8)
                if search_value == read_byte:
                    addr = mem_file.seek(-8, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


# Dword architecture

def search_and_read_dword_XA(PID: str, xa_dict: dict, read: int) -> tuple[list, int]:
    xa_address = xa_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<i', read)
    else:
        search_value = struct.pack('>i', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_dword_ALL(PID: str, all_dict: dict, read: int) -> tuple[list, int]:
    all_address = all_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<i', read)
    else:
        search_value = struct.pack('>i', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_dword_CA(PID: str, ca_dict: dict, read: int) -> tuple[list, int]:
    ca_address = ca_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<i', read)
    else:
        search_value = struct.pack('>i', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_dword_A(PID: str, a_dict: dict, read: int) -> tuple[list, int]:
    a_address = a_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<i', read)
    else:
        search_value = struct.pack('>i', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


# Word architecture

def search_and_read_word_XA(PID: str, xa_dict: dict, read: int) -> tuple[list, int]:
    xa_address = xa_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<h', read)
    else:
        search_value = struct.pack('>h', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 2
                read_byte = mem_file.read(2)
                if search_value == read_byte:
                    addr = mem_file.seek(-2, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_word_ALL(PID: str, all_dict: dict, read: int) -> tuple[list, int]:
    all_address = all_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<h', read)
    else:
        search_value = struct.pack('>h', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 2
                read_byte = mem_file.read(2)
                if search_value == read_byte:
                    addr = mem_file.seek(-2, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_word_CA(PID: str, ca_dict: dict, read: int) -> tuple[list, int]:
    ca_address = ca_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<h', read)
    else:
        search_value = struct.pack('>h', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 2
                read_byte = mem_file.read(2)
                if search_value == read_byte:
                    addr = mem_file.seek(-2, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_word_A(PID: str, a_dict: dict, read: int) -> tuple[list, int]:
    a_address = a_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<h', read)
    else:
        search_value = struct.pack('>h', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 2
                read_byte = mem_file.read(2)
                if search_value == read_byte:
                    addr = mem_file.seek(-2, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


# Qword architecture

def search_and_read_qword_XA(PID: str, xa_dict: dict, read: int) -> tuple[list, int]:
    xa_address = xa_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<q', read)
    else:
        search_value = struct.pack('>q', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 8
                read_byte = mem_file.read(8)
                if search_value == read_byte:
                    addr = mem_file.seek(-8, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_qword_ALL(PID: str, all_dict: dict, read: int) -> tuple[list, int]:
    all_address = all_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<q', read)
    else:
        search_value = struct.pack('>q', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 8
                read_byte = mem_file.read(8)
                if search_value == read_byte:
                    addr = mem_file.seek(-8, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_qword_CA(PID: str, ca_dict: dict, read: int) -> tuple[list, int]:
    ca_address = ca_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<q', read)
    else:
        search_value = struct.pack('>q', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 8
                read_byte = mem_file.read(8)
                if search_value == read_byte:
                    addr = mem_file.seek(-8, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_qword_A(PID: str, a_dict: dict, read: int) -> tuple[list, int]:
    a_address = a_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<q', read)
    else:
        search_value = struct.pack('>q', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 8
                read_byte = mem_file.read(8)
                if search_value == read_byte:
                    addr = mem_file.seek(-8, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


# Bytes architecture

def search_and_read_byte_XA(PID: str, xa_dict: dict, read: int) -> tuple[list, int]:
    xa_address = xa_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<b', read)
    else:
        search_value = struct.pack('>b', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 1
                read_byte = mem_file.read(1)
                if search_value == read_byte:
                    addr = mem_file.seek(-1, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_byte_ALL(PID: str, all_dict: dict, read: int) -> tuple[list, int]:
    all_address = all_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<b', read)
    else:
        search_value = struct.pack('>b', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 1
                read_byte = mem_file.read(1)
                if search_value == read_byte:
                    addr = mem_file.seek(-1, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_byte_CA(PID: str, ca_dict: dict, read: int) -> tuple[list, int]:
    ca_address = ca_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<b', read)
    else:
        search_value = struct.pack('>b', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 1
                read_byte = mem_file.read(1)
                if search_value == read_byte:
                    addr = mem_file.seek(-1, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_byte_A(PID: str, a_dict: dict, read: int) -> tuple[list, int]:
    a_address = a_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<b', read)
    else:
        search_value = struct.pack('>b', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 1
                read_byte = mem_file.read(1)
                if search_value == read_byte:
                    addr = mem_file.seek(-1, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


# Xor architecture

def search_and_read_xor_XA(PID: str, xa_dict: dict, read: int) -> tuple[list, int]:
    xa_address = xa_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<l', read)
    else:
        search_value = struct.pack('>l', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_xor_ALL(PID: str, all_dict: dict, read: int) -> tuple[list, int]:
    all_address = all_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<l', read)
    else:
        search_value = struct.pack('>l', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_xor_CA(PID: str, ca_dict: dict, read: int) -> tuple[list, int]:
    ca_address = ca_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<l', read)
    else:
        search_value = struct.pack('>l', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found


def search_and_read_xor_A(PID: str, a_dict: dict, read: int) -> tuple[list, int]:
    a_address = a_dict['address']

    offsets = []

    if sys.byteorder == 'little':
        search_value = struct.pack('<l', read)
    else:
        search_value = struct.pack('>l', read)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_found = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        current_bytes = 0
        try:
            while current_bytes < total_bytes + 1:
                current_bytes += 4
                read_byte = mem_file.read(4)
                if search_value == read_byte:
                    addr = mem_file.seek(-4, 1)
                    offsets.append(hex(startAddr + addr))
                    total_values_found += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_found)
    return offsets, total_values_found
