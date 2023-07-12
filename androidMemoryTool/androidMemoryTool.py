"""
 *  date   : 2023/07/11
 *  Version : 0.5
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# ! /usr/bin/env python
from .additional_features import AdditionalFeatures
from .ThreadingController import FastSearchAlgo
from .libs_read_writers import LibsControllers
from .mapping import Mapping


class AndroidMemoryTool(FastSearchAlgo):
    """
    This class represents a tool for performing memory-related operations on an Android device. It inherits from the FastSearchAlgo class.

    Constructor:

    __init__(self, PKG: any((str, int)), TYPE=FastSearchAlgo.DataTypes.DWORD, SPEED_MODE=True, WORKERS=50,
             pMAP=FastSearchAlgo.PMAP()) -> None:
             Initializes an instance of the AndroidMemoryTool class. It takes the following parameters:
    PKG: Package name or ID of the target process.
    TYPE: Data type to be used in memory operations (default: FastSearchAlgo.DataTypes.DWORD).
    SPEED_MODE: Flag indicating whether speed mode is enabled (default: True).
    WORKERS: Number of worker threads to use in search operations (default: 50).
    pMAP: Instance of the PMAP class for memory mapping (default: FastSearchAlgo.PMAP()).

    Methods:

    initialize(self, PKG: any((str, int)), TYPE: str, SPEED_MODE: bool,
               WORKERS: int, pMAP: FastSearchAlgo.PMAP) -> None:
               Initializes the AndroidMemoryTool instance with the specified parameters.

    read_value(self, read: any) -> any: Reads the value at a given memory address. It takes the following parameter:
    read: Memory address to read from.

    read_write_value(self, read: any, write: any) -> any:
                     Reads the value at a given memory address and then writes a new value to that address.
                      It takes the following parameters:
    read: Memory address to read from.
    write: Value to write to the memory address.

    write_lib(self, base_address: hex, offset: hex, write_value: any) -> any:
              Writes a value to a specific offset in a shared library. It takes the following parameters:
    base_address: Base address of the shared library.
    offset: Offset within the shared library.
    write_value: Value to write to the specified offset.

    read_lib(self, base_address: hex, offset: hex, value: any((str, int, None)) = None) -> any:
             Reads a value from a specific offset in a shared library. It takes the following parameters:
    base_address: Base address of the shared library.
    offset: Offset within the shared library.
    value (optional): Value to use for dynamic buffer size calculation (default: None).

    refiner_address(self, list_address: list, value_to_refine: any) -> any:
                Refines a list of memory addresses based on a specific value. It takes the following parameters:
    list_address: List of memory addresses to refine.
    value_to_refine: Value to refine the addresses based on.

    get_module_base_address(pid: str, module_name: str) -> any:
                    Retrieves the base address of a specific module within a process. It takes the following parameters:
    pid: Process ID.
    module_name: Name of the module.

    raw_dump(self, lib_name: str, path='./') -> bool:
             Dumps the raw binary contents of a shared library. It takes the following parameters:
    lib_name: Name of the shared library.
    path (optional): Path to save the binary dump (default: './').

    find_hex_pattern(self, hex_pattern: str) -> any:
            Searches for a hexadecimal pattern in the memory of the target process. It takes the following parameter:
    hex_pattern: Hexadecimal pattern to search for.

    dump_maps(self, path="./") -> bool:
        Dumps the memory mapping information of the target process to a file. It takes the following parameter:
    path (optional): Path to save the memory mapping file (default: './').

    """
    VERSION_CODE = 0.5
    DEVELOPER = "Abdul Moez"
    _LibControllerObject = LibsControllers()

    def __init__(self, PKG: any((str, int)), TYPE=FastSearchAlgo.DataTypes.DWORD, SPEED_MODE=True, WORKERS=50,
                 pMAP=FastSearchAlgo.PMAP()) -> None:
        """
            Initializes an instance of the AndroidMemoryTool class. It takes the following parameters:
        Args:
            PKG: Package name or ID of the target process.
            TYPE: Data type to be used in memory operations (default: FastSearchAlgo.DataTypes.DWORD).
            SPEED_MODE: Flag indicating whether speed mode is enabled (default: True).
            WORKERS: Number of worker threads to use in search operations (default: 50).
            pMAP: Instance of the PMAP class for memory mapping (default: FastSearchAlgo.PMAP()).
        """
        super(AndroidMemoryTool, self).__init__()
        self.initialize(PKG, TYPE, SPEED_MODE, WORKERS, pMAP)

    def initialize(self, PKG: any((str, int)), TYPE: str, SPEED_MODE: bool, WORKERS: int,
                   pMAP: FastSearchAlgo.PMAP) -> None:
        """
        Initializes the AndroidMemoryTool object.

        Args:
            PKG: The package name or process ID.
            TYPE: The data type to search for. Defaults to FastSearchAlgo.DataTypes.DWORD.
            SPEED_MODE: Whether to enable speed mode. Defaults to True.
            WORKERS: The number of workers to use for searching. Defaults to 50.
            pMAP: The memory map to use. Defaults to FastSearchAlgo.PMAP().
        """

        super().init_setup(PKG, TYPE, SPEED_MODE, WORKERS)
        super().init_tool(pMAP)

    @staticmethod
    def get_version_code():
        return AndroidMemoryTool.VERSION_CODE

    @staticmethod
    def get_developer():
        return AndroidMemoryTool.DEVELOPER

    def read_value(self, read: any) -> any:
        """
        Reads the value from the specified memory address.

        Args:
            read: The memory address to read from.

        Returns:
            The value read from the memory address.
        """

        # gets if speed mode is on or off
        speed_mode = super().get_variables(is_speed=True)
        # gets data type bytes in int
        data_types = super().get_variables(is_data_byte=True)
        # gets PID of running process
        proc_id = super().get_variables(is_pid=True)

        if proc_id == '':
            print('[*] Pid not found')
            return None

        # If data type is valid continue
        if data_types != -1:
            maps_addr = super().get_variables(is_map_addr=True)
            value_to_read = super().data_type_encoding(read)

            if data_types == 0:
                if speed_mode:
                    super().fast_search_algorithms_text(proc_id, maps_addr, value_to_read)
                    value = self._SearchAndReadObject.get_readers_values()
                    self._SearchAndReadObject.reset_queue()
                    return value

                return self._SearchAndReadObject.search_and_read_text(proc_id, maps_addr, value_to_read)
            else:
                if speed_mode:
                    super().fast_search_algorithms_value(proc_id, maps_addr, value_to_read,
                                                         data_types)
                    value = self._SearchAndReadObject.get_readers_values()
                    self._SearchAndReadObject.reset_queue()
                    return value

                return self._SearchAndReadObject.search_and_read(proc_id, maps_addr, data_types, value_to_read)

        return None

    def read_write_value(self, read: any, write: any) -> any:
        """
        Reads the value from the specified memory address and writes the new value to it.

        Args:
            read: The memory address to read from.
            write: The new value to write.

        Returns:
            The value written to the memory address.
        """

        speed_mode = super().get_variables(is_speed=True)
        data_types = super().get_variables(is_data_byte=True)
        proc_id = super().get_variables(is_pid=True)

        if proc_id == '':
            print('[*] Pid not found')
            return None

        if data_types != -1:
            maps_addr = super().get_variables(is_map_addr=True)
            value_to_read, value_to_write = super().data_type_encoding(read, write)

            if data_types == 0:
                if speed_mode:
                    super().fast_search_algorithms_text(proc_id, maps_addr, value_to_read, value_to_write)
                    value = self._SearchAndWriteObject.get_writer_values()
                    self._SearchAndWriteObject.reset_queue()
                    return value

                return self._SearchAndWriteObject.search_and_write_text(proc_id, maps_addr, value_to_read,
                                                                        value_to_write)
            else:
                if speed_mode:
                    super().fast_search_algorithms_value(proc_id, maps_addr, value_to_read,
                                                         data_types, value_to_write)
                    value = self._SearchAndWriteObject.get_writer_values()
                    self._SearchAndWriteObject.reset_queue()
                    return value

                return self._SearchAndWriteObject.search_and_write(proc_id, maps_addr, data_types, value_to_read,
                                                                   value_to_write)
        return None

    def write_lib(self, base_address: str, offset: str, write_value: any) -> any:
        """
        Writes the value to the specified library offset.

        Args:
            base_address: The base address of the library.
            offset: The offset within the library.
            write_value: The value to write.

        Returns:
            The value written to the library offset.
        """

        data_types = super().get_variables(is_data_byte=True)
        proc_id = super().get_variables(is_pid=True)
        base_address = str(base_address)
        offset = str(offset)

        if proc_id == '':
            print('[*] Pid not found')
            return None

        if data_types != -1:
            value_to_write = super().data_type_encoding(write_value)
            return self._LibControllerObject.write_lib_offsets(proc_id, base_address, offset, value_to_write)
        return None

    def read_lib(self, base_address: str, offset: str, value:  any((str, int, None)) = None) -> any:
        """
        Reads the value from the specified library offset.

        Args:
            base_address: The base address of the library.
            offset: The offset within the library.
            value: The additional value parameter for certain data types. Defaults to None.

        Returns:
            The value read from the library offset.
        """

        data_types = super().get_variables(is_data_byte=True)
        proc_id = super().get_variables(is_pid=True)
        base_address = str(base_address)
        offset = str(offset)

        if proc_id == '':
            print('[*] Pid not found')
            return None

        if data_types != -1:
            if data_types == 0:
                if value is None:
                    print("[*] Needed Value parameter")
                    return None

                if isinstance(value, int):
                    buffer = 18 + (2 * int(value))
                elif str(value).isnumeric():
                    buffer = 18 + (2 * int(str(value)))
                else:
                    buffer = 18 + (2 * int(len(str(value))))

                value = self._LibControllerObject.read_lib_offsets(proc_id, base_address, offset, buffer)
                if value:
                    return super().data_type_decoding(value)

            else:
                value = self._LibControllerObject.read_lib_offsets(proc_id, base_address, offset, data_types)
                if value:
                    return super().data_type_decoding(value)
        return None

    def refiner_address(self, list_address: list, value_to_refine: any) -> any:
        """
        Refines the list of addresses based on the specified value to refine.

        Args:
            list_address: The list of addresses to refine.
            value_to_refine: The value to refine.

        Returns:
            The refined list of addresses.
        """

        proc_id = super().get_variables(is_pid=True)
        data_types = super().get_variables(is_data_byte=True)
        value_to_read = super().data_type_encoding(value_to_refine)

        if proc_id == '':
            print('[*] Pid not found')
            return None

        if data_types != -1:
            if data_types == 0:
                print("[*] Data type not supported")
            else:
                return self._LibControllerObject.address_refiners(proc_id, list_address, data_types, value_to_read)
        return None

    @staticmethod
    def get_module_base_address(pid: str, module_name: str) -> any:
        """
        Gets the base address of the specified module for the given process ID.

        Args:
            pid: The process ID.
            module_name: The name of the module.

        Returns:
            The base address of the module.
        """

        map_file = open(f"/proc/{pid}/maps", 'r')
        address = []
        if map_file is not None:
            for line in map_file.readlines():
                line_split = line.split()
                if module_name in line_split[len(line_split) - 1]:
                    address.append(line_split[0].split('-'))
        if len(address) < 1:
            print("[*] Module not found")
            return None
        base_address = hex(int(address[0][0], 16))
        return base_address

    def raw_dump(self, lib_name: str, path='./') -> bool:
        """
        Dumps the specified library to a raw binary file.

        Args:
            lib_name: The name of the library.
            path: The path to save the dumped file. Defaults to './'.

        Returns:
            True if the dump was successful, False otherwise.
        """

        proc_id = super().get_variables(is_pid=True)

        if "-" in lib_name:
            address = lib_name.split("-")
        else:
            address = Mapping.mapping_dump_libs(proc_id, lib_name)

        if len(address) < 1:
            print("[*] Module not found")
            return False

        binary_string = self._LibControllerObject.raw_dumper(proc_id, address)
        open(f"{path}{address[0][0]}-{address[len(address) - 1][1]}-{lib_name.replace('.so', '')}.bin", 'wb') \
            .write(binary_string)
        return True

    def find_hex_pattern(self, search_pattern: str) -> any:
        """
        Finds the specified hexadecimal pattern in the memory.

        Args:
            search_pattern: The hexadecimal pattern to search for.

        Returns:
            The addresses where the pattern was found.
        """

        proc_id = super().get_variables(is_pid=True)
        maps_addr = super().get_variables(is_map_addr=True)
        speed_mode = super().get_variables(is_speed=True)

        filter_user_data = search_pattern.replace(" ", "")
        bytes_of_filtered_data = int(len(filter_user_data) / 2)
        pattern_of_hex = ""
        character_counter_hex = 0
        for char in filter_user_data:
            if char == "?":
                character_counter_hex += 1
            else:
                if character_counter_hex != 0:
                    pattern_of_hex += f"[A-Fa-f0-9]{{{character_counter_hex}}}"
                    character_counter_hex = 0
                if char != "?":
                    pattern_of_hex += char

        if character_counter_hex != 0:
            pattern_of_hex += f"[A-Fa-f0-9]{{{character_counter_hex}}}"
        if speed_mode:
            super().fast_search_algorithms_pattern_finding(proc_id, maps_addr, bytes_of_filtered_data,
                                                           pattern_of_hex)
            values = self._AdditionalFeaturesObject.get_pattern_finder_values()
            self._AdditionalFeaturesObject.reset_queue()
            return values

        return AdditionalFeatures.find_hexadecimal_pattern(proc_id, maps_addr, bytes_of_filtered_data, pattern_of_hex)

    def find_and_replace_hex_pattern(self, search_pattern: str, replace_pattern: str) -> any:
        """
            Finds and replaces a hexadecimal pattern in memory addresses.

            Args:
                search_pattern (str): The pattern to search for. It can contain hexadecimal digits (0-9, A-F)
                 and '?' as a wildcard for any single hexadecimal digit.
                replace_pattern (str): The pattern to replace the found pattern with.
                 It should be a valid hexadecimal string.

            Returns:
                any: The result of the pattern finding and replacement operation.
                 The format of the result depends on the 'speed_mode' setting.
        """

        proc_id = super().get_variables(is_pid=True)
        maps_addr = super().get_variables(is_map_addr=True)
        speed_mode = super().get_variables(is_speed=True)

        filter_user_data = search_pattern.replace(" ", "")
        replace_pattern = replace_pattern.replace(" ", "")
        bytes_of_filtered_data = int(len(filter_user_data) / 2)
        pattern_of_hex = ""
        character_counter_hex = 0
        for char in filter_user_data:
            if char == "?":
                character_counter_hex += 1
            else:
                if character_counter_hex != 0:
                    pattern_of_hex += f"[A-F0-9]{{{character_counter_hex}}}"
                    character_counter_hex = 0
                if char != "?":
                    pattern_of_hex += char

        if character_counter_hex != 0:
            pattern_of_hex += f"[A-F0-9]{{{character_counter_hex}}}"

        if speed_mode:
            super().fast_search_algorithms_pattern_finding(proc_id, maps_addr, bytes_of_filtered_data,
                                                           pattern_of_hex, replace_pattern)
            values = self._AdditionalFeaturesObject.get_pattern_finder_values()
            self._AdditionalFeaturesObject.reset_queue()
            return values

        return AdditionalFeatures.find_and_replace_hexadecimal_pattern(proc_id, maps_addr,
                                                                       bytes_of_filtered_data, pattern_of_hex,
                                                                       replace_pattern)

    def dump_maps(self, path="./") -> bool:
        """
        Dumps the memory maps of the process.

        Args:
            path: The path to save the dumped file. Defaults to './'.

        Returns:
            True if the dump was successful, False otherwise.
        """

        proc_id = super().get_variables(is_pid=True)
        if proc_id:
            map_file = open(f"/proc/{proc_id}/maps", "r").read()
            open(f"{path}Map_{proc_id}.txt", "w").write(map_file)
            return True

        return False

