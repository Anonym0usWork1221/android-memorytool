"""
 *  date   : 2022/03/23
 *  Version : 0.3
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
        self._returned_values.put(function(self, *args))
    return wrapper


class SearchAndWrite:
    _returned_values = queue.Queue()

    def get_writer_values(self) -> list:
        return self._returned_values.get()

    @store_in_queue
    def speed_search_and_write(self, pid: str, address_list: list, buf: int, read: any, write: any) -> int:
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0

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
                        addr = mem_file.seek(-buf, 1)
                        print(addr)
                        mem_file.write(write)
                        total_values_replaced += 1
            except Exception as e:
                print("[*] Exception ", e)

        mem_file.close()

        return total_values_replaced

    @store_in_queue
    def speed_search_and_write_text(self, pid: str, address_list: list, read: any, write: any) -> int:
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0
        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            byte_strings = mem_file.read(total_bytes)
            occurrence = [_.start() for _ in re.finditer(read, byte_strings)]

            for offset in occurrence:
                mem_file.seek(start_addr + offset)
                mem_file.write(write)
                total_values_replaced += 1

        mem_file.close()
        return total_values_replaced

    @staticmethod
    def search_and_write(pid: str, address_list: list, buf: int, read: any, write: any) -> int:
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0

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
                        mem_file.seek(-buf, 1)
                        mem_file.write(write)
                        total_values_replaced += 1
            except Exception as e:
                print("[*] Exception ", e)

        mem_file.close()

        return total_values_replaced

    @staticmethod
    def search_and_write_text(pid: str, address_list: list, read: any, write: any) -> int:
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0
        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            byte_strings = mem_file.read(total_bytes)
            occurrence = [_.start() for _ in re.finditer(read, byte_strings)]

            for offset in occurrence:
                mem_file.seek(start_addr + offset)
                mem_file.write(write)
                total_values_replaced += 1

        mem_file.close()
        return total_values_replaced
