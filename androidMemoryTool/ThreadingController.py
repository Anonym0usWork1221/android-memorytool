"""
 *  date   : 2023/07/11
 *  Version : 0.5
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

from .additional_features import AdditionalFeatures
from .search_and_writers import SearchAndWrite
from .search_and_readers import SearchAndRead
from .DataClasses import DataClasses
from concurrent.futures import ThreadPoolExecutor


class FastSearchAlgo(DataClasses):
    """A class that implements fast search algorithms for text, values, and pattern finding."""

    _SearchAndWriteObject = SearchAndWrite()
    _SearchAndReadObject = SearchAndRead()
    _AdditionalFeaturesObject = AdditionalFeatures()

    def __init__(self):
        super(FastSearchAlgo, self).__init__()

    def fast_search_algorithms_text(self, pid: str, addr: list, read: any, write=None) -> None:
        """
        Performs a fast search for text in the specified memory address range of a process.

            Args:
                pid (str): The process ID.
                addr (list): A list of memory addresses to search in.
                read (any): The text to search for.
                write (Optional): The replacement text for writing to memory (default: None).

            Returns:
                None
        """
        if write:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._SearchAndWriteObject.speed_search_and_write_text, pid, addr, read, write)
        else:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._SearchAndReadObject.speed_search_and_read_text, pid, addr, read)

    def fast_search_algorithms_value(self, pid: str, addr: list, read: any, buf: int, write=None) -> None:
        """
        Performs a fast search for values in the specified memory address range of a process.

            Args:
                pid (str): The process ID.
                addr (list): A list of memory addresses to search in.
                read (any): The value to search for.
                buf (int): The buffer size for reading memory.
                write (Optional): The replacement value for writing to memory (default: None).

            Returns:
                None
        """
        if write:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._SearchAndWriteObject.speed_search_and_write, pid, addr, buf, read, write)
        else:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._SearchAndReadObject.speed_search_and_read, pid, addr, buf, read)

    def fast_search_algorithms_pattern_finding(self, pid: str, addr: list, buf: int, hex_pattern: str,
                                               replace_pattern: str = None) -> None:
        """
            Executes fast search algorithms for finding a hexadecimal pattern in memory addresses.

            Args:
                pid (str): The process ID.
                addr (list): The list of memory addresses to search.
                buf (int): The buffer size for reading memory.
                hex_pattern (str): The hexadecimal pattern to search for.
                replace_pattern (str, optional): The hexadecimal pattern to replace the found pattern with.
                 Defaults to None.

            Returns:
                None.
        """

        if replace_pattern:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._AdditionalFeaturesObject.speed_find_and_replace_hexadecimal_pattern, pid,
                                addr, buf, hex_pattern, replace_pattern)
        else:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._AdditionalFeaturesObject.speed_find_hexadecimal_pattern, pid,
                                addr, buf, hex_pattern)
