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

from .WindowsAPI.android_memory_tool_windows import AndroidMemoryToolWindows
from .LinuxAPI.android_memory_tool_linux import AndroidMemoryToolLinux
from .CommonAPI.cross_platform_memory_profiler import MemoryProfiler
from .LinuxAPI.DataClasses import DataClasses
from subprocess import check_output
from dataclasses import dataclass
import platform
import psutil

if platform.system() == 'Windows':
    _WIN_PLATFORM = True
else:
    # Assuming that the platforms are in list[Linux, Android] other platform will give errors.
    _WIN_PLATFORM = False


@dataclass()
class PMAP(DataClasses.PMAP):
    """
    Data class that defines different options for memory mapping.

    Inherited-Attributes:
        ALL (bool, optional): True to search for memory attributes in all regions, False to search in MAIN only.
        B_BAD (bool, optional): True to search for BAD regions in memory.
        C_ALLOC (bool, optional): True to search for C_ALLOC regions in memory.
        C_BSS (bool, optional): True to search for C_BSS regions in memory.
        C_DATA (bool, optional): True to search for C_DATA regions in memory.
        C_HEAP (bool, optional): True to search for C_HEAP regions in memory.
        JAVA_HEAP (bool, optional): True to search for JAVA_HEAP regions in memory.
        A_ANONYMOUS (bool, optional): True to search for A_ANONYMOUS regions in memory.
        CODE_SYSTEM (bool, optional): True to search for CODE_SYSTEM regions in memory.
        STACK (bool, optional): True to search for STACK regions in memory.
        ASHMEM (bool, optional): True to search for ASHMEM regions in memory.
        J_Java (bool, optional): True to search for J_Java regions in memory.
        CODE_APP (bool, optional): True to search for CODE_APP regions in memory.
        V_video (bool, optional): True to search for V_video regions in memory.
    """
    ...


@dataclass()
class DataTypes(DataClasses.DataTypes):
    """
    Data class that defines different data types used in the code.

    Inherited-Attributes:
        DWORD (str): 32-bit data type.
        FLOAT (str): 32-bit floating-point data type.
        DOUBLE (str): 64-bit floating-point data type.
        WORD (str): 16-bit data type.
        BYTE (str): 8-bit data type.
        QWORD (str): 64-bit data type.
        XOR (str): XOR data type.
        UTF_8 (str): UTF-8 character encoding.
        UTF_16LE (str): UTF-16LE character encoding.
    """
    ...


class AndroidMemoryTool(object):
    """
        Android Memory Tool for reading, writing, and analyzing memory of Android applications and processes.

        Attributes:
            VERSION_CODE (float): The version code of the AndroidMemoryTool.
            DEVELOPER (str): The name of the developer of AndroidMemoryTool.
            PLATFORM (str): The platform the script is running on (Linux, Android, Windows).

        Args:
            PKG (str or int): The package name or PID of the target Android application.
            TYPE (str): The data type for memory operations (default is DWORD).
            SPEED_MODE (bool): Enable speed mode for memory operations (default is False).
            WORKERS (int): The number of worker processes for parallel memory operations (default is half of CPU cores).
            pMAP (PMAP): Process Memory Attributes object to specify memory search attributes (default is empty PMAP).

        Raises:
            PIDException: If the specified process is not running in memory.

        Example:
            To initialize AndroidMemoryTool and obtain the Process ID (PID) of a target process:
            ```python
            from androidMemoryTool import AndroidMemoryTool
            tool = AndroidMemoryTool(PKG="ac_client")
            pid = tool.get_pid()
            print(pid)
            ```

    """
    VERSION_CODE = 0.6
    DEVELOPER = "Abdul Moez"
    PLATFORM = platform.system()

    def __init__(self, PKG: any((str, int)),
                 TYPE: str = DataTypes.DWORD,
                 SPEED_MODE: bool = False,
                 WORKERS: int = int(psutil.cpu_count() / 2),  # half of cores available in operating system
                 pMAP: PMAP = PMAP()
                 ) -> None:
        """
        Initialize AndroidMemoryTool with specified parameters.

        Args:
            PKG (str or int): The package name or PID of the target Android application.
            TYPE (str): The data type for memory operations (default is DWORD).
            SPEED_MODE (bool): Enable speed mode for memory operations (default is False).
            WORKERS (int): The number of worker processes for parallel memory operations (default is half of CPU cores).
            pMAP (PMAP): Process Memory Attributes object to specify memory search attributes (default is empty PMAP).

        Returns:
            None

        Example:
            To initialize AndroidMemoryTool with custom parameters:
            ```python
            tool = AndroidMemoryTool(PKG="ac_client", TYPE=DataTypes.WORD, SPEED_MODE=True, WORKERS=4)
            ```
        """

        self._pkg_name = PKG
        if _WIN_PLATFORM:
            # PMAP is not supported in Windows API
            self._current_instance = AndroidMemoryToolWindows(PKG=PKG, TYPE=TYPE, SPEED_MODE=SPEED_MODE,
                                                              WORKERS=WORKERS)
        else:
            self._current_instance = AndroidMemoryToolLinux(PKG=PKG,
                                                            TYPE=TYPE,
                                                            SPEED_MODE=SPEED_MODE,
                                                            WORKERS=WORKERS,
                                                            pMAP=pMAP)

    def __repr__(self) -> str:
        """
        Return a string representation of the AndroidMemoryTool instance.

        Returns:
            str: A string containing the class name and the target package name or PID.

        Example:
            ```python
            tool = AndroidMemoryTool(PKG="ac_client")
            print(tool)  # Output: "AndroidMemoryTool: 'ac_client'"
            ```
        """

        return f'{self.__class__.__name__}: "{self._pkg_name}"'

    @staticmethod
    def get_version_code() -> float:
        """
        Get the version code of AndroidMemoryTool.

        Returns:
            float: The version code.

        Example:
            ```python
            version = AndroidMemoryTool.get_version_code()
            print(version)
            ```
        """
        return AndroidMemoryTool.VERSION_CODE

    @staticmethod
    def get_cpu_counts(fraction: int = None) -> int:
        """
        Get the number of CPU cores available on the device.

        Args:
            fraction (int, optional): If specified, returns a fraction of available CPU cores (default is None).

        Returns:
            int: The number of CPU cores.

        Example:
            ```python
            cores = AndroidMemoryTool.get_cpu_counts()
            print(cores)

            # Get half of available CPU cores
            half_cores = AndroidMemoryTool.get_cpu_counts(fraction=2)
            print(half_cores)
            ```
        """

        if fraction:
            return int(psutil.cpu_count() / fraction)
        return psutil.cpu_count()

    @staticmethod
    def get_developer() -> str:
        """
        Get the name of the developer of AndroidMemoryTool.

        Returns:
            str: The developer's name.

        Example:
            ```python
            developer = AndroidMemoryTool.get_developer()
            print(developer)
            ```
        """

        return AndroidMemoryTool.DEVELOPER

    @staticmethod
    def get_platform(verbose: bool = False) -> str:
        """
        Get the platform the script is running on (Linux, Android, Windows).

        Args:
            verbose (bool, optional): If True, print a message for unsupported platforms (default is False).

        Returns:
            str: The platform name.

        Example:
            ```python
            platform_name = AndroidMemoryTool.get_platform(verbose=True)
            print(platform_name)
            ```
        """

        if platform.system() == 'Windows':
            return "Windows"
        elif platform.system() == 'Linux':
            return 'Linux'
        elif check_output(['uname', '-o']).strip() == b'Android':
            return 'Android'
        else:
            if verbose:
                print('[DEBUG] This platform is not currently supported by AndroidMemoryTool')
            return platform.system()

    @staticmethod
    def is_root_acquired() -> bool:
        """
        Check if the script is running with root/administrator privileges.

        Returns:
            bool: True if running with root/admin privileges, False otherwise.

        Example:
            ```python
            is_root = AndroidMemoryTool.is_root_acquired()
            print(is_root)
            ```
        """

        if _WIN_PLATFORM:
            import ctypes
            return True if ctypes.windll.shell32.IsUserAnAdmin() == 1 else False
        from os import getuid
        return True if getuid() == 0 else False

    def read_value(self, read: any, is_grouped: bool = False, range_val: int = 512) -> any:
        """
        Search and read a value or values from memory.

        Args:
            read (any): The value or values to search for in memory.
            is_grouped (bool, optional): True to group search results, False to return individual results
                                         (default is False).
            range_val (int, optional): The maximum range for memory search (default is 512).

        Returns:
            any: The value or values found in memory.

        Example:
            ```python
            values = tool.read_value(100)
            founded_offsets = values[0]
            founded_values = values[1]
            print(founded_values)
            print(founded_offsets)
            ```
        """

        # Note: Group search is not available for string data-types
        return self._current_instance.read_value(read=read, is_grouped=is_grouped, range_val=range_val)

    def read_write_value(self, read: any, write: any, is_grouped: bool = False, range_val: int = 552) -> any:
        """
        Search, read, and optionally write a value or values in memory.

        Args:
            read (any): The value or values to search for in memory.
            write (any): The value to replace the found value(s) with.
            is_grouped (bool, optional): True to group search results, False to return individual results
                                         (default is False).
            range_val (int, optional): The maximum range for memory search (default is 552).

        Returns:
            any: The value or values found in memory.

        Example:
            ```python
            values1 = tool.read_write_value(100, 10)
            print(values1)
            ```
        """

        # Note: Group search is not available for string data-types
        return self._current_instance.read_write_value(read=read, write=write, is_grouped=is_grouped,
                                                       range_val=range_val)

    def write_lib(self, base_address: str, offset: str, write_value: any) -> any:
        """
        Write a value to a specific memory address.

        Args:
            base_address (str): The base address in hexadecimal format.
            offset (str): The offset in hexadecimal format.
            write_value (any): The value to write to the specified memory address.

        Returns:
            any: The result of the write operation.

        Example:
            ```python
            values1 = tool.write_lib(base_address='0x12345678', offset='0x100', write_value=42)
            print(values1)
            ```
        """

        return self._current_instance.write_lib(base_address=base_address, offset=offset, write_value=write_value)

    def read_lib(self, base_address: str, offset: str, value: any((str, int, None)) = None) -> any:
        """
        Read a value from a specific memory address.

        Args:
            base_address (str): The base address in hexadecimal format.
            offset (str): The offset in hexadecimal format.
            value (any, optional): A value to compare against the read value (default is None).

        Returns:
            any: The value read from the specified memory address.

        Example:
            ```python
            values1 = tool.read_lib(base_address='0x12345678', offset='0x100', value=None)
            print(values1)
            ```
        """

        return self._current_instance.read_lib(base_address=base_address, offset=offset, value=value)

    def refiner_address(self, list_address: list, value_to_refine: any) -> any:
        """
        Refine a list of memory addresses based on a specific value.

        Args:
            list_address (list): A list of memory addresses.
            value_to_refine (any): The value to refine the addresses against.

        Returns:
            any: The refined list of memory addresses.

        Example:
            ```python
            values = tool.read_value(100)
            founded_offsets = values[0]
            refined_address = tool.refiner_address(list_address=founded_offsets, value_to_refine=50)
            print(refined_address)
            ```
        """

        return self._current_instance.refiner_address(list_address=list_address, value_to_refine=value_to_refine)

    def get_module_base_address(self, module_name: str) -> any:
        """
        Get the base address of a specific module in the target process.

        Args:
            module_name (str): The name of the module to retrieve the base address of.

        Returns:
            any: The base address of the module.

        Example:
            ```python
            base_addr = tool.get_module_base_address("client.so")
            print(base_addr)
            ```
        """

        return self._current_instance.get_module_base_address(module_name=module_name)

    def raw_dump(self, lib_name: str, path='./') -> bool:
        """
        Dump the memory of a process to a file.

        Args:
            lib_name (str): The name of the library to dump.
            path (str, optional): The path to save the dump file (default is './').

        Returns:
            bool: True if the dump was successful, False otherwise.

        Example:
            ```python
            dump = tool.raw_dump(lib_name='client.so', path='./')
            print(dump)
            ```
        """

        return self._current_instance.raw_dump(lib_name=lib_name, path=path)

    def find_hex_pattern(self, search_pattern: str) -> any:
        """
        Find hex patterns in memory (Linux and Android only).

        Args:
            search_pattern (str): The hex pattern to search for.

        Returns:
            any: A tuple containing found addresses, total patterns found, and found values.

        Example:
            ```python
            found_pattern = tool.find_hex_pattern("87 ?? 2B")
            for index in range(0, len(found_pattern[0])):
                print(f"{found_pattern[0][index]}: {found_pattern[2][index]}")
            print(f"Total Pattern found: {found_pattern[1]}")
            ```
        """

        # Note: Not available for Windows API in this version
        return self._current_instance.find_hex_pattern(search_pattern=search_pattern)

    def find_and_replace_hex_pattern(self, search_pattern: str, replace_pattern: str) -> any:
        """
        Find and replace hex patterns in memory (Linux and Android only).

        Args:
            search_pattern (str): The hex pattern to search for.
            replace_pattern (str): The hex pattern to replace with.

        Returns:
            any: A tuple containing found addresses, total patterns found, and found values.

        Example:
            ```python
            found_pattern = tool.find_and_replace_hex_pattern("87 ?? 2B", "87 1D 2B")
            for index in range(0, len(found_pattern[0])):
                print(f"{found_pattern[0][index]}: {found_pattern[2][index]}")
            print(f"Total Pattern found and replaced: {found_pattern[1]}")
            ```
        """

        # Note: Not available for Windows API in this version
        return self._current_instance.find_and_replace_hex_pattern(search_pattern=search_pattern,
                                                                   replace_pattern=replace_pattern)

    def dump_maps(self, path="./") -> bool:
        """
        Dump the memory maps of a process to a file.

        Args:
            path (str, optional): The path to save the memory maps dump file (default is './').

        Returns:
            bool: True if the dump was successful, False otherwise.

        Example:
            ```python
            is_dumped = tool.dump_maps(path="./")
            print(is_dumped)
            ```
        """

        return self._current_instance.dump_maps(path=path)

    def get_pid(self) -> int:
        """
        Get the Process ID (PID) of the target process.

        Returns:
            int: The PID of the process.

        Raises:
            PIDException: If the specified process is not running in memory.

        Example:
            ```python
            pid = tool.get_pid()
            print(pid)
            ```
        """
        return int(self._current_instance.get_process_id())

    def get_memory_profiler(self, logging_file_path: str = "memory_log.txt") -> MemoryProfiler:
        """
        Get a MemoryProfiler instance to analyze memory usage.

        Args:
            logging_file_path (str, optional): The path to the memory profiling log file (default is "memory_log.txt").

        Returns:
            MemoryProfiler: A MemoryProfiler instance.

        Example:
            ```python
            memory_profiler = tool.get_memory_profiler(logging_file_path="memory_log.txt")
            memory_profiler.start_profiling(logging=False)
            ```
        """
        # Only needed PID (Initialize the MemoryTool with pid or name only)
        pid = self.get_pid()
        return MemoryProfiler(pid=pid, logging_file_path=logging_file_path)
