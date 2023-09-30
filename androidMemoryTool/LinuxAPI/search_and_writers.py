"""
/*
 *  Date     : 2023/09/30
 *  Version  : 0.6
 *  Author   : Abdul Moez
 *  Email    : abdulmoez123456789@gmail.com
 *  Affiliation : Undergraduate at Government College University (GCU) Lahore, Pakistan
 *  GitHub   : https://github.com/Anonym0usWork1221/android-memorytool
 *
 *  Description:
 *  This code is governed by the GNU General Public License, version 3 or later.
 *  You should have received a copy of the GNU General Public License
 *  along with this program. If not, see <https://www.gnu.org/licenses/>.
 */
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
        self._returned_values.put(function(self, *args))

    return wrapper


class SearchAndWrite:
    """
        Class for searching and writing memory values in a process.

        Methods:
            get_writer_values() -> list:
                Retrieves the values stored in the queue.

            reset_queue() -> None:
                Resets the queue to remove all stored values.

            speed_search_and_write(pid: str, address_list: list, buf: int, read: any, write: any) -> int:
                Searches and writes binary values in memory addresses of a process (optimized).

            speed_search_and_write_text(pid: str, address_list: list, read: any, write: any) -> int:
                Searches and writes text values in memory addresses of a process (optimized).

            search_and_write(pid: str, address_list: list, buf: int, read: any, write: any) -> int:
                Searches and writes binary values in memory addresses of a process.

            search_and_write_text(pid: str, address_list: list, read: any, write: any) -> int:
                Searches and writes text values in memory addresses of a process.
    """

    def __init__(self):
        pass

    _returned_values = Queue()

    def get_writer_values(self) -> list:
        """
            Retrieves the values stored in the queue.

            Returns:
                list: List of stored values.
        """
        return self._returned_values.get()

    def reset_queue(self) -> None:
        """
            Resets the queue to remove all stored values.
        """
        self._returned_values.queue.clear()

    @store_in_queue
    def speed_search_and_write(self, pid: str, address_list: list, buf: int, read: any, write: any) -> int:
        """
            Searches and writes binary values in memory addresses of a process (optimized).

            Args:
                pid (str): The process ID.
                address_list (list): List of memory address ranges to search and write.
                buf (int): The number of bytes to read at once.
                read (any): The binary value to search for.
                write (any): The binary value to write.

            Returns:
                int: The total number of values replaced.
        """

        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0
        replaced_addresses = []
        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            current_bytes = 0
            while current_bytes < total_bytes + 1:
                try:
                    current_bytes += buf
                    read_byte = mem_file.read(buf)
                    if read == read_byte:
                        addr = mem_file.seek(-buf, 1)
                        mem_file.write(write)
                        replaced_addresses.append(hex(addr))
                        total_values_replaced += 1
                except IOError:
                    ...

        mem_file.close()
        return total_values_replaced

    @store_in_queue
    def speed_search_and_write_text(self, pid: str, address_list: list, read: any, write: any) -> int:
        """
            Searches and writes text values in memory addresses of a process (optimized).

            Args:
                pid (str): The process ID.
                address_list (list): List of memory address ranges to search and write.
                read (any): The text value to search for.
                write (any): The text value to write.

            Returns:
                int: The total number of values replaced.
        """

        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0
        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            byte_strings = mem_file.read(total_bytes)
            occurrence = [_.start() for _ in finditer(read, byte_strings)]

            for offset in occurrence:
                mem_file.seek(start_addr + offset)
                mem_file.write(write)
                total_values_replaced += 1

        mem_file.close()
        return total_values_replaced

    @store_in_queue
    def speed_group_search_and_write(self, pid: str, address_list: list, buf: int, read_list: list, write: any,
                                     range_val: int) -> int:
        """
        Searches and writes binary values in memory addresses of a process with a specified range.

        Args:
            pid (str): The process ID.
            address_list (list): List of memory address ranges to search and write.
            buf (int): The number of bytes to read at once.
            read_list (list): List of binary values to search for.
            write (any): The binary value to write.
            range_val (int): Maximum distance between the group search values.

        Returns:
            int: The total number of values replaced.
        """
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0

        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            current_bytes = 0
            found_indexes = []
            while current_bytes < total_bytes + 1:
                try:
                    current_bytes += buf
                    read_byte = mem_file.read(buf)
                    if read_byte in read_list:
                        found_indexes.append(mem_file.tell() - buf)
                except IOError:
                    ...

            # Perform range check on found indexes
            for ranged_index in range(len(found_indexes) - 1):
                # Calculation from GameGuardian Post:
                # https://gameguardian.net/forum/topic/8149-gameguadian-group-search/

                if found_indexes[ranged_index + 1] - found_indexes[ranged_index] <= range_val * buf:
                    mem_file.seek(found_indexes[ranged_index])
                    mem_file.write(write)
                    total_values_replaced += 1

        mem_file.close()

        return total_values_replaced

    @staticmethod
    def group_search_and_write(pid: str, address_list: list, buf: int, read_list: list, write: any,
                               range_val: int) -> int:
        """
        Searches and writes binary values in memory addresses of a process with a specified range.

        Args:
            pid (str): The process ID.
            address_list (list): List of memory address ranges to search and write.
            buf (int): The number of bytes to read at once.
            read_list (list): List of binary values to search for.
            write (any): The binary value to write.
            range_val (int): Maximum distance between the group search values.

        Returns:
            int: The total number of values replaced.
        """
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0

        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            current_bytes = 0
            found_indexes = []
            while current_bytes < total_bytes + 1:
                try:
                    current_bytes += buf
                    read_byte = mem_file.read(buf)
                    if read_byte in read_list:
                        found_indexes.append(mem_file.tell() - buf)
                except IOError:
                    ...

            # Perform range check on found indexes
            for ranged_index in range(len(found_indexes) - 1):
                # Calculation from GameGuardian Post:
                # https://gameguardian.net/forum/topic/8149-gameguadian-group-search/

                if found_indexes[ranged_index + 1] - found_indexes[ranged_index] <= range_val * buf:
                    mem_file.seek(found_indexes[ranged_index])
                    mem_file.write(write)
                    total_values_replaced += 1

        mem_file.close()

        return total_values_replaced

    @staticmethod
    def search_and_write(pid: str, address_list: list, buf: int, read: any, write: any) -> int:
        """
            Searches and writes binary values in memory addresses of a process.

            Args:
                pid (str): The process ID.
                address_list (list): List of memory address ranges to search and write.
                buf (int): The number of bytes to read at once.
                read (any): The binary value to search for.
                write (any): The binary value to write.

            Returns:
                int: The total number of values replaced.
        """

        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0

        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            current_bytes = 0
            while current_bytes < total_bytes + 1:
                try:
                    current_bytes += buf
                    read_byte = mem_file.read(buf)
                    if read == read_byte:
                        mem_file.seek(-buf, 1)
                        mem_file.write(write)
                        total_values_replaced += 1
                except IOError:
                    ...

        mem_file.close()

        return total_values_replaced

    @staticmethod
    def search_and_write_text(pid: str, address_list: list, read: any, write: any) -> int:
        """
            Searches and writes text values in memory addresses of a process.

            Args:
                pid (str): The process ID.
                address_list (list): List of memory address ranges to search and write.
                read (any): The text value to search for.
                write (any): The text value to write.

            Returns:
                int: The total number of values replaced.
        """

        mem_file = open(f"/proc/{pid}/mem", "rb+")
        total_values_replaced = 0
        for address in address_list:
            partitions = address.split("-")
            start_addr = int(partitions[0], 16)
            end_addr = int(partitions[1], 16)
            mem_file.seek(start_addr)
            total_bytes = end_addr - start_addr
            byte_strings = mem_file.read(total_bytes)
            occurrence = [_.start() for _ in finditer(read, byte_strings)]

            for offset in occurrence:
                mem_file.seek(start_addr + offset)
                mem_file.write(write)
                total_values_replaced += 1

        mem_file.close()
        return total_values_replaced
