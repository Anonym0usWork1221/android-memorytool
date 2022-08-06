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

returned_values = queue.Queue()


def get_writer_values():
    global returned_values
    return returned_values.get()


def storeInQueue(f):
    def wrapper(*args):
        returned_values.put(f(*args))

    return wrapper


@storeInQueue
def speed_search_and_write(PID: str, addr: list, buf: int, read: any, write: any):
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-buf, 1)
                    mem_file.write(write)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()

    return total_values_replaced


@storeInQueue
def speed_search_and_write_text(PID: str, addr: list, read: any, write: any):
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0
    for i in addr:
        partitions = i.split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(read, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(write)
            total_values_replaced += 1

    mem_file.close()
    return total_values_replaced


def search_and_write(PID: str, addr: list, buf: int, read: any, write: any):
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-buf, 1)
                    mem_file.write(write)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()

    return total_values_replaced


def search_and_write_text(PID: str, addr: list, read: any, write: any):
    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0
    for i in addr:
        partitions = i.split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(read, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(write)
            total_values_replaced += 1

    mem_file.close()
    return total_values_replaced


# UTF-8 architecture

def search_and_write_utf8_XA(PID: str, xa_dict: dict, read: str, write: str) -> int:
    xa_address = xa_dict['address']
    search_value = read.encode('utf-8')
    replace_value = write.encode('utf-8')

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(replace_value)
            total_values_replaced += 1

    return total_values_replaced


def search_and_write_utf8_ALL(PID: str, all_dict: dict, read: str, write: str) -> int:
    all_address = all_dict['address']
    search_value = read.encode('utf-8')
    replace_value = write.encode('utf-8')

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(replace_value)
            total_values_replaced += 1

    return total_values_replaced


def search_and_write_utf8_CA(PID: str, ca_dict: dict, read: str, write: str) -> int:
    ca_address = ca_dict['address']
    search_value = read.encode('utf-8')
    replace_value = write.encode('utf-8')

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(replace_value)
            total_values_replaced += 1

    return total_values_replaced


def search_and_write_utf8_A(PID: str, a_dict: dict, read: str, write: str) -> int:
    a_address = a_dict['address']
    search_value = read.encode('utf-8')
    replace_value = write.encode('utf-8')

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(replace_value)
            total_values_replaced += 1

    return total_values_replaced


# UTF-16LE architecture

def search_and_write_utf16LE_XA(PID: str, xa_dict: dict, read: str, write: str) -> int:
    xa_address = xa_dict['address']
    search_value = read.encode('utf-16LE')
    replace_value = write.encode('utf-16LE')

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

    for addr in range(0, len(xa_address)):
        partitions = xa_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(replace_value)
            total_values_replaced += 1

    return total_values_replaced


def search_and_write_utf16LE_ALL(PID: str, all_dict: dict, read: str, write: str) -> int:
    all_address = all_dict['address']
    search_value = read.encode('utf-16LE')
    replace_value = write.encode('utf-16LE')

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

    for addr in range(0, len(all_address)):
        partitions = all_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(replace_value)
            total_values_replaced += 1

    return total_values_replaced


def search_and_write_utf16LE_CA(PID: str, ca_dict: dict, read: str, write: str) -> int:
    ca_address = ca_dict['address']
    search_value = read.encode('utf-16LE')
    replace_value = write.encode('utf-16LE')

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

    for addr in range(0, len(ca_address)):
        partitions = ca_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(replace_value)
            total_values_replaced += 1

    return total_values_replaced


def search_and_write_utf16LE_A(PID: str, a_dict: dict, read: str, write: str) -> int:
    a_address = a_dict['address']
    search_value = read.encode('utf-16LE')
    replace_value = write.encode('utf-16LE')

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

    for addr in range(0, len(a_address)):
        partitions = a_address[addr].split("-")
        startAddr = int(partitions[0], 16)
        endAddr = int(partitions[1], 16)
        mem_file.seek(startAddr)
        total_bytes = endAddr - startAddr
        byte_strings = mem_file.read(total_bytes)
        occurrence = [_.start() for _ in re.finditer(search_value, byte_strings)]

        for i in occurrence:
            mem_file.seek(startAddr + i)
            mem_file.write(replace_value)
            total_values_replaced += 1

    return total_values_replaced


# Float architecture

def search_and_write_float_XA(PID: str, xa_dict: dict, read: float, write: float) -> int:
    xa_address = xa_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<f', read)
        replace_value = struct.pack('<f', write)
    else:
        search_value = struct.pack('>f', read)
        replace_value = struct.pack('>f', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_float_ALL(PID: str, all_dict: dict, read: float, write: float) -> int:
    all_address = all_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<f', read)
        replace_value = struct.pack('<f', write)
    else:
        search_value = struct.pack('>f', read)
        replace_value = struct.pack('>f', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_float_CA(PID: str, ca_dict: dict, read: float, write: float) -> int:
    ca_address = ca_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<f', read)
        replace_value = struct.pack('<f', write)
    else:
        search_value = struct.pack('>f', read)
        replace_value = struct.pack('>f', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_float_A(PID: str, a_dict: dict, read: float, write: float) -> int:
    a_address = a_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<f', read)
        replace_value = struct.pack('<f', write)
    else:
        search_value = struct.pack('>f', read)
        replace_value = struct.pack('>f', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


# Double architecture

def search_and_write_double_XA(PID: str, xa_dict: dict, read: float, write: float) -> int:
    xa_address = xa_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<d', read)
        replace_value = struct.pack('<d', write)
    else:
        search_value = struct.pack('>d', read)
        replace_value = struct.pack('>d', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-8, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_double_ALL(PID: str, all_dict: dict, read: float, write: float) -> int:
    all_address = all_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<d', read)
        replace_value = struct.pack('<d', write)
    else:
        search_value = struct.pack('>d', read)
        replace_value = struct.pack('>d', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-8, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_double_CA(PID: str, ca_dict: dict, read: float, write: float) -> int:
    ca_address = ca_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<d', read)
        replace_value = struct.pack('<d', write)
    else:
        search_value = struct.pack('>d', read)
        replace_value = struct.pack('>d', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-8, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_double_A(PID: str, a_dict: dict, read: float, write: float) -> int:
    a_address = a_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<d', read)
        replace_value = struct.pack('<d', write)
    else:
        search_value = struct.pack('>d', read)
        replace_value = struct.pack('>d', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-8, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1
        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


# Dword architecture

def search_and_write_dword_XA(PID: str, xa_dict: dict, read: int, write: int) -> int:
    xa_address = xa_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<i', read)
        replace_value = struct.pack('<i', write)
    else:
        search_value = struct.pack('>i', read)
        replace_value = struct.pack('>i', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_dword_ALL(PID: str, all_dict: dict, read: int, write: int) -> int:
    all_address = all_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<i', read)
        replace_value = struct.pack('<i', write)
    else:
        search_value = struct.pack('>i', read)
        replace_value = struct.pack('>i', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_dword_CA(PID: str, ca_dict: dict, read: int, write: int) -> int:
    ca_address = ca_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<i', read)
        replace_value = struct.pack('<i', write)
    else:
        search_value = struct.pack('>i', read)
        replace_value = struct.pack('>i', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_dword_A(PID: str, a_dict: dict, read: int, write: int) -> int:
    a_address = a_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<i', read)
        replace_value = struct.pack('<i', write)
    else:
        search_value = struct.pack('>i', read)
        replace_value = struct.pack('>i', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


# Word architecture

def search_and_write_word_XA(PID: str, xa_dict: dict, read: int, write: int) -> int:
    xa_address = xa_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<h', read)
        replace_value = struct.pack('<h', write)
    else:
        search_value = struct.pack('>h', read)
        replace_value = struct.pack('>h', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-2, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_word_ALL(PID: str, all_dict: dict, read: int, write: int) -> int:
    all_address = all_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<h', read)
        replace_value = struct.pack('<h', write)
    else:
        search_value = struct.pack('>h', read)
        replace_value = struct.pack('>h', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-2, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_word_CA(PID: str, ca_dict: dict, read: int, write: int) -> int:
    ca_address = ca_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<h', read)
        replace_value = struct.pack('<h', write)
    else:
        search_value = struct.pack('>h', read)
        replace_value = struct.pack('>h', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-2, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_word_A(PID: str, a_dict: dict, read: int, write: int) -> int:
    a_address = a_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<h', read)
        replace_value = struct.pack('<h', write)
    else:
        search_value = struct.pack('>h', read)
        replace_value = struct.pack('>h', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-2, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


# Qword architecture

def search_and_write_qword_XA(PID: str, xa_dict: dict, read: int, write: int) -> int:
    xa_address = xa_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<q', read)
        replace_value = struct.pack('<q', write)
    else:
        search_value = struct.pack('>q', read)
        replace_value = struct.pack('>q', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-8, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_qword_ALL(PID: str, all_dict: dict, read: int, write: int) -> int:
    all_address = all_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<q', read)
        replace_value = struct.pack('<q', write)
    else:
        search_value = struct.pack('>q', read)
        replace_value = struct.pack('>q', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-8, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_qword_CA(PID: str, ca_dict: dict, read: int, write: int) -> int:
    ca_address = ca_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<q', read)
        replace_value = struct.pack('<q', write)
    else:
        search_value = struct.pack('>q', read)
        replace_value = struct.pack('>q', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-8, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_qword_A(PID: str, a_dict: dict, read: int, write: int) -> int:
    a_address = a_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<q', read)
        replace_value = struct.pack('<q', write)
    else:
        search_value = struct.pack('>q', read)
        replace_value = struct.pack('>q', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-8, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


# Bytes architecture

def search_and_write_byte_XA(PID: str, xa_dict: dict, read: int, write: int) -> int:
    xa_address = xa_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<b', read)
        replace_value = struct.pack('<b', write)
    else:
        search_value = struct.pack('>b', read)
        replace_value = struct.pack('>b', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-1, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_byte_ALL(PID: str, all_dict: dict, read: int, write: int) -> int:
    all_address = all_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<b', read)
        replace_value = struct.pack('<b', write)
    else:
        search_value = struct.pack('>b', read)
        replace_value = struct.pack('>b', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-1, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_byte_CA(PID: str, ca_dict: dict, read: int, write: int) -> int:
    ca_address = ca_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<b', read)
        replace_value = struct.pack('<b', write)
    else:
        search_value = struct.pack('>b', read)
        replace_value = struct.pack('>b', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-1, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_byte_A(PID: str, a_dict: dict, read: int, write: int) -> int:
    a_address = a_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<b', read)
        replace_value = struct.pack('<b', write)
    else:
        search_value = struct.pack('>b', read)
        replace_value = struct.pack('>b', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-1, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


# Xor architecture

def search_and_write_xor_XA(PID: str, xa_dict: dict, read: int, write: int) -> int:
    xa_address = xa_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<l', read)
        replace_value = struct.pack('<l', write)
    else:
        search_value = struct.pack('>l', read)
        replace_value = struct.pack('>l', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_xor_ALL(PID: str, all_dict: dict, read: int, write: int) -> int:
    all_address = all_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<l', read)
        replace_value = struct.pack('<l', write)
    else:
        search_value = struct.pack('>l', read)
        replace_value = struct.pack('>l', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_xor_CA(PID: str, ca_dict: dict, read: int, write: int) -> int:
    ca_address = ca_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<l', read)
        replace_value = struct.pack('<l', write)
    else:
        search_value = struct.pack('>l', read)
        replace_value = struct.pack('>l', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced


def search_and_write_xor_A(PID: str, a_dict: dict, read: int, write: int) -> int:
    a_address = a_dict['address']

    if sys.byteorder == 'little':
        search_value = struct.pack('<l', read)
        replace_value = struct.pack('<l', write)
    else:
        search_value = struct.pack('>l', read)
        replace_value = struct.pack('>l', write)

    mem_file = open(f"/proc/{PID}/mem", "rb+")
    total_values_replaced = 0

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
                    mem_file.seek(-4, 1)
                    mem_file.write(replace_value)
                    total_values_replaced += 1

        except Exception as e:
            print("[*] Exception ", e)

    mem_file.close()
    # print("[*] Values replaced ", total_values_replaced)
    return total_values_replaced
