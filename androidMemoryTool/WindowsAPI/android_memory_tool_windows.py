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

# RES: https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-readprocessmemory?redirectedfrom=MSDN

# ! /usr/bin/env python
from .ThreadingController import FastSearchAlgo
from .DataClasses import DataClasses
from ..errors_class import WINAPIException, PIDException
from os import cpu_count
import ctypes

# Process Permissions
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_OPERATION = 0x0008
PROCESS_ALL_ACCESS = 0x1f0fff
PROCESS_VM_WRITE = 0x0020
PROCESS_VM_READ = 0x0010
MAX_PATH = 260


class AndroidMemoryToolWindows(FastSearchAlgo):
    """
    AndroidMemoryToolWindows is a class for interacting with the memory of Android processes on Windows.

    Args:
        PKG (Union[str, int]): The package name or process ID of the Android application.
        TYPE (str, optional): The data type to use when reading and writing memory. Defaults to "DWORD".
        SPEED_MODE (bool, optional): If True, use a fast search algorithm; if False, use a slower but more
                                     precise method. Defaults to True.
        WORKERS (int, optional): The number of worker threads to use for memory operations. Defaults to half of the
                                 available CPU cores.

    Attributes:
        _pid (int): The process ID of the Android application.
        _handle (int): The handle to the process.
        _string_data_types (list): List of supported string data types.
        _speed_mode (bool): Flag indicating whether to use fast search algorithms.
        _data_type (str): The data type to use for memory operations.
        _search_and_read (SearchAndRead): An instance of the SearchAndRead class for memory operations.

    Methods:
        _get_process_by_id(self):
            Private method to obtain a handle to the Android process based on its process ID.

        _open_handle(self):
            Private method to open a handle to the Android process with specific access rights.

        _open_handler_on_all_access(self):
            Private method to open a handle to the Android process with full access.

        _close_handle(self) -> int:
            Private method to close the handle to the Android process and return the last error code.

        read_value(self, read: Any, is_grouped: bool = False, range_val: int = 512) -> Any:
            Read a value from the Android process's memory.

        read_write_value(self, read: Any, write: Any, is_grouped: bool = False, range_val: int = 512) -> Any:
            Read and write a value in the Android process's memory.

        write_lib(self, base_address: str, offset: str, write_value: Any) -> bool:
            Write a value to a specified memory address within a loaded library in the Android process.

        read_lib(self, base_address: str, offset: str, value: Union[str, int, None] = None) -> Any:
            Read a value from a specified memory address within a loaded library in the Android process.

        refiner_address(self, list_address: List[int], value_to_refine: Any) -> Any:
            Refine a list of memory addresses based on a specified value.

        get_module_base_address(self, module_name: str) -> Any:
            Get the base address of a loaded module (DLL) in the Android process's memory.

        raw_dump(self, lib_name: str, path: str = './') -> bool:
            Dump the memory of a specified loaded library in the Android process to a binary file.

        find_hex_pattern(search_pattern: str) -> Any:
            [Not implemented in this version] Find a hexadecimal pattern in the Android process's memory.

        find_and_replace_hex_pattern(search_pattern: str, replace_pattern: str) -> Any:
            [Not implemented in this version] Find and replace a hexadecimal pattern in the Android process's memory.

        dump_maps(self, path: str = "./") -> bool:
            Dump the memory maps (address ranges) of the Android process to a text file.
    """

    def __init__(self,
                 PKG: any((str, int)),
                 TYPE: str = DataClasses.DataTypes.DWORD,
                 SPEED_MODE: bool = True,
                 WORKERS: int = int(cpu_count() / 2),  # half of cores available in operating system
                 ) -> None:
        """
        Initializes an instance of AndroidMemoryToolWindows.

        Args:
            PKG (str or int): The package name or process ID of the Android application.
            TYPE (str, optional): The data type to use for memory operations (default is DataClasses.DataTypes.DWORD).
            SPEED_MODE (bool, optional): Whether to use speed optimization mode (default is True).
            WORKERS (int, optional): Number of worker threads to use for memory operations
                                     (default is half of CPU cores).
        """

        super(AndroidMemoryToolWindows, self).__init__(workers=WORKERS)
        self._pid = DataClasses.get_pid(pkg=PKG)
        self._handle = self._get_process_by_id()
        self._close_handle()
        self._string_data_types = [DataClasses.DataTypes.UTF_8, DataClasses.DataTypes.UTF_16LE]
        self._speed_mode = SPEED_MODE
        self._data_type = TYPE

    def _get_process_by_id(self):
        """
        Get the handle of the Android application's process by its process ID.
        Returns:
            int: The process handle.
        Raises:
            PIDException: If the process with the specified PID is not found.
        """

        handle = ctypes.windll.kernel32.OpenProcess(PROCESS_QUERY_INFORMATION, False, self._pid)
        if handle:
            image_file_name = (ctypes.c_char * MAX_PATH)()
            if ctypes.windll.psapi.GetProcessImageFileNameA(handle, image_file_name, MAX_PATH) > 0:
                return handle
            else:
                raise PIDException(f'Unable to get the executable\'s name for PID={self._pid}!')

        raise PIDException(f'Process "{self._pid}" not found!')

    def _open_handle(self):
        """
        Open the process handle with specific access rights.

        Raises:
            WINAPIException: If unable to open the process handle.
        """

        dw_desired_access = (PROCESS_QUERY_INFORMATION | PROCESS_VM_OPERATION | PROCESS_VM_READ | PROCESS_VM_WRITE)
        b_inherit_handle = True
        self._handle = ctypes.windll.kernel32.OpenProcess(dw_desired_access, b_inherit_handle, self._pid)
        if not self._handle:
            raise WINAPIException(f'Unable to open process')

    def _open_handler_on_all_access(self):
        """
        Open the process handle with all access rights.

        Raises:
            WINAPIException: If unable to open the process handle.
        """
        b_inherit_handle = True
        self._handle = ctypes.windll.kernel32.OpenProcess(PROCESS_ALL_ACCESS, b_inherit_handle, self._pid)
        if not self._handle:
            raise WINAPIException(f'Unable to open process')

    def _close_handle(self) -> int:
        """
        Close the process handle.

        Returns:
            int: The error code if the handle cannot be closed.
        """

        ctypes.windll.kernel32.CloseHandle(self._handle)
        return ctypes.windll.kernel32.GetLastError()

    def read_value(self, read: any, is_grouped: bool = False, range_val: int = 512) -> any:
        """
        Read a value from the memory of the Android application.

        Args:
            read: The value to read from memory.
            is_grouped (bool, optional): Whether the read operation is grouped (default is False).
            range_val (int, optional): The range of memory to search for the value (default is 512).

        Returns:
            any: The read value.
        """
        self._open_handler_on_all_access()
        if not is_grouped:
            data_types = DataClasses.data_type_buffer(data_type=self._data_type, read_value=read)
        else:
            data_types = [DataClasses.data_type_buffer(data_type=self._data_type, read_value=val) for val in read]
        # If data type is valid continue
        if not is_grouped:
            # Handle both string and on ASCII chars
            if self._speed_mode:
                super().fast_search_algorithms_value(handle=self._handle, buf=data_types)
                r_value = self.main_controller.get_readers_values()
                self.main_controller.reset_queue()
                self._close_handle()
                return r_value
            r_value = self.main_controller.search_and_read_in_memory(handle=self._handle, buf=data_types)
            self._close_handle()
            return r_value
        elif is_grouped and self._data_type:
            if self._speed_mode:
                # FIXME: Bug-Threads are not terminating and runnning forever.
                super().fast_search_algorithms_group_values(handle=self._handle, buf=data_types, range_val=range_val)
                r_value = self.main_controller.get_readers_values()
                self.main_controller.reset_queue()
                self._close_handle()
                return r_value
            r_value = self.main_controller.group_search_and_read(handle=self._handle, buf=data_types,
                                                                 range_val=range_val)
            self._close_handle()
            return r_value

        return None

    def read_write_value(self, read: any, write: any, is_grouped: bool = False, range_val: int = 512) -> any:
        """
        Read and write a value to the memory of the Android application.

        Args:
            read: The value to read from memory.
            write: The value to write to memory.
            is_grouped (bool, optional): Whether the read and write operations are grouped (default is False).
            range_val (int, optional): The range of memory to search for the value (default is 512).

        Returns:
            any: The read value.
        """

        self._open_handler_on_all_access()
        read_buffer, write_buffer = DataClasses.data_type_buffer(data_type=self._data_type, read_value=read,
                                                                 write=write, read_string=read, write_string=write)
        # If data type is valid continue
        if self._data_type not in self._string_data_types and not is_grouped:
            if self._speed_mode:
                super().fast_search_algorithms_value(handle=self._handle, buf=read_buffer, write_buf=write_buffer)
                r_value = self.main_controller.get_readers_values()
                self.main_controller.reset_queue()
                self._close_handle()
                return r_value
            r_value = self.main_controller.search_and_write_in_memory(handle=self._handle, read_buf=read_buffer,
                                                                      write_buff=write_buffer)
            self._close_handle()
            return r_value

        elif is_grouped and self._data_type:
            if self._speed_mode:
                if self._data_type in self._string_data_types:
                    super().fast_search_algorithms_group_values(handle=self._handle,
                                                                buf=read_buffer, range_val=range_val,
                                                                write_buf=write_buffer, string=True)
                else:
                    super().fast_search_algorithms_group_values(handle=self._handle,
                                                                buf=read_buffer, range_val=range_val,
                                                                write_buf=write_buffer)

                r_value = self.main_controller.get_readers_values()
                self.main_controller.reset_queue()
                self._close_handle()
                return r_value
            if self._data_type in self._string_data_types:
                r_value = self.main_controller.group_search_and_write(handle=self._handle,
                                                                      read_buf=read_buffer,
                                                                      write_buff=write_buffer,
                                                                      range_val=range_val, string=True)
            else:
                r_value = self.main_controller.group_search_and_write(handle=self._handle,
                                                                      read_buf=read_buffer,
                                                                      write_buff=write_buffer,
                                                                      range_val=range_val)
            self._close_handle()
            return r_value
        else:
            # string to search
            if self._speed_mode:
                super().fast_search_algorithms_value(handle=self._handle, buf=read_buffer, write_buf=write_buffer,
                                                     string=True)
                r_value = self.main_controller.get_readers_values()
                self.main_controller.reset_queue()
                self._close_handle()
                return r_value
            r_value = self.main_controller.search_and_write_in_memory(handle=self._handle, read_buf=read_buffer,
                                                                      write_buff=write_buffer, string=True)
            self._close_handle()
            return r_value

    def write_lib(self, base_address: str, offset: str, write_value: any) -> bool:
        """
        Write a value to a specified memory location within a loaded library.

        Args:
            base_address (str): The base address of the loaded library.
            offset (str): The offset within the library where the value should be written.
            write_value: The value to write to memory.

        Returns:
            bool: True if the write operation was successful, False otherwise.
        """

        self._open_handle()
        _, write_buf = DataClasses.data_type_buffer(data_type=self._data_type, write=write_value,
                                                    write_string=write_value)
        base_address = str(base_address)
        offset = str(offset)
        is_string = True if self._data_type in self._string_data_types else False
        r_value = self.main_controller.write_lib_offsets(handle=self._handle,
                                                         base_address=base_address, offset=offset, buf=write_buf,
                                                         string=is_string)
        self._close_handle()
        return r_value

    def read_lib(self, base_address: str, offset: str, value: any((str, int, None)) = None) -> any:
        """
        Read a value from a specified memory location within a loaded library.
        Args:
            base_address (str): The base address of the loaded library.
            offset (str): The offset within the library where the value should be read from.
            value (str, int, None, optional): The expected value to compare when reading (default is None).
        Returns:
            any: The read value.
        """

        self._open_handle()
        read_buffer = DataClasses.data_type_buffer(data_type=self._data_type, read_string=value)
        base_address = str(base_address)
        offset = str(offset)
        if self._data_type not in self._string_data_types:
            r_value = self.main_controller.read_lib_offsets(handle=self._handle,
                                                            base_address=base_address,
                                                            offset=offset, buf=read_buffer)
            self._close_handle()
            return r_value
        else:
            is_utf_16 = True if self._data_type == DataClasses.DataTypes.UTF_16LE else False
            length_of_read = len(value)
            r_value = self.main_controller.read_lib_offsets(handle=self._handle,
                                                            base_address=base_address,
                                                            offset=offset, buf=read_buffer, string=True,
                                                            length=length_of_read, utf_16=is_utf_16)
            self._close_handle()
            return r_value

    def refiner_address(self, list_address: list, value_to_refine: any) -> any:
        """
        Refine a list of memory addresses based on a value to match.

        Args:
           list_address (list): List of memory addresses to refine.
           value_to_refine: The value to refine the addresses.

        Returns:
           any: The refined list of memory addresses.
        """

        self._open_handle()
        read_buffer = DataClasses.data_type_buffer(data_type=self._data_type, read_string=value_to_refine)
        if self._data_type not in self._string_data_types:
            r_value = self.main_controller.address_refiners(handle=self._handle,
                                                            list_address=list_address, buf=read_buffer,
                                                            changed_value=value_to_refine)
            self._close_handle()
            return r_value
        else:
            is_utf_16 = True if self._data_type == DataClasses.DataTypes.UTF_16LE else False
            length_of_read = len(value_to_refine)
            r_value = self.main_controller.address_refiners(handle=self._handle,
                                                            list_address=list_address, buf=read_buffer,
                                                            changed_value=value_to_refine, string=True,
                                                            length=length_of_read, utf_16=is_utf_16)
            self._close_handle()
            return r_value

    def get_module_base_address(self, module_name: str) -> any:
        """
        Get the base address of a loaded module (DLL) by its name.

        Args:
            module_name (str): The name of the loaded module.

        Returns:
            any: The base address of the module.
        """

        self._open_handle()
        base_address, _ = self.main_controller.find_dll_addresses(handle=self._handle, dll_name=module_name)
        self._close_handle()
        return base_address

    def raw_dump(self, lib_name: str, path='./') -> bool:
        """
        Dump the memory of a loaded library to a binary file.

        Args:
            lib_name (str): The name of the loaded library to dump.
            path (str, optional): The path where the binary dump file should be saved (default is './').

        Returns:
            bool: True if the dump was successful, False otherwise.
        """
        self._open_handle()
        bytes_of_process, address = self.main_controller.raw_dumper(handle=self._handle, dll_name=lib_name)
        with open(f"{path}{address[0]}-{address[1]}-{lib_name.replace('.dll', '')}.bin", "wb") as byte_file:
            byte_file.write(bytes_of_process)
            byte_file.close()
        self._close_handle()
        return True

    @staticmethod
    def find_hex_pattern(search_pattern: str) -> any:
        """
        Finds the specified hexadecimal pattern in the memory.

        Args:
            search_pattern: The hexadecimal pattern to search for.

        Returns:
            The addresses where the pattern was found.
        """
        print('[DEBUG] This function is not available in current version. Please wait for next update')
        return None

    @staticmethod
    def find_and_replace_hex_pattern(search_pattern: str, replace_pattern: str) -> any:
        """
        Search for and replace a hexadecimal pattern in the memory of the Android application.

        Args:
            search_pattern (str): The hexadecimal pattern to search for.
            replace_pattern (str): The hexadecimal pattern to replace with.

        Returns:
            any: The result of the search
            and replace operation.
        """
        print('[DEBUG] This function is not available in current version. Please wait for next update')
        return None

    def dump_maps(self, path="./") -> bool:
        """
        Dump the memory mappings of the Android application to a text file.

        Args:
            path (str, optional): The path where the text file should be saved (default is './').

        Returns:
            bool: True if the dump was successful, False otherwise.
        """

        self._open_handle()
        memory_maps = self.main_controller.get_memory_mappings(handle=self._handle)
        self._close_handle()
        if memory_maps:
            with open(f"{path}maps.txt", "w") as map_file:
                for memory_map in memory_maps:
                    map_file.write(f"{memory_map['BaseAddress']}-{memory_map['EndingAddress']:<40}"
                                   f"{memory_map['SizeOfImage']:<30}{memory_map['ModuleName']:<70}\n")
                map_file.close()
            return True
        return False
