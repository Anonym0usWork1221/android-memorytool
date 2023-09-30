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

from ..errors_class import WINAPIException
from functools import wraps
from sys import byteorder
from queue import Queue
import ctypes.wintypes
from enum import Enum
import ctypes
import re


# Constants for maximum path length and buffer size
MAX_PATH = 260
BUFFER_SIZE = 4096

# Necessary memory protection constants
PAGE_READWRITE = 0x04
PAGE_WRITECOPY = 0x08
PAGE_EXECUTE_READWRITE = 0x40
PAGE_EXECUTE_WRITECOPY = 0x80


def store_in_queue(function) -> any:
    """
    A decorator function that stores the result of the wrapped function in a queue.

    Args:
        function: The function to be wrapped.

    Returns:
        A wrapper function that puts the result of the wrapped function in a queue.
    """

    @wraps(function)
    def wrapper(self, *args):
        self._returned_values.put(function(self, *args))

    return wrapper


class MemoryAllocationStatesEnum(Enum):
    MEM_COMMIT = 0x1000
    MEM_FREE = 0x10000
    MEM_LARGE_PAGES = 0x20000000
    MEM_PHYSICAL = 0x00400000
    MEM_TOP_DOWN = 0x00100000
    MEM_RESERVE = 0x2000
    MEM_RESET = 0x00080000
    MEM_RESET_UNDO = 0x1000000


class MemoryTypesEnum(Enum):
    MEM_IMAGE = 0x1000000
    MEM_MAPPED = 0x40000
    MEM_PRIVATE = 0x20000


class MemoryProtectionsEnum(Enum):
    PAGE_EXECUTE = 0x10
    PAGE_EXECUTE_READ = 0x20
    PAGE_EXECUTE_READWRITE = 0x40
    PAGE_EXECUTE_WRITECOPY = 0x80
    PAGE_GUARD = 0x100
    PAGE_NOACCESS = 0x01
    PAGE_NOCACHE = 0x200
    PAGE_READONLY = 0x02
    PAGE_READWRITE = 0x04
    PAGE_READABLE = PAGE_EXECUTE_READ | PAGE_EXECUTE_READWRITE | PAGE_READWRITE
    PAGE_TARGETS_INVALID = 0x40000000
    PAGE_TARGETS_NO_UPDATE = 0x40000000
    PAGE_WRITECOPY = 0x08
    PAGE_WRITECOMBINE = 0x400


class MemoryBasicInformation(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_void_p),
        ("AllocationBase", ctypes.c_void_p),
        ("AllocationProtect", ctypes.c_uint32),
        ("RegionSize", ctypes.c_size_t),
        ("State", ctypes.c_uint32),
        ("Protect", ctypes.c_uint32),
        ("Type", ctypes.c_uint32),
    ]


class MemoryBasicInformation64(ctypes.Structure):
    _fields_ = [
        ("BaseAddress", ctypes.c_ulonglong),
        ("AllocationBase", ctypes.c_ulonglong),
        ("AllocationProtect", ctypes.wintypes.DWORD),
        ("__alignment1", ctypes.wintypes.DWORD),
        ("RegionSize", ctypes.c_ulonglong),
        ("State", ctypes.wintypes.DWORD),
        ("Protect", ctypes.wintypes.DWORD),
        ("Type", ctypes.wintypes.DWORD),
        ("__alignment2", ctypes.wintypes.DWORD),
    ]


class SystemInfo(ctypes.Structure):
    _fields_ = [
        ("wProcessorArchitecture", ctypes.wintypes.WORD),
        ("wReserved", ctypes.wintypes.WORD),
        ("dwPageSize", ctypes.wintypes.DWORD),
        ("lpMinimumApplicationAddress", ctypes.c_void_p),
        ("lpMaximumApplicationAddress", ctypes.c_void_p),
        ("dwActiveProcessorMask", ctypes.c_void_p),
        ("dwNumberOfProcessors", ctypes.wintypes.DWORD),
        ("dwProcessorType", ctypes.wintypes.DWORD),
        ("dwAllocationGranularity", ctypes.wintypes.DWORD),
        ("wProcessorLevel", ctypes.wintypes.WORD),
        ("wProcessorRevision", ctypes.wintypes.WORD),
    ]


# The structure changes according to the Python version (64 or 32 bits).
MEMORY_BASIC_INFORMATION = MemoryBasicInformation64 if ctypes.sizeof(ctypes.c_void_p) == 8 \
    else MemoryBasicInformation


class ModuleInfo(ctypes.Structure):
    """
    Represents information about a module in a process.
    _fields:
        lpBaseOfDll: The base address of the module.
        SizeOfImage: The size of the module's image.
        EntryPoint: The entry point address of the module.
    """
    _fields_ = [
        ("lpBaseOfDll", ctypes.c_void_p),
        ("SizeOfImage", ctypes.c_ulong),
        ("EntryPoint", ctypes.c_void_p),
    ]


# ! /usr/bin/env python
class ComplexApiController:
    """
        Class for controlling and manipulating Windows processes and memory.

        This class provides various methods for reading and writing memory in Windows processes, as well as querying
        information about loaded modules.

        Attributes:
            _returned_v: A queue for storing the returned values from decorated methods.
    """
    _returned_v = Queue()

    def __init__(self):
        """
        Initialize a new instance of the SearchAndRead class.
        This constructor does not take any parameters.
        """
        ...

    def reset_queue(self) -> None:
        """
        Reset the internal queue used to store returned values.
        """

        self._returned_v.queue.clear()

    def get_readers_values(self) -> list:
        """
        Get the values stored in the internal queue.

        Returns:
            A list of values stored in the internal queue.
        """

        return self._returned_v.get()

    @staticmethod
    def write_lib_offsets(handle, base_address: str, offset: str, buf: any,
                          string: bool = False) -> bool:
        """
           Write data to a specified memory location in a Windows process.
           Args:
               handle: The handle to the target process.
               base_address: The base address where the data should be written.
               offset: The offset from the base address where the data should be written.
               buf: The data to be written.
               string: Whether the data is a string (default is False).
           Returns:
               True if the write operation was successful, False otherwise.
        """

        write_address = int(base_address, 16) + int(offset, 16)

        try:
            if string:
                lp_buffer = ctypes.byref(buf)
                n_size = ctypes.sizeof(buf)
                lp_number_of_bytes_written = ctypes.c_size_t()
                ctypes.windll.kernel32.WriteProcessMemory(handle, write_address, lp_buffer,
                                                          n_size, lp_number_of_bytes_written)
                return True
            else:
                lp_buffer = ctypes.byref(buf)
                n_size = ctypes.sizeof(buf)
                lp_number_of_bytes_written = ctypes.c_ulong(0)
                ctypes.windll.kernel32.WriteProcessMemory(handle, ctypes.c_void_p(write_address), lp_buffer,
                                                          n_size, lp_number_of_bytes_written)
                return True
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)

            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)

    @staticmethod
    def read_lib_offsets(handle, base_address: str, offset: str, buf: any, string: bool = False,
                         utf_16: bool = False) -> any:
        """
        Read data from a specified memory location in a Windows process.

        Args:
            handle: The handle to the target process.
            base_address: The base address from where the data should be read.
            offset: The offset from the base address where the data should be read.
            buf: A buffer to store the read data.
            string: Whether the data to be read is a string (default is False).
            utf_16: Whether to interpret the data as UTF-16 (default is False).

        Returns:
            The read data.
        """

        read_address = int(base_address, 16) + int(offset, 16)
        try:
            if string:
                lp_number_of_bytes_read = ctypes.c_ulong(0)
                ctypes.windll.kernel32.ReadProcessMemory(handle, read_address, buf, ctypes.sizeof(buf),
                                                         lp_number_of_bytes_read)
                buffer_array = bytearray(buf)
                found_terminator = buffer_array.find(b'\x00')
                if found_terminator != -1:
                    if utf_16:
                        return buffer_array[:found_terminator].decode("utf-16")  # need to be decoded
                    return buffer_array[:found_terminator].decode("utf-8")  # need to be decoded
                return None
            else:
                lp_buffer = ctypes.byref(buf)
                n_size = ctypes.sizeof(buf)
                lp_number_of_bytes_read = ctypes.c_ulong(0)
                ctypes.windll.kernel32.ReadProcessMemory(handle, ctypes.c_void_p(read_address), lp_buffer, n_size,
                                                         lp_number_of_bytes_read)
                return buf.value
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)

            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)

    def address_refiners(self, handle, list_address: list, buf: any, changed_value: any, string: bool = False,
                         utf_16: bool = False) -> list:
        """
        Refine a list of memory addresses based on their content.

        Args:
            handle: The handle to the target process.
            list_address: A list of memory addresses to be refined.
            buf: A buffer to use for reading memory.
            changed_value: The value to compare against for refinement.
            string: Whether the data to be read is a string (default is False).
            utf_16: Whether to interpret the data as UTF-16 (default is False).

        Returns:
            A list of refined memory addresses.
        """

        refined_address = []
        for address in list_address:
            read_value = self.read_lib_offsets(handle=handle, base_address=address, offset='0x0', buf=buf,
                                               string=string, utf_16=utf_16)
            if read_value == changed_value:
                refined_address.append(address)
        return refined_address

    def get_base_address(self, handle):
        """
           Get the base address of the main module of a Windows process.

           Args:
               handle: The handle to the target process.

           Returns:
               The base address of the main module.
       """

        return self.get_modules(handle=handle)[0]

    def get_last_address(self, handle):
        """
        Get the last loaded module's address in a Windows process.
        Args:
            handle: The handle to the target process.
        Returns:
            The address of the last loaded module.
        """

        modules = self.get_modules(handle=handle)
        if modules:
            return modules[-1]
        else:
            return None

    @staticmethod
    def get_memory_regions(handle: int):
        system_information = SystemInfo()
        ctypes.windll.kernel32.GetSystemInfo(ctypes.byref(system_information))
        mem_region_begin = system_information.lpMinimumApplicationAddress
        mem_region_end = system_information.lpMaximumApplicationAddress
        current_address = mem_region_begin
        while current_address < mem_region_end:
            region = MEMORY_BASIC_INFORMATION()
            ctypes.windll.kernel32.VirtualQueryEx(handle, ctypes.c_void_p(current_address),
                                                  ctypes.byref(region), ctypes.sizeof(region))
            yield {"address": current_address, "size": region.RegionSize, "struct": region}
            current_address += region.RegionSize

    def search_and_read_in_memory(self, handle, buf: any) -> tuple[list[str], int]:
        founded_addresses = []
        total_values_found = 0
        try:
            buff_length = ctypes.sizeof(buf)
            target_value_bytes = ctypes.cast(ctypes.byref(buf), ctypes.POINTER(ctypes.c_byte * buff_length))
            target_value_bytes = int.from_bytes(bytes(target_value_bytes.contents), byteorder)
            regions = list()
            memory_total = 0
            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                memory_total += region["size"]
                regions.append(region)

            checked_memory_size = 0
            for region in regions:
                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                for index in range(size - buff_length):
                    data = region_data[index: index + buff_length]
                    data = int.from_bytes(bytes((ctypes.c_byte * buff_length)(*data)), byteorder)
                    if data != target_value_bytes:
                        continue
                    found_address = address + index
                    founded_addresses.append(hex(found_address))
                    total_values_found += 1
                checked_memory_size += size
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return founded_addresses, total_values_found

    def find_and_replace_hex_pattern_in_memory(self, handle, search_pattern: str, replacement_pattern: str) -> int:
        """
        Finds and replaces the specified hexadecimal pattern in the memory using regular expressions.

        Args:
            handle: The process handle.
            search_pattern: The hexadecimal pattern to search for (e.g., "A1 2B ?C ?D").
            replacement_pattern: The hexadecimal pattern to replace with.

        Returns:
            The total number of replacements made.
        """
        total_replacements = 0
        try:
            search_pattern = f"\\b{search_pattern}\\b"  # Ensure whole word matching

            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                memory_bytes = bytearray(region_data.raw)
                hex_memory = memory_bytes.hex()

                # Find matches using regular expressions
                matches = re.finditer(search_pattern, hex_memory)

                for match in matches:
                    offset = match.start() // 2
                    start_offset = address + offset
                    end_offset = start_offset + len(search_pattern) // 2

                    # Replace the matched bytes with the replacement pattern
                    replacement_bytes = bytes.fromhex(replacement_pattern)
                    memory_bytes[start_offset - address:end_offset - address] = replacement_bytes
                    total_replacements += 1

                # Write the modified memory back
                ctypes.windll.kernel32.WriteProcessMemory(handle,
                                                          ctypes.c_void_p(address),
                                                          ctypes.c_char_p(memory_bytes), size, None)

        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)

        return total_replacements

    @store_in_queue
    def speed_find_and_replace_hex_pattern_in_memory(self, handle, search_pattern: str, replacement_pattern: str) -> int:
        """
        Finds and replaces the specified hexadecimal pattern in the memory using regular expressions.

        Args:
            handle: The process handle.
            search_pattern: The hexadecimal pattern to search for (e.g., "A1 2B ?C ?D").
            replacement_pattern: The hexadecimal pattern to replace with.

        Returns:
            The total number of replacements made.
        """
        total_replacements = 0
        try:
            search_pattern = f"\\b{search_pattern}\\b"  # Ensure whole word matching

            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                memory_bytes = bytearray(region_data.raw)
                hex_memory = memory_bytes.hex()

                # Find matches using regular expressions
                matches = re.finditer(search_pattern, hex_memory)

                for match in matches:
                    offset = match.start() // 2
                    start_offset = address + offset
                    end_offset = start_offset + len(search_pattern) // 2

                    # Replace the matched bytes with the replacement pattern
                    replacement_bytes = bytes.fromhex(replacement_pattern)
                    memory_bytes[start_offset - address:end_offset - address] = replacement_bytes
                    total_replacements += 1

                # Write the modified memory back
                ctypes.windll.kernel32.WriteProcessMemory(handle,
                                                          ctypes.c_void_p(address),
                                                          ctypes.c_char_p(memory_bytes), size, None)

        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)

        return total_replacements

    def find_hex_pattern_in_memory(self, handle, search_pattern: str) -> tuple:
        """
        Finds the specified hexadecimal pattern in the memory using regular expressions.

        Args:
            handle: The process handle.
            search_pattern: The hexadecimal pattern to search for (e.g., "A1 2B ?C ?D").

        Returns:
            A list of addresses where the pattern was found.
        """
        founded_addresses = []
        total_founded_values = 0
        try:
            pattern = f"{search_pattern}"  # Ensure whole word matching as a whole

            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                memory_bytes = bytes(region_data)
                matches = re.finditer(pattern, memory_bytes.hex())
                for match in matches:
                    offset = match.start() // 2
                    found_address = address + offset
                    founded_addresses.append(hex(found_address))
                    total_founded_values += 1

        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return founded_addresses, total_founded_values

    @store_in_queue
    def speed_find_hex_pattern_in_memory(self, handle, search_pattern: str) -> tuple:
        """
        Finds the specified hexadecimal pattern in the memory using regular expressions.

        Args:
            handle: The process handle.
            search_pattern: The hexadecimal pattern to search for (e.g., "A1 2B ?C ?D").

        Returns:
            A list of addresses where the pattern was found.
        """
        founded_addresses = []
        total_founded_values = 0
        try:
            pattern = f"\\b{search_pattern}\\b"  # Ensure whole word matching as a whole

            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                memory_bytes = bytes(region_data.raw)
                matches = re.finditer(pattern, memory_bytes.hex())
                for match in matches:
                    offset = match.start() // 2
                    found_address = address + offset
                    founded_addresses.append(hex(found_address))
                    total_founded_values += 1

        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return founded_addresses, total_founded_values

    def group_search_and_read(self, handle, buf: list, range_val: int) -> tuple[list[str], int]:
        founded_addresses = []
        total_values_found = 0
        try:
            buff_length = ctypes.sizeof(buf[0])  # same buffer length (DWORD-4)
            target_bytes = [ctypes.cast(ctypes.byref(buffer), ctypes.POINTER(ctypes.c_byte * buff_length))
                            for buffer in buf]
            target_value_bytes = [int.from_bytes(bytes(t_byte.contents), byteorder) for t_byte in target_bytes] # list
            regions = list()
            memory_total = 0
            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                memory_total += region["size"]
                regions.append(region)

            checked_memory_size = 0
            for region in regions:
                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                found_indexes = []
                for index in range(size - buff_length):
                    data = region_data[index: index + buff_length]
                    data = int.from_bytes(bytes((ctypes.c_byte * buff_length)(*data)), byteorder)
                    if data in target_value_bytes:
                        found_indexes.append(address + index)

                for ranged_index in range(len(found_indexes) - 1):
                    if found_indexes[ranged_index + 1] - found_indexes[ranged_index] <= range_val * buff_length:
                        founded_addresses.append(hex(found_indexes[ranged_index]))
                        total_values_found += 1
                checked_memory_size += size
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return founded_addresses, total_values_found

    @store_in_queue
    def speed_group_search_and_read(self, handle, buf: any, range_val: int) -> tuple[list[str], int]:
        founded_addresses = []
        total_values_found = 0
        try:
            buff_length = ctypes.sizeof(buf[0])  # same buffer length (DWORD-4)
            target_bytes = [ctypes.cast(ctypes.byref(buffer), ctypes.POINTER(ctypes.c_byte * buff_length))
                            for buffer in buf]
            target_value_bytes = [int.from_bytes(bytes(t_byte.contents), byteorder) for t_byte in target_bytes]  # list
            regions = list()
            memory_total = 0
            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                memory_total += region["size"]
                regions.append(region)

            checked_memory_size = 0
            for region in regions:
                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                found_indexes = []
                for index in range(size - buff_length):
                    data = region_data[index: index + buff_length]
                    data = int.from_bytes(bytes((ctypes.c_byte * buff_length)(*data)), byteorder)
                    if data in target_value_bytes:
                        found_indexes.append(address + index)

                for ranged_index in range(len(found_indexes) - 1):
                    if found_indexes[ranged_index + 1] - found_indexes[ranged_index] <= range_val * buff_length:
                        founded_addresses.append(hex(found_indexes[ranged_index]))
                        total_values_found += 1
                checked_memory_size += size
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return founded_addresses, total_values_found

    def search_and_write_in_memory(self, handle, read_buf: any, write_buff: any,
                                   string: bool = False) -> int:

        """
        Search for a value in the memory of a Windows process and replace matching values.
        Args:
            handle: The handle to the target process.
            read_buf: A buffer to use for reading memory.
            write_buff: The data to write in place of the matched value.
            string: Whether the data to be read is a string (default is False).
        Returns:
            The total number of values replaced.
        """
        total_values_replaced = 0
        try:
            buff_length = ctypes.sizeof(read_buf)
            target_value_bytes = ctypes.cast(ctypes.byref(read_buf), ctypes.POINTER(ctypes.c_byte * buff_length))
            target_value_bytes = int.from_bytes(bytes(target_value_bytes.contents), byteorder)
            regions = list()
            memory_total = 0
            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                memory_total += region["size"]
                regions.append(region)

            checked_memory_size = 0
            for region in regions:
                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                for index in range(size - buff_length):
                    data = region_data[index: index + buff_length]
                    data = int.from_bytes(bytes((ctypes.c_byte * buff_length)(*data)), byteorder)
                    if data != target_value_bytes:
                        continue
                    found_address = address + index
                    self.write_lib_offsets(handle=handle,
                                           base_address=hex(found_address), offset='0x0', string=string,
                                           buf=write_buff)
                    total_values_replaced += 1
                checked_memory_size += size
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return total_values_replaced

    def group_search_and_write(self, handle, read_buf: any, write_buff: any,
                               range_val: int, string: bool = False) -> int:

        """
        Search for a value in the memory of a Windows process and replace matching values in specific range.
        Args:
            handle: The handle to the target process.
            read_buf: A buffer to use for reading memory.
            write_buff: The data to write in place of the matched value.
            string: Whether the data to be read is a string (default is False).
        Returns:
            The total number of values replaced.
        """
        total_values_replaced = 0
        try:
            buff_length = ctypes.sizeof(read_buf[0])  # same buffer length (DWORD-4)
            target_bytes = [ctypes.cast(ctypes.byref(buffer), ctypes.POINTER(ctypes.c_byte * buff_length))
                            for buffer in read_buf]
            target_value_bytes = [int.from_bytes(bytes(t_byte.contents), byteorder) for t_byte in target_bytes]  # list
            regions = list()
            memory_total = 0
            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                memory_total += region["size"]
                regions.append(region)

            checked_memory_size = 0
            for region in regions:
                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                found_indexes = []
                for index in range(size - buff_length):
                    data = region_data[index: index + buff_length]
                    data = int.from_bytes(bytes((ctypes.c_byte * buff_length)(*data)), byteorder)
                    if data in target_value_bytes:
                        found_indexes.append(address + index)

                for ranged_index in range(len(found_indexes) - 1):
                    if found_indexes[ranged_index + 1] - found_indexes[ranged_index] <= range_val * buff_length:
                        self.write_lib_offsets(handle=handle,
                                               base_address=hex(found_indexes[ranged_index]), offset='0x0',
                                               string=string, buf=write_buff)
                        total_values_replaced += 1
                checked_memory_size += size
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return total_values_replaced

    @store_in_queue
    def speed_group_search_and_write(self, handle, read_buf: any, write_buff: any,
                                     range_val: int, string: bool = False) -> int:

        """
        Search for a value in the memory of a Windows process and replace matching values in specific range.
        Args:
            handle: The handle to the target process.
            read_buf: A buffer to use for reading memory.
            write_buff: The data to write in place of the matched value.
            string: Whether the data to be read is a string (default is False).
        Returns:
            The total number of values replaced.
        """
        total_values_replaced = 0
        try:
            buff_length = ctypes.sizeof(read_buf[0])  # same buffer length (DWORD-4)
            target_bytes = [ctypes.cast(ctypes.byref(buffer), ctypes.POINTER(ctypes.c_byte * buff_length))
                            for buffer in read_buf]
            target_value_bytes = [int.from_bytes(bytes(t_byte.contents), byteorder) for t_byte in target_bytes]  # list
            regions = list()
            memory_total = 0
            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                memory_total += region["size"]
                regions.append(region)

            checked_memory_size = 0
            for region in regions:
                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                found_indexes = []
                for index in range(size - buff_length):
                    data = region_data[index: index + buff_length]
                    data = int.from_bytes(bytes((ctypes.c_byte * buff_length)(*data)), byteorder)
                    if data in target_value_bytes:
                        found_indexes.append(address + index)

                for ranged_index in range(len(found_indexes) - 1):
                    if found_indexes[ranged_index + 1] - found_indexes[ranged_index] <= range_val * buff_length:
                        self.write_lib_offsets(handle=handle,
                                               base_address=hex(found_indexes[ranged_index]), offset='0x0',
                                               string=string, buf=write_buff)
                        total_values_replaced += 1
                checked_memory_size += size
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return total_values_replaced

    @store_in_queue
    def speed_search_and_read_in_memory(self, handle, buf: any) -> tuple[list[str], int]:
        """
        A decorator-enhanced version of search_and_read_in_memory that stores the result in a queue.

        Args:
            handle: The handle to the target process.
            buf: A buffer to use for reading memory.
        Returns:
            A tuple containing a list of found addresses and the total number of values found.
        """

        founded_addresses = []
        total_values_found = 0
        try:
            buff_length = ctypes.sizeof(buf)
            target_value_bytes = ctypes.cast(ctypes.byref(buf), ctypes.POINTER(ctypes.c_byte * buff_length))
            target_value_bytes = int.from_bytes(bytes(target_value_bytes.contents), byteorder)
            regions = list()
            memory_total = 0
            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                memory_total += region["size"]
                regions.append(region)

            checked_memory_size = 0
            for region in regions:
                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                for index in range(size - buff_length):
                    data = region_data[index: index + buff_length]
                    data = int.from_bytes(bytes((ctypes.c_byte * buff_length)(*data)), byteorder)
                    if data != target_value_bytes:
                        continue
                    found_address = address + index
                    founded_addresses.append(hex(found_address))
                    total_values_found += 1
                checked_memory_size += size
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return founded_addresses, total_values_found

    @store_in_queue
    def speed_search_and_write_in_memory(self, handle, read_buf: any, write_buff: any,
                                         string: bool = False) -> int:
        """
        A decorator-enhanced version of search_and_write_in_memory that stores the result in a queue.

        Args:
            handle: The handle to the target process.
            read_buf: A buffer to use for reading memory.
            write_buff: The data to write in place of the matched value.
            string: Whether the data to be read is a string (default is False).
        Returns:
            The total number of values replaced.
        """

        total_values_replaced = 0
        try:
            buff_length = ctypes.sizeof(read_buf)
            target_value_bytes = ctypes.cast(ctypes.byref(read_buf), ctypes.POINTER(ctypes.c_byte * buff_length))
            target_value_bytes = int.from_bytes(bytes(target_value_bytes.contents), byteorder)
            regions = list()
            memory_total = 0
            for region in self.get_memory_regions(handle=handle):
                if region["struct"].State != MemoryAllocationStatesEnum.MEM_COMMIT.value:
                    continue
                if region["struct"].Type != MemoryTypesEnum.MEM_PRIVATE.value:
                    continue
                if region["struct"].Protect & MemoryProtectionsEnum.PAGE_READABLE.value == 0:
                    continue

                memory_total += region["size"]
                regions.append(region)

            checked_memory_size = 0
            for region in regions:
                address, size = region["address"], region["size"]
                region_data = (ctypes.c_byte * size)()
                ctypes.windll.kernel32.ReadProcessMemory(handle,
                                                         ctypes.c_void_p(address),
                                                         ctypes.byref(region_data), size, None)
                for index in range(size - buff_length):
                    data = region_data[index: index + buff_length]
                    data = int.from_bytes(bytes((ctypes.c_byte * buff_length)(*data)), byteorder)
                    if data != target_value_bytes:
                        continue
                    found_address = address + index
                    self.write_lib_offsets(handle=handle,
                                           base_address=hex(found_address), offset='0x0', string=string,
                                           buf=write_buff)
                    total_values_replaced += 1
                checked_memory_size += size
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
        return total_values_replaced

    @staticmethod
    def get_modules(handle) -> list[int]:
        """
        Get a list of module addresses loaded in a Windows process.
        Args:
            handle: The handle to the target process.
        Returns:
            A list of module addresses.
        """

        modules = (ctypes.wintypes.HMODULE * MAX_PATH)()
        ctypes.windll.psapi.EnumProcessModules(handle, modules, ctypes.sizeof(modules), None)
        return [x for x in tuple(modules) if x is not None]

    # Example: ntdll.dll
    def find_dll_addresses(self, handle, dll_name: str) -> tuple[str, str]:
        """
        Find the base and ending addresses of a DLL module in a Windows process.
        Args:
            handle: The handle to the target process.
            dll_name: The name of the DLL to search for.
        Returns:
            A tuple containing the base and ending addresses of the DLL module.
        """

        try:
            modules = self.get_modules(handle=handle)
            for module_base in modules:
                module_name = ctypes.create_string_buffer(MAX_PATH)
                ctypes.windll.psapi.GetModuleFileNameExA(handle, ctypes.c_void_p(module_base), module_name,
                                                         MAX_PATH)
                module_name_str = module_name.value.decode('utf-8')
                if dll_name.lower() in module_name_str.lower():
                    module_info = ModuleInfo()
                    ctypes.windll.psapi.GetModuleInformation(handle, ctypes.c_void_p(module_base),
                                                             ctypes.byref(module_info), ctypes.sizeof(module_info))
                    base_address = module_info.lpBaseOfDll
                    ending_address = base_address + module_info.SizeOfImage
                    return str(hex(base_address)), str(hex(ending_address))

            return "0x0", "0x0"  # Return (0, 0) if DLL not found
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)

            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)

    def get_dll_address(self, handle):
        """
        Get the addresses of all DLL modules loaded in a Windows process.

        Args:
            handle: The handle to the target process.

        Returns:
            A list of address ranges for loaded DLL modules.
        """

        try:
            modules = self.get_modules(handle=handle)
            dlls = []
            for module_base in modules:
                module_name = ctypes.create_string_buffer(MAX_PATH)
                ctypes.windll.psapi.GetModuleFileNameExA(handle, ctypes.c_void_p(module_base), module_name,
                                                         MAX_PATH)
                module_info = ModuleInfo()
                ctypes.windll.psapi.GetModuleInformation(handle, ctypes.c_void_p(module_base),
                                                         ctypes.byref(module_info), ctypes.sizeof(module_info))
                base_address = module_info.lpBaseOfDll
                ending_address = base_address + module_info.SizeOfImage
                dlls.append(f'{base_address}-{ending_address}')

            return dlls
        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)

            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)

    def raw_dumper(self, handle, dll_name: str) -> tuple:
        """
        Dump the raw memory content of a DLL module in a Windows process.

        Args:
            handle: The handle to the target process.
            dll_name: The name of the DLL to dump.

        Returns:
            A tuple containing the dumped memory data and the base and ending addresses of the DLL module.
        """

        address = self.find_dll_addresses(handle=handle, dll_name=dll_name)
        start_addr = int(address[0], 16)
        end_addr = int(address[1], 16)
        if start_addr == 0 or end_addr == 0:
            raise WINAPIException(f"Could not able to retrieve address for {dll_name} check for spellings.")
        try:
            size = end_addr - start_addr
            read_buffer = ctypes.create_string_buffer(size)
            lp_number_of_bytes_read = ctypes.c_ulong(0)
            ctypes.windll.kernel32.ReadProcessMemory(handle, ctypes.c_void_p(start_addr),
                                                     read_buffer, size, lp_number_of_bytes_read)
            memory_data = read_buffer.raw
            return memory_data, address

        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)
            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)

    def get_memory_mappings(self, handle):
        """
        Get a list of memory mappings in a Windows process.
        Args:
            handle: The handle to the target process.
        Returns:
            A list of memory mapping information.
        """

        try:
            memory_mappings = []

            modules = self.get_modules(handle=handle)
            for module_base in modules:
                module_info = ModuleInfo()
                ctypes.windll.psapi.GetModuleInformation(handle, ctypes.c_void_p(module_base),
                                                         ctypes.byref(module_info), ctypes.sizeof(module_info))

                base_address = module_info.lpBaseOfDll
                ending_address = base_address + module_info.SizeOfImage
                size_of_image = module_info.SizeOfImage
                module_name = ctypes.create_string_buffer(MAX_PATH)
                ctypes.windll.psapi.GetModuleFileNameExA(handle, ctypes.c_void_p(module_base), module_name, MAX_PATH)
                module_name_str = module_name.value.decode('utf-8')

                memory_mapping = {
                    "BaseAddress": hex(base_address),
                    "EndingAddress": hex(ending_address),
                    "SizeOfImage": size_of_image,
                    "ModuleName": module_name_str,
                }

                memory_mappings.append(memory_mapping)

            return memory_mappings

        except (BufferError, ValueError, TypeError) as error:
            if handle:
                ctypes.windll.kernel32.CloseHandle(handle)

            error_code = ctypes.windll.kernel32.GetLastError()
            error = {'msg': str(error), 'Handle': handle, 'ErrorCode': error_code}
            raise WINAPIException(error)
