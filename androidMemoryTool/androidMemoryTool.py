"""
 *  date   : 2022/03/23
 *  Version : 0.3
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# ! /usr/bin/env python
from .libs_read_writers import LibsControllers
from .ThreadingController import FastSearchAlgo
from .mapping import Mapping


class AndroidMemoryTool(FastSearchAlgo):
    _LibControllerObject = LibsControllers()

    def __init__(self, PKG: str, TYPE=FastSearchAlgo.DataTypes.DWORD, SPEED_MODE=True, WORKERS=50,
                 pMAP=FastSearchAlgo.PMAP()):
        super(AndroidMemoryTool, self).__init__()
        self.initialize(PKG, TYPE, SPEED_MODE, WORKERS, pMAP)

    def initialize(self, PKG, TYPE, SPEED_MODE, WORKERS, pMAP):
        super().init_setup(PKG, TYPE, SPEED_MODE, WORKERS)
        super().init_tool(pMAP)

    def read_value(self, read: any) -> any:
        speed_mode = super().get_variables(is_speed=True)
        data_types = super().get_variables(is_data_byte=True)
        proc_id = super().get_variables(is_pid=True)

        if proc_id == '':
            print('[*] Pid not found')
            return None

        if data_types != -1:
            maps_addr = super().get_variables(is_map_addr=True)
            value_to_read = super().data_type_encoding(read)

            if data_types == 0:
                if speed_mode:
                    super().fast_search_algorithms_text(proc_id, maps_addr, value_to_read)
                    return self._SearchAndReadObject.get_readers_values()
                else:
                    self._SearchAndReadObject.search_and_read_text(proc_id, maps_addr, value_to_read)
                    return self._SearchAndReadObject.get_readers_values()
            else:
                if speed_mode:
                    super().fast_search_algorithms_value(proc_id, maps_addr, value_to_read,
                                                         data_types)
                    return self._SearchAndReadObject.get_readers_values()
                else:
                    return self._SearchAndReadObject.search_and_read(proc_id, maps_addr, data_types, value_to_read)
        return None

    def read_write_value(self, read: any, write: any) -> any:
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
                    return self._SearchAndWriteObject.get_writer_values()
                else:
                    return self._SearchAndWriteObject.search_and_write_text(proc_id, maps_addr, value_to_read,
                                                                            value_to_write)
            else:
                if speed_mode:
                    super().fast_search_algorithms_value(proc_id, maps_addr, value_to_read,
                                                         data_types, value_to_write)
                    return self._SearchAndWriteObject.get_writer_values()
                else:
                    return self._SearchAndWriteObject.search_and_write(proc_id, maps_addr, data_types, value_to_read,
                                                                       value_to_write)
        return None

    def write_lib(self, base_address: hex, offset: hex, write_value: any) -> any:
        data_types = super().get_variables(is_data_byte=True)
        proc_id = super().get_variables(is_pid=True)

        if proc_id == '':
            print('[*] Pid not found')
            return None

        if data_types != -1:
            value_to_write = super().data_type_encoding(write_value)
            if data_types == 0:
                print("[*] Data type not supported")
            else:
                return self._LibControllerObject.write_lib_offsets(proc_id, base_address, offset, value_to_write)
        return None

    def read_lib(self, base_address: hex, offset: hex) -> any:
        data_types = super().get_variables(is_data_byte=True)
        proc_id = super().get_variables(is_pid=True)

        if proc_id == '':
            print('[*] Pid not found')
            return None

        if data_types != -1:
            if data_types == 0:
                print("[*] Data type not supported")
            else:
                value = self._LibControllerObject.read_lib_offsets(proc_id, base_address, offset, data_types)
                if value:
                    return super().data_type_decoding(value)
        return None

    def refiner_address(self, list_address: list, value_to_refine: any) -> any:
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
        proc_id = super().get_variables(is_pid=True)
        address = Mapping.mapping_dump_libs(proc_id, lib_name)

        if len(address) < 1:
            print("[*] Module not found")
            return False

        binary_string = self._LibControllerObject.raw_dumper(proc_id, address)
        open(f"{path}{address[0][0]}-{address[len(address) - 1][1]}-{lib_name}.bin", 'wb').write(binary_string)
        return True
