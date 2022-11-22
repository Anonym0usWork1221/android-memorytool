"""
 *  date   : 2022/03/23
 *  Version : 0.4
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# ! /usr/bin/env python
import re
import queue
from functools import wraps


def store_in_queue(function) -> any:
    @wraps(function)
    def wrapper(self, *args):
        self._returned_v.put(function(self, *args))

    return wrapper


class SearchAndRead:
    _returned_v = queue.Queue()

    def get_readers_values(self) -> list:
        return self._returned_v.get()

    def reset_queue(self) -> None:
        self._returned_v.queue.clear()

    @store_in_queue
    def speed_search_and_read_text(self, pid: str, address_list: list, read: any) -> tuple[list[str], int]:
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_found = 0
        offsets = []

        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            byte_strings = mem_file.read(total_bytes)
            occurrence = [_.start() for _ in re.finditer(read, byte_strings)]

            for offset in occurrence:
                offsets.append(hex(start_addr + offset))
                total_values_found += 1

        mem_file.close()
        return offsets, total_values_found

    @store_in_queue
    def speed_search_and_read(self, pid: str, address_list: list, buf: int, read: any) -> tuple[list[str], int]:
        mem_file = open(f"/proc/{pid}/mem", "rb+")

        offsets = []
        total_values_found = 0

        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            current_bytes = 0
            try:
                while current_bytes < total_bytes + 1:
                    current_bytes += buf
                    read_byte = mem_file.read(buf)
                    if read == read_byte:
                        address_list = mem_file.seek(-buf, 1)
                        mem_file.read(buf)
                        offsets.append(hex(start_addr + address_list))
                        total_values_found += 1
            except Exception as e:
                print("[*] Exception ", e)

        mem_file.close()
        return offsets, total_values_found

    @staticmethod
    def search_and_read(pid: str, address_list: list, buf: int, read: any) -> list:
        mem_file = open(f"/proc/{pid}/mem", "rb+")

        offsets = []
        total_values_found = 0

        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            current_bytes = 0
            try:
                while current_bytes < total_bytes + 1:
                    current_bytes += buf
                    read_byte = mem_file.read(buf)
                    if read == read_byte:
                        address_list = mem_file.seek(-buf, 1)
                        mem_file.read(buf)
                        offsets.append(hex(start_addr + address_list))
                        total_values_found += 1
            except Exception as e:
                print("[*] Exception ", e)

        mem_file.close()
        return list([offsets, total_values_found])

    @staticmethod
    def search_and_read_text(pid: str, address_list: list, read: any) -> list:
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_found = 0
        offsets = []

        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            byte_strings = mem_file.read(total_bytes)
            occurrence = [_.start() for _ in re.finditer(read, byte_strings)]

            for offset in occurrence:
                offsets.append(hex(start_addr + offset))
                total_values_found += 1

        mem_file.close()
        return list([offsets, total_values_found])
