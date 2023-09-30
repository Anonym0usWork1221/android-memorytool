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
class LibsControllers:
    """
    Class for controlling memory operations on a process.

    Methods:
        write_lib_offsets(pid: str, base_address: str, offset: str, value: any) -> bool:
            Writes a value to a specific memory address in the memory of a process.

        read_lib_offsets(pid: str, base_address: str, offset: str, buf: int) -> any:
            Reads the value from a specific memory address in the memory of a process.

        address_refiners(pid: str, list_address: list, buf: int, changed_value: any) -> list:
            Refines a list of memory addresses by checking if the value at each address matches a specified value.

        raw_dumper(pid: str, address: list) -> bytes:
            Dumps a range of memory addresses from a process.
    """

    def __init__(self):
        pass

    @staticmethod
    def write_lib_offsets(pid: str, base_address: str, offset: str, value: any) -> bool:
        """
            Writes a value to a specific memory address in the memory of a process.

            Args:
                pid (str): The process ID.
                base_address (str): The base memory address in hexadecimal format.
                offset (str): The offset from the base address in hexadecimal format.
                value (any): The value to be written to the memory address.

            Returns:
                bool: True if the write operation is successful, False otherwise.
        """

        write_address = int(base_address, 16) + int(offset, 16)
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        try:
            mem_file.seek(write_address)
            mem_file.write(value)
            mem_file.close()
            return True
        except IOError as e:
            if not isinstance(base_address, str) or not isinstance(offset, str):
                print(f"[-] Exception: {e}\n[-] This error mostly occur due to invalid type of parameters,"
                      f" pass the base_address and offset as a hex string e.g: '0x5645c973ad44'")
        return False

    @staticmethod
    def read_lib_offsets(pid: str, base_address: str, offset: str, buf: int) -> any:
        """
            Reads the value from a specific memory address in the memory of a process.

            Args:
                pid (str): The process ID.
                base_address (str): The base memory address in hexadecimal format.
                offset (str): The offset from the base address in hexadecimal format.
                buf (int): The number of bytes to read from the memory address.

            Returns:
                any: The value read from the memory address.
        """

        read_address = int(base_address, 16) + int(offset, 16)
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        try:
            mem_file.seek(read_address)
            founded_value_on_address = mem_file.read(buf)
            mem_file.close()
            return founded_value_on_address
        except IOError as e:
            if not isinstance(base_address, str) or not isinstance(offset, str):
                print(f"[-] Exception: {e}\n[-] This error mostly occur due to invalid type of parameters,"
                      f" pass the base_address and offset as a hex string e.g: '0x5645c973ad44'")
        return None

    def address_refiners(self, pid: str, list_address: list, buf: int, changed_value: any) -> list:
        """
            Refines a list of memory addresses by checking if the value at each address matches a specified value.

            Args:
                pid (str): The process ID.
                list_address (list): List of memory addresses to be refined.
                buf (int): The number of bytes to read from each memory address.
                changed_value (any): The value to compare against the read values.

            Returns:
                list: List of refined memory addresses where the read value matches the changed value.
        """

        refined_address = []
        for address in list_address:
            read_value = self.read_lib_offsets(pid, '0x0', address, buf)
            if read_value == changed_value:
                refined_address.append(address)
        return refined_address

    @staticmethod
    def raw_dumper(pid: str, address: list) -> bytes:
        """
            Dumps a range of memory addresses from a process.

            Args:
                pid (str): The process ID.
                address (list): List of memory address ranges to dump.

            Returns:
                bytes: The dumped bytes from the specified memory address range.
        """

        start_addr = int(address[0][0], 16)
        end_addr = int(address[len(address) - 1][1], 16)
        mem_file = open(f"/proc/{pid}/mem", "rb+")
        mem_file.seek(start_addr)
        total_bytes = end_addr - start_addr
        byte_strings = mem_file.read(total_bytes)
        return byte_strings
