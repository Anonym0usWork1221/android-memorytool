"""
 *  date   : 2023/07/11
 *  Version : 0.5
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

from subprocess import check_output, CalledProcessError
from .mapping import Mapping
from dataclasses import dataclass
from struct import pack, unpack
from binascii import unhexlify
from sys import byteorder


class DataClasses:
    _PKG_NAME = ""
    _DATA_TYPES = ""
    _IS_SPEED_MODE = False
    _TOTAL_WORKERS = 55

    _MAPS_ADDR = []
    _DATA_BYTE = 0
    _PID = ""

    @dataclass()
    class DataTypes:
        """
        Data class that defines different data types used in the code.
        """

        DWORD: str = "DWORD"
        FLOAT: str = "FLOAT"
        DOUBLE: str = "DOUBLE"
        WORD: str = "WORD"
        BYTE: str = "BYTE"
        QWORD: str = "QWORD"
        XOR: str = "XOR"
        UTF_8: str = "UTF-8"
        UTF_16LE: str = "UTF-16LE"

    @dataclass()
    class PMAP:
        """
            Data class that defines different options for memory mapping.
        """

        ALL: bool = True
        B_BAD: bool = False
        C_ALLOC: bool = False
        C_BSS: bool = False
        C_DATA: bool = False
        C_HEAP: bool = False
        JAVA_HEAP: bool = False
        A_ANONYMOUS: bool = False
        CODE_SYSTEM: bool = False
        STACK: bool = False
        ASHMEM: bool = False
        J_Java: bool = False
        CODE_APP: bool = False
        V_video: bool = False

    def __init__(self):
        ...

    @staticmethod
    def get_pid(pkg: any((str, int))) -> str:
        """
            Retrieves the process ID (PID) for the given package name or PID.

            Args:
                pkg: The package name or PID.

            Returns:
                The process ID (PID) as a string.
        """

        pkg = str(pkg)
        # if the pkg is numeric string
        if pkg.isnumeric():
            try:
                pid_id = check_output(["ps", "-q", pkg, "-o", "cmd="])
                return pkg if pid_id.decode().strip() is not None else ""
            except CalledProcessError:
                print("[-] Processes is not running")
        else:
            try:
                pid_id = check_output(["pidof", "-s", pkg])  # gets the first id if multiple ids found
                process_ids = pid_id.decode().strip()
                return str(process_ids)
            except CalledProcessError:
                print("[-] Processes is not running")

        return ""

    def init_setup(self, PKG: any((str, int)), TYPE=DataTypes.DWORD, SPEED_MODE=False, WORKERS=55) -> None:
        """
        Initializes the setup with the specified package, data type, speed mode, and number of workers.

        Args:
            PKG: The package name or PID.
            TYPE: The data type.
            SPEED_MODE: Flag indicating whether speed mode is enabled or not.
            WORKERS: The number of workers.

        Returns:
            None.
        """

        self._DATA_TYPES = TYPE
        self._PKG_NAME = PKG
        self._IS_SPEED_MODE = SPEED_MODE
        self._TOTAL_WORKERS = WORKERS

    def identify_dict(self, P=PMAP()) -> list:
        """
        Identifies the memory addresses based on the given memory mapping options.

        Args:
            P: The memory mapping options.

        Returns:
            A list of identified memory addresses.
        """
        mapping_functions = {
            "ALL": Mapping.mapping_all,
            "B_BAD": Mapping.mapping_b,
            "C_ALLOC": Mapping.mapping_ca,
            "C_BSS": Mapping.mapping_cb,
            "C_DATA": Mapping.mapping_cd,
            "C_HEAP": Mapping.mapping_ch,
            "JAVA_HEAP": Mapping.mapping_jh,
            "A_ANONYMOUS": Mapping.mapping_a,
            "CODE_SYSTEM": Mapping.mapping_xs,
            "STACK": Mapping.mapping_s,
            "ASHMEM": Mapping.mapping_as,
            "J_Java": Mapping.mapping_j,
            "CODE_APP": Mapping.mapping_xa,
            "V_video": Mapping.mapping_v
        }

        wanted_ranges = [k for k, v in P.__dict__.items() if v]
        address_set = set()

        for map_name in wanted_ranges:
            if map_name in mapping_functions:
                address_set.update(mapping_functions[map_name](self.get_pid(self._PKG_NAME))["address"])
                if map_name == "ALL":
                    break

        return list(address_set)

    def data_type_encoding(self, read: any, write=None) -> any:
        """
            Encodes the data values based on the specified data type for searching or writing in memory.

            Args:
                read: The value to be encoded for searching in memory.
                write: The value to be encoded for writing in memory.

            Returns:
                The encoded search value and replace value (if provided).
        """
        if self._DATA_TYPES == "DWORD":
            if write:
                if "h" in str(read).lower():
                    read = int(str(read).lower().replace("h", ""), 16)
                if "h" in str(write).lower():
                    write = int(str(write).lower().replace("h", ""), 16)

                if byteorder == 'little':
                    search_value = pack('<i', read)
                    replace_value = pack('<i', write)
                else:
                    search_value = pack('>i', read)
                    replace_value = pack('>i', write)

                return search_value, replace_value

            else:
                if "h" in str(read).lower():
                    read = int(str(read).lower().replace("h", ""), 16)

                if byteorder == 'little':
                    search_value = pack('<i', read)
                else:
                    search_value = pack('>i', read)
                return search_value

        elif self._DATA_TYPES == "FLOAT":
            if write:
                if "h" in str(read).lower():
                    read = unpack('!f', bytes.fromhex(str(read).lower().replace("h", "")))[0]

                if "h" in str(write).lower():
                    write = unpack('!f', bytes.fromhex(str(write).lower().replace("h", "")))[0]

                if byteorder == 'little':
                    search_value = pack('<f', read)
                    replace_value = pack('<f', write)
                else:
                    search_value = pack('>f', read)
                    replace_value = pack('>f', write)

                return search_value, replace_value

            else:
                if "h" in str(read).lower():
                    read = unpack('!f', bytes.fromhex(str(read).lower().replace("h", "")))[0]

                if byteorder == 'little':
                    search_value = pack('<f', read)
                else:
                    search_value = pack('>f', read)
                return search_value

        elif self._DATA_TYPES == "DOUBLE":
            if write:
                if "h" in str(read).lower():
                    read = unpack('d', unhexlify(str(read).lower().replace("h", "")))[0]

                if "h" in str(write).lower():
                    write = unpack('d', unhexlify(str(write).lower().replace("h", "")))[0]

                if byteorder == 'little':
                    search_value = pack('<d', read)
                    replace_value = pack('<d', write)
                else:
                    search_value = pack('>d', read)
                    replace_value = pack('>d', write)

                return search_value, replace_value

            else:
                if "h" in str(read).lower():
                    read = unpack('d', unhexlify(str(read).lower().replace("h", "")))[0]

                if byteorder == 'little':
                    search_value = pack('<d', read)
                else:
                    search_value = pack('>d', read)
                return search_value

        elif self._DATA_TYPES == "WORD":
            if write:

                if byteorder == 'little':
                    search_value = pack('<h', read)
                    replace_value = pack('<h', write)
                else:
                    search_value = pack('>h', read)
                    replace_value = pack('>h', write)

                return search_value, replace_value

            else:
                if byteorder == 'little':
                    search_value = pack('<i', read)
                else:
                    search_value = pack('>i', read)
                return search_value

        elif self._DATA_TYPES == "BYTE":
            if write:
                if byteorder == 'little':
                    search_value = pack('<b', read)
                    replace_value = pack('<b', write)
                else:
                    search_value = pack('>b', read)
                    replace_value = pack('>b', write)

                return search_value, replace_value

            else:
                if byteorder == 'little':
                    search_value = pack('<b', read)
                else:
                    search_value = pack('>b', read)
                return search_value

        elif self._DATA_TYPES == "QWORD":
            if write:
                if byteorder == 'little':
                    search_value = pack('<q', read)
                    replace_value = pack('<q', write)
                else:
                    search_value = pack('>q', read)
                    replace_value = pack('>q', write)

                return search_value, replace_value

            else:
                if byteorder == 'little':
                    search_value = pack('<q', read)
                else:
                    search_value = pack('>q', read)
                return search_value

        elif self._DATA_TYPES == "XOR":
            if write:
                if byteorder == 'little':
                    search_value = pack('<l', read)
                    replace_value = pack('<l', write)
                else:
                    search_value = pack('>l', read)
                    replace_value = pack('>l', write)

                return search_value, replace_value

            else:
                if byteorder == 'little':
                    search_value = pack('<l', read)
                else:
                    search_value = pack('>l', read)
                return search_value

        elif self._DATA_TYPES == "UTF-8":
            if write:
                search_value = read.encode('utf-8')
                replace_value = write.encode('utf-8')

                return search_value, replace_value

            else:
                search_value = read.encode('utf-8')
                return search_value

        elif self._DATA_TYPES == "UTF-16LE":
            if write:
                search_value = read.encode('utf-16LE')
                replace_value = write.encode('utf-16LE')

                return search_value, replace_value

            else:
                search_value = read.encode('utf-16LE')
                return search_value

        else:
            return None

    def data_type_decoding(self, read: any, write=None) -> any:
        """
        Decodes the data values based on the specified data type after reading from memory.

        Args:
            read: The value to be decoded after reading from memory.
            write: The value to be decoded after writing to memory.

        Returns:
            The decoded search value and replace value (if provided).
        """

        if write:
            decode_func = unpack
            search_value = replace_value = None
            decode_format = ""
            if self._DATA_TYPES == "DWORD":
                decode_format = '<i' if byteorder == 'little' else '>i'
            elif self._DATA_TYPES == "FLOAT":
                decode_format = '<f' if byteorder == 'little' else '>f'
            elif self._DATA_TYPES == "DOUBLE":
                decode_format = '<d' if byteorder == 'little' else '>d'
            elif self._DATA_TYPES == "WORD":
                decode_format = '<h' if byteorder == 'little' else '>h'
            elif self._DATA_TYPES == "BYTE":
                decode_format = '<b' if byteorder == 'little' else '>b'
            elif self._DATA_TYPES == "QWORD":
                decode_format = '<q' if byteorder == 'little' else '>q'
            elif self._DATA_TYPES == "XOR":
                decode_format = '<l' if byteorder == 'little' else '>l'
            elif self._DATA_TYPES == "UTF-8":
                search_value = read.encode('utf-8')
                replace_value = write.encode('utf-8')
            elif self._DATA_TYPES == "UTF-16LE":
                search_value = read.encode('utf-16LE')
                replace_value = write.encode('utf-16LE')
            else:
                return None

            if search_value is None:
                search_value = decode_func(decode_format, read)
            if replace_value is None:
                replace_value = decode_func(decode_format, write)

            return search_value, replace_value
        else:
            decode_func = unpack
            decode_format = None
            search_value = None

            if self._DATA_TYPES == "DWORD":
                decode_format = '<i' if byteorder == 'little' else '>i'
            elif self._DATA_TYPES == "FLOAT":
                decode_format = '<f' if byteorder == 'little' else '>f'
            elif self._DATA_TYPES == "DOUBLE":
                decode_format = '<d' if byteorder == 'little' else '>d'
            elif self._DATA_TYPES == "WORD":
                decode_format = '<h' if byteorder == 'little' else '>h'
            elif self._DATA_TYPES == "BYTE":
                decode_format = '<b' if byteorder == 'little' else '>b'
            elif self._DATA_TYPES == "QWORD":
                decode_format = '<q' if byteorder == 'little' else '>q'
            elif self._DATA_TYPES == "XOR":
                decode_format = '<l' if byteorder == 'little' else '>l'
            elif self._DATA_TYPES == "UTF-8":
                search_value = read.encode('utf-8')
            elif self._DATA_TYPES == "UTF-16LE":
                search_value = read.encode('utf-16LE')
            else:
                return None

            if decode_format:
                search_value = decode_func(decode_format, read)

            return search_value

    def data_type_bytes(self) -> int:
        """
        Returns the number of bytes occupied by the current data type.

        Returns:
            The number of bytes occupied by the current data type.
        """
        data_type_sizes = {
            "DWORD": 4,
            "FLOAT": 4,
            "DOUBLE": 8,
            "WORD": 2,
            "BYTE": 1,
            "QWORD": 8,
            "XOR": 4,
            "UTF-8": 0,
            "UTF-16LE": 0
        }

        return data_type_sizes.get(self._DATA_TYPES, -1)

    def init_tool(self, pMAP=PMAP()) -> None:
        """
            Initializes the memory tool with the specified memory mapping options.

            Args:
                pMAP: The memory mapping options.

            Returns:
                None.
        """
        self._MAPS_ADDR = self.identify_dict(pMAP)
        self._DATA_BYTE = self.data_type_bytes()
        self._PID = self.get_pid(self._PKG_NAME)

    def get_variables(self, is_speed=False, is_pkg=False, is_data_type=False, is_workers=False, is_map_addr=False,
                      is_data_byte=False, is_pid=False) -> any:
        """
        Retrieves the specified variable based on the provided flags.

        Args:
            is_speed: Flag indicating whether to retrieve the speed mode value.
            is_pkg: Flag indicating whether to retrieve the package name value.
            is_data_type: Flag indicating whether to retrieve the data type value.
            is_workers: Flag indicating whether to retrieve the number of workers value.
            is_map_addr: Flag indicating whether to retrieve the memory map addresses value.
            is_data_byte: Flag indicating whether to retrieve the data type bytes value.
            is_pid: Flag indicating whether to retrieve the process ID (PID) value.

        Returns:
            The requested variable value.
        """
        variables = {
            is_speed: self._IS_SPEED_MODE,
            is_pkg: self._PKG_NAME,
            is_workers: self._TOTAL_WORKERS,
            is_data_type: self._DATA_TYPES,
            is_map_addr: self._MAPS_ADDR,
            is_data_byte: self._DATA_BYTE,
            is_pid: self._PID
        }

        return variables.get(True, None)
