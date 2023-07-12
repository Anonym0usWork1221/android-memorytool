""""
 *  date   : 2023/07/11
 *  Version : 0.5
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# ! /usr/bin/env python

from functools import wraps
from queue import Queue
from re import search


def store_in_queue(function) -> any:
    """
        Decorator that stores the return value of a function in a queue.

        Args:
            function: The function to be decorated.

        Returns:
            The decorated function.
    """

    @wraps(function)
    def wrapper(self, *args):
        self._returned_values.put(function(self, *args))

    return wrapper


class AdditionalFeatures:
    """
        Class for additional features of memory manipulation.

        Methods:
            get_pattern_finder_values() -> list:
                Retrieves the values from the pattern finder operation.

            reset_queue() -> None:
                Resets the queue of returned values.

            speed_find_hexadecimal_pattern(pid: str, address_list: list, buf: int, hex_pattern: str) -> list:
                Searches for a hexadecimal pattern in memory addresses using speed optimization.

            find_hexadecimal_pattern(pid: str, address_list: list, buf: int, hex_pattern: str) -> list:
                Searches for a hexadecimal pattern in memory addresses.
    """

    def __init__(self):
        pass

    _returned_values = Queue()

    def get_pattern_finder_values(self) -> list:
        """
            Retrieves the values from the pattern finder operation.

            Returns:
                The values from the pattern finder operation.
        """
        return self._returned_values.get()

    def reset_queue(self) -> None:
        """
            Resets the queue of returned values.
        """
        self._returned_values.queue.clear()

    @store_in_queue
    def speed_find_hexadecimal_pattern(self, pid: str, address_list: list, buf: int, hex_pattern: str) -> list:
        """
            Searches for a hexadecimal pattern in memory addresses using speed optimization.

            Args:
                pid (str): The process ID.
                address_list (list): The list of memory addresses to search.
                buf (int): The buffer size for reading memory.
                hex_pattern (str): The hexadecimal pattern to search for.

            Returns:
                list: A list containing the offsets, total values found, and founded patterns.
        """

        offsets = []
        founded_patterns = []
        total_values_found = 0

        with open(f"/proc/{pid}/mem", "rb+") as mem_file:
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
                        read_bytes = mem_file.read(buf)
                        read_hex = read_bytes.hex().upper()
                        # print(f"{read_hex}\t{hex_pattern}")
                        if search(hex_pattern, read_hex):
                            founded_patterns.append(read_hex)
                            current_pos = mem_file.tell() - buf
                            mem_file.seek(current_pos)
                            mem_file.read(buf)
                            offsets.append(hex(current_pos))
                            total_values_found += 1
                except Exception as e:
                    print("[*] Exception ", e)

        return [offsets, total_values_found, founded_patterns]

    @staticmethod
    def find_hexadecimal_pattern(pid: str, address_list: list, buf: int, hex_pattern: str) -> list:
        """
            Searches for a hexadecimal pattern in memory addresses.

            Args:
                pid (str): The process ID.
                address_list (list): The list of memory addresses to search.
                buf (int): The buffer size for reading memory.
                hex_pattern (str): The hexadecimal pattern to search for.

            Returns:
                list: A list containing the offsets, total values found, and founded patterns.
        """

        offsets = []
        founded_patterns = []
        total_values_found = 0

        with open(f"/proc/{pid}/mem", "rb+") as mem_file:
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
                        read_bytes = mem_file.read(buf)
                        read_hex = read_bytes.hex().upper()
                        if search(hex_pattern, read_hex):
                            founded_patterns.append(read_hex)
                            current_pos = mem_file.tell() - buf
                            mem_file.seek(current_pos)
                            mem_file.read(buf)
                            offsets.append(hex(current_pos))
                            total_values_found += 1
                except Exception as e:
                    print("[*] Exception ", e)

        return [offsets, total_values_found, founded_patterns]

    @store_in_queue
    def speed_find_and_replace_hexadecimal_pattern(self, pid: str, address_list: list, buf: int,
                                                   search_pattern: str, replace_pattern: str) -> list:
        """
            Searches for a hexadecimal pattern in memory addresses and replaces it with a new pattern using speed optimization.

            Args:
                pid (str): The process ID.
                address_list (list): The list of memory addresses to search and replace.
                buf (int): The buffer size for reading memory.
                search_pattern (str): The hexadecimal pattern to search for.
                replace_pattern (str): The hexadecimal pattern to replace the found pattern with.

            Returns:
                list: A list containing the offsets, total values found, and founded patterns.
        """

        offsets = []
        founded_patterns = []
        total_values_found = 0

        with open(f"/proc/{pid}/mem", "rb+") as mem_file:
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
                        read_bytes = mem_file.read(buf)
                        read_hex = read_bytes.hex().upper()
                        if search(search_pattern, read_hex):
                            founded_patterns.append(read_hex)
                            current_pos = mem_file.tell() - buf
                            mem_file.seek(current_pos)
                            byte_array_conversion = bytearray.fromhex(replace_pattern)
                            mem_file.write(byte_array_conversion)
                            offsets.append(hex(current_pos))
                            total_values_found += 1
                except Exception as e:
                    print("[*] Exception ", e)

        return [offsets, total_values_found, founded_patterns]

    @staticmethod
    def find_and_replace_hexadecimal_pattern(pid: str, address_list: list, buf: int,
                                             search_pattern: str, replace_pattern: str) -> list:
        """
            Searches for a hexadecimal pattern in memory addresses and replaces it with a new pattern.

            Args:
                pid (str): The process ID.
                address_list (list): The list of memory addresses to search and replace.
                buf (int): The buffer size for reading memory.
                search_pattern (str): The hexadecimal pattern to search for.
                replace_pattern (str): The hexadecimal pattern to replace the found pattern with.

            Returns:
                list: A list containing the offsets, total values found, and founded patterns.
        """
        offsets = []
        founded_patterns = []
        total_values_found = 0

        with open(f"/proc/{pid}/mem", "rb+") as mem_file:
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
                        read_bytes = mem_file.read(buf)
                        read_hex = read_bytes.hex().upper()
                        if search(search_pattern, read_hex):
                            founded_patterns.append(read_hex)
                            current_pos = mem_file.tell() - buf
                            mem_file.seek(current_pos)
                            byte_array_conversion = bytearray.fromhex(replace_pattern)
                            mem_file.write(byte_array_conversion)
                            offsets.append(hex(current_pos))
                            total_values_found += 1
                except Exception as e:
                    print("[*] Exception ", e)

        return [offsets, total_values_found, founded_patterns]
