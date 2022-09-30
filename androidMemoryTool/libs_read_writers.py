"""
 *  date   : 2022/03/23
 *  Version : 0.3
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""


# ! /usr/bin/env python

class LibsControllers:

    @staticmethod
    def write_lib_offsets(pid: str, base_address: hex, offset: hex, value: any) -> bool:
        write_address = int(str(base_address), 16) + int(str(offset), 16)
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        try:
            mem_file.seek(write_address)
            mem_file.write(value)
            mem_file.close()
            return True
        except Exception as e:
            print("[*] Exception ", e)
        return False

    @staticmethod
    def read_lib_offsets(pid: str, base_address: hex, offset: hex, buf: int) -> any:
        read_address = int(str(base_address), 16) + int(str(offset), 16)
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        try:
            mem_file.seek(read_address)
            value = mem_file.read(buf)
            mem_file.close()
            return value
        except Exception as e:
            print("[*] Exception ", e)
        return None

    def address_refiners(self, pid: str, list_address: list, buf: int, changed_value: any) -> any:
        refined_address = []
        for address in list_address:
            read_value = self.read_lib_offsets(pid, 0x0, address, buf)
            if read_value == changed_value:
                refined_address.append(address)

        return refined_address

    @staticmethod
    def raw_dumper(pid: str, address: list) -> bytes:
        start_addr = int(address[0][0], 16)
        end_addr = int(address[len(address) - 1][1], 16)
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        mem_file.seek(start_addr)
        total_bytes = end_addr - start_addr
        byte_strings = mem_file.read(total_bytes)
        return byte_strings
