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

"""
Mapping Structure:

The mapping structure provides information about the memory regions allocated to a process, including their 
permissions, offsets, devices, inodes, and pathnames.

Mapping Format:
    [address] [perms] [offset] [device] [inode] [pathname]

Mapping Fields:
    - address: The range of memory addresses covered by the mapping.
    - perms: The permissions of the memory region (e.g., read, write, execute).
    - offset: The offset of the mapping.
    - device: The device associated with the mapping.
    - inode: The inode of the file associated with the mapping (if applicable).
    - pathname: The pathname of the file associated with the mapping (if applicable).

Mapping Tags:
    - O->others:others: Anonymous mappings without specific tags (e.g., --p, anon, system/framework, etc.).
    - Jh->:rw-p, anon:dalvik-main space: Dalvik heap mappings in the Java space.
    - Xs->system: --xp, lib, .so, system: System libraries and shared objects mappings.
    - J->Java: rw-p, javalib: Java library mappings.
    - ch -> c++heap: C++ heap mappings.
    - ca -> c++ alloc: Anonymous C++ allocations mappings.
    - cd -> c++ data: C++ data mappings.
    - cb -> c++ bss: C++ BSS (Block Started by Symbol) mappings.
    - PS -> PPSSPP: PPSSPP emulator mappings.
    - A -> Anonymous: Anonymous mappings with read-write permissions only.
    - S -> Stack: Stack mappings.
    - As -> Ashmem: Ashmem (Anonymous Shared Memory) mappings.
    - V -> Video: Video mappings.
    - B -> Bad(dang): Bad or dangerous mappings.
    - Xa -> code app:r-xp, lib, .so, .jar: Application code mappings (read-executable).
    
Order of Fields in map.txt:
    ['address', 'perms', 'offset', 'device', 'inode', 'pathname']
    
Example:
    ['76a01ae000-76a01af000', 'r--p', '00000000', '00:00', '26', '[anon:atexit handler]']
    
    The mapping above represents an anonymous mapping with read-only permissions, no offset, device '00:00',
     inode '26', and no associated file pathname.

"""

# order
'''
         address          perms     offset    device   inode        pathname
            0               1         2          3       4              5
['76a01ae000-76a01af000', 'r--p', '00000000', '00:00', '26', '[anon:atexit handler]']

A -> 4[]
'''


# ! /usr/bin/env python
class Mapping:
    """Class for extracting memory mappings of a process using /proc/[pid]/maps file."""

    def __init__(self):
        pass

    @staticmethod
    def _read_map_file(pid: str):
        """
        Reads the mapping file for the specified process ID (pid).
            Args:
                pid (str): The process ID.

            Returns:
                list: A list of strings representing the lines read from the mapping file.
        """

        with open(f"/proc/{pid}/maps", "r") as map_file:
            return map_file.readlines()

    @staticmethod
    def _parse_mapping_line(line: str):
        """
        Parses a mapping line and extracts relevant information.
            Args:
                line (str): A line from the mapping file.

            Returns:
                tuple: A tuple containing temporary details, region, and permissions extracted from the line.
        """
        temp_details = line.split(" ", 5)
        region = temp_details[-1]
        perm = temp_details[1]
        return temp_details, region, perm

    @staticmethod
    def _filter_mappings(lines: list, condition: callable):
        """
        Filters the mappings based on a given condition.
            Args:
                lines (list): A list of strings representing the lines read from the mapping file.
                condition (callable): A lambda function that takes temporary details, region, and permissions as input
                           and returns True or False based on the condition.

            Returns:
                dict: A dictionary containing filtered mapping details with keys 'address', 'permissions',
                      and 'allocated'.
        """

        details = {"address": [], "permissions": [], "allocated": []}
        for line in lines:
            temp_details, region, perm = Mapping._parse_mapping_line(line)
            if condition(temp_details, region, perm):
                details["address"].append(temp_details[0])
                details["permissions"].append(temp_details[1])
                details["allocated"].append(region)
        return details

    @staticmethod
    def mapping_xa(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to libraries in the system.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for libraries with specific conditions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: \
            ("lib" in region) and ("rw" in perm) and (".so" in region) and ("system" in region)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_dump_libs(pid: str, lib_name: str) -> list:
        """
        Returns the addresses of pages belonging to a specific library in the process.

            Args:
                pid (str): The process ID.
                lib_name (str): The name of the library.

            Returns:
                list: A list of addresses belonging to the specified library.
        """

        lines = Mapping._read_map_file(pid)
        address = []
        for line in lines:
            page = line.split()
            module = page[-1]
            if lib_name in module:
                address.append(page[0].split('-'))
        return address

    @staticmethod
    def mapping_ca(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to libc_malloc and anonymous regions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for libc_malloc and anonymous regions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: \
            ("anon" in region) and ("rw" in perm) and ("libc_malloc" in region)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_a(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to regions with fewer than 46 details and
        read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for regions with specific conditions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: (len(temp_details) < 46) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_b(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to regions containing 'fonts' in the name
        and read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for regions with specific conditions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: ("fonts" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_cb(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to the '[anon:.bss]' region and
        read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for the specified region.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: ("[anon:.bss]" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_cd(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to regions starting with '/data/app/' and
        read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for the specified regions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: ("/data/app/" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_ch(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to the '[heap]' region and
        read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for the specified region.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: ("[heap]" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_jh(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to regions starting with '/dev/ashmem/' and
        read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for the specified regions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: ("/dev/ashmem/" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_xs(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to regions starting with '/system' and
        read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for the specified regions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: ("/system" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_s(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to the '[stack]' region and
        read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for the specified region.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: ("[stack]" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_as(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to regions starting with '/dev/ashmem/' and
        containing 'dalvik' in the name and read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for the specified regions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: \
            ("/dev/ashmem/" in region and "dalvik" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_j(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to regions containing 'javalib' and
        'dalvik' in the name and read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for the specified regions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: \
            ("javalib" in region and "dalvik" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_v(pid: str) -> dict:
        """
        Returns the mappings with specific conditions related to regions containing 'kgsl-3d0' in the name
        and read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing mapping details for the specified regions.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: ("kgsl-3d0" in region) and ("rw" in perm)
        return Mapping._filter_mappings(lines, condition)

    @staticmethod
    def mapping_all(pid: str) -> dict:
        """
        Returns all the mappings with read-write permissions.

            Args:
                pid (str): The process ID.

            Returns:
                dict: A dictionary containing all mapping details with keys 'address', 'permissions',
                      and 'allocated'.
        """

        lines = Mapping._read_map_file(pid)
        condition = lambda temp_details, region, perm: "rw" in perm
        return Mapping._filter_mappings(lines, condition)


# if __name__ == '__main__':
#     print(Mapping().mapping_a(pid="9628"))
