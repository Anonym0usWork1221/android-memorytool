"""
 *  date   : 2022/03/23
 *  Version : 0.4
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# ! /usr/bin/env python
from .libs_read_writers import LibsControllers
from .ThreadingController import FastSearchAlgo
from .additional_features import AdditionalFeatures
from .mapping import Mapping


class AndroidMemoryTool(FastSearchAlgo):
    _LibControllerObject = LibsControllers()

    def __init__(self, PKG: any((str, int)), TYPE=FastSearchAlgo.DataTypes.DWORD, SPEED_MODE=True, WORKERS=50,
                 pMAP=FastSearchAlgo.PMAP()) -> None:
        """
        Initialize the tool to read or write runtime memory.
        :rtype: None
        :param PKG: Any(PID or PackageName)
        :param TYPE: DataType
        :param SPEED_MODE: Turn on/off Threading
        :param WORKERS: Number of threads
        :param pMAP: MAPS
        """
        super(AndroidMemoryTool, self).__init__()
        self.initialize(PKG, TYPE, SPEED_MODE, WORKERS, pMAP)

    def initialize(self, PKG: any((str, int)), TYPE: str, SPEED_MODE: bool, WORKERS: int,
                   pMAP: FastSearchAlgo.PMAP) -> None:
        """
        Initialize the DataClass with the provided Data.
        :rtype: None
        :param PKG: Any(PID or PackageName)
        :param TYPE: DataType
        :param SPEED_MODE: Turn on/off Threading
        :param WORKERS: Number of threads
        :param pMAP: MAPS
        """
        super().init_setup(PKG, TYPE, SPEED_MODE, WORKERS)
        super().init_tool(pMAP)

    def read_value(self, read: any) -> any:
        """
        The Read Value takes Any (int, string, float) as a parameter and search it in memory and return results.
        :param read: Value
        :type read: any
        :return: Any(tuple, list, None)
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
        The Write Value takes Any (int, string, float) as a parameter and replace it in memory and return results.
        :param read: Value(toFind)
        :param write: Value(toWrite)
        :return: any(tuple, list, None)
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

    def write_lib(self, base_address: hex, offset: hex, write_value: any) -> any:
        """
        Replace address value.
        :param base_address: Hex(BaseAddress)
        :param offset: Hex(Offset)
        :param write_value: Value(toWrite)
        :return: Any
        """
        data_types = super().get_variables(is_data_byte=True)
        proc_id = super().get_variables(is_pid=True)

        if proc_id == '':
            print('[*] Pid not found')
            return None

        if data_types != -1:
            value_to_write = super().data_type_encoding(write_value)
            return self._LibControllerObject.write_lib_offsets(proc_id, base_address, offset, value_to_write)
        return None

    def read_lib(self, base_address: hex, offset: hex, value:  any((str, int, None)) = None) -> any:
        """
        :param value: Optional(For UTF-8 & UTF-16)
        :param base_address: Hex(BaseAddress)
        :param offset: Hex(Offset)
        :return: any
        """

        data_types = super().get_variables(is_data_byte=True)
        proc_id = super().get_variables(is_pid=True)

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
        :param list_address: list(FoundedAddress)
        :param value_to_refine: Value(ChangedValue)
        :return: Any
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
                refined_address = self._LibControllerObject.address_refiners(proc_id, list_address, data_types,
                                                                             value_to_read)
                return refined_address
        return None

    @staticmethod
    def get_module_base_address(pid: str, module_name: str) -> any:
        """
        :param pid: Str(PID)
        :param module_name: Str(Module)
        :return: Any
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
        :param lib_name: Str(LibName or Address)
        :param path: Str(OutputPath)
        :return: bool(Ture, False)
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

    def find_hex_pattern(self, hex_pattern: str) -> any:
        """
        :param hex_pattern: Str(Pattern, eg:88 ?? 97)
        :return: Any
        """
        proc_id = super().get_variables(is_pid=True)
        maps_addr = super().get_variables(is_map_addr=True)
        speed_mode = super().get_variables(is_speed=True)

        filter_user_data = hex_pattern.replace(" ", "")
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
                                                           pattern_of_hex)
            values = self._AdditionalFeaturesObject.get_pattern_finder_values()
            self._AdditionalFeaturesObject.reset_queue()
            return values

        return AdditionalFeatures.find_hexadecimal_pattern(proc_id, maps_addr, bytes_of_filtered_data, pattern_of_hex)

    def dump_maps(self, path="./") -> bool:
        """
        :param path: Str(OutputPath)
        :return: bool(True, False)
        """
        proc_id = super().get_variables(is_pid=True)
        if proc_id:
            map_file = open(f"/proc/{proc_id}/maps", "r").read()
            open(f"{path}Map_{proc_id}.txt", "w").write(map_file)
            return True

        return False
