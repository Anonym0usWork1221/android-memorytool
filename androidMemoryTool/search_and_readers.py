"""
 *  date   : 2023/07/11
 *  Version : 0.5
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# ! /usr/bin/env python
from functools import wraps
from queue import Queue
from re import finditer


def store_in_queue(function) -> any:
    """
        Decorator function that stores the return value of the decorated function in a queue.

        Args:
            function: The function to be decorated.

        Returns:
            any: The return value of the decorated function.
    """

    @wraps(function)
    def wrapper(self, *args):
        self._returned_v.put(function(self, *args))

    return wrapper


class SearchAndRead:
    """
    Class for searching and reading memory values in a process.

    Methods:
        get_readers_values() -> list:
            Retrieves the values stored in the queue.

        reset_queue() -> None:
            Resets the queue to remove all stored values.

        speed_search_and_read_text(pid: str, address_list: list, read: any) -> tuple[list[str], int]:
            Searches and reads text values from memory addresses in a process (optimized).

        speed_search_and_read(pid: str, address_list: list, buf: int, read: any) -> tuple[list[str], int]:
            Searches and reads binary values from memory addresses in a process (optimized).

        search_and_read(pid: str, address_list: list, buf: int, read: any) -> list:
            Searches and reads binary values from memory addresses in a process.

        search_and_read_text(pid: str, address_list: list, read: any) -> list:
            Searches and reads text values from memory addresses in a process.
    """

    def __init__(self):
        pass

    _returned_v = Queue()

    def get_readers_values(self) -> list:
        """
            Retrieves the values stored in the queue.

            Returns:
                list: List of stored values.
        """

        return self._returned_v.get()

    def reset_queue(self) -> None:
        """
            Resets the queue to remove all stored values.
        """

        self._returned_v.queue.clear()

    @store_in_queue
    def speed_search_and_read_text(self, pid: str, address_list: list, read: any) -> tuple[list[str], int]:
        """
            Searches and reads text values from memory addresses in a process (optimized).

            Args:
                pid (str): The process ID.
                address_list (list): List of memory address ranges to search and read.
                read (any): The text value to search for.

            Returns:
                tuple[list[str], int]: Tuple containing a list of found offsets and the total number of values found.
        """

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
            occurrence = [_.start() for _ in finditer(read, byte_strings)]

            for offset in occurrence:
                offsets.append(hex(offset))   # fixed illegal calculation of hex value
                total_values_found += 1

        mem_file.close()
        return offsets, total_values_found

    @store_in_queue
    def speed_search_and_read(self, pid: str, address_list: list, buf: int, read: any) -> tuple[list[str], int]:
        """
            Searches and reads binary values from memory addresses in a process (optimized).

            Args:
                pid (str): The process ID.
                address_list (list): List of memory address ranges to search and read.
                buf (int): The number of bytes to read at once.
                read (any): The binary value to search for.

            Returns:
                tuple[list[str], int]: Tuple containing a list of found offsets and the total number of values found.
        """

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
                        offsets.append(hex(address_list))  # fixed illegal calculation of hex value
                        total_values_found += 1
            except Exception as e:
                print("[*] Exception ", e)

        mem_file.close()
        return offsets, total_values_found

    @staticmethod
    def search_and_read(pid: str, address_list: list, buf: int, read: any) -> list:
        """
            Searches and reads binary values from memory addresses in a process.

            Args:
                pid (str): The process ID.
                address_list (list): List of memory address ranges to search and read.
                buf (int): The number of bytes to read at once.
                read (any): The binary value to search for.

            Returns:
                list: List containing a list of found offsets and the total number of values found.
        """

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
                        offsets.append(hex(address_list))  # fixed illegal calculation of hex value
                        total_values_found += 1
            except Exception as e:
                print("[*] Exception ", e)

        mem_file.close()
        return list([offsets, total_values_found])

    @staticmethod
    def search_and_read_text(pid: str, address_list: list, read: any) -> list:
        """
            Searches and reads text values from memory addresses in a process.

            Args:
                pid (str): The process ID.
                address_list (list): List of memory address ranges to search and read.
                read (any): The text value to search for.

            Returns:
                list: List containing a list of found offsets and the total number of values found.
        """

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
            occurrence = [_.start() for _ in finditer(read, byte_strings)]

            for offset in occurrence:
                offsets.append(hex(offset))  # fixed illegal calculation of hex value
                total_values_found += 1

        mem_file.close()
        return list([offsets, total_values_found])
