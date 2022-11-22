""""
 *  date   : 2022/11/19
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
        self._returned_values.put(function(self, *args))
    return wrapper


class AdditionalFeatures:
    _returned_values = queue.Queue()

    def get_pattern_finder_values(self) -> list:
        return self._returned_values.get()

    def reset_queue(self) -> None:
        self._returned_values.queue.clear()

    @store_in_queue
    def speed_find_hexadecimal_pattern(self, pid: str, address_list: list, buf: int, hex_pattern: str) -> list:
        mem_file = open(f"/proc/{pid}/mem", "rb+")

        offsets = []
        founded_patterns = []
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
                    read_hex = mem_file.read(buf).hex().upper()
                    if re.search(hex_pattern, str(read_hex)):
                        founded_patterns.append(read_hex)

                        address_list = mem_file.seek(-buf, 1)
                        mem_file.read(buf)
                        offsets.append(hex(start_addr + address_list))
                        total_values_found += 1
            except Exception as e:
                print("[*] Exception ", e)

        mem_file.close()

        return list([offsets, total_values_found, founded_patterns])

    @staticmethod
    def find_hexadecimal_pattern(pid: str, address_list: list, buf: int, hex_pattern: str) -> list:
        mem_file = open(f"/proc/{pid}/mem", "rb+")

        offsets = []
        founded_patterns = []
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
                    read_hex = mem_file.read(buf).hex().upper()
                    if re.search(hex_pattern, str(read_hex)):
                        founded_patterns.append(read_hex)

                        address_list = mem_file.seek(-buf, 1)
                        mem_file.read(buf)
                        offsets.append(hex(start_addr + address_list))
                        total_values_found += 1
            except Exception as e:
                print("[*] Exception ", e)

        mem_file.close()
        return list([offsets, total_values_found, founded_patterns])
