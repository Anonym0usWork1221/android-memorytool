"""
 *  date   : 2022/03/23
 *  Version : 0.4
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

from concurrent.futures.thread import ThreadPoolExecutor

from .DataClasses import DataClasses
from .search_and_writers import SearchAndWrite
from .search_and_readers import SearchAndRead
from .additional_features import AdditionalFeatures


class FastSearchAlgo(DataClasses):
    _SearchAndWriteObject = SearchAndWrite()
    _SearchAndReadObject = SearchAndRead()
    _AdditionalFeaturesObject = AdditionalFeatures()

    def __int__(self):
        super(FastSearchAlgo, self).__int__()

    def fast_search_algorithms_text(self, pid: str, addr: list, read: any, write=None) -> None:
        if write:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._SearchAndWriteObject.speed_search_and_write_text, pid, addr, read, write)

        else:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._SearchAndReadObject.speed_search_and_read_text, pid, addr, read)

    def fast_search_algorithms_value(self, pid: str, addr: list, read: any, buf: int, write=None) -> None:
        if write:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._SearchAndWriteObject.speed_search_and_write, pid, addr, buf, read, write)

        else:
            with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
                executor.submit(self._SearchAndReadObject.speed_search_and_read, pid, addr, buf, read)

    def fast_search_algorithms_pattern_finding(self, pid: str, addr: list, buf: int, hex_pattern: str) -> None:
        with ThreadPoolExecutor(max_workers=super().get_variables(is_workers=True)) as executor:
            executor.submit(self._AdditionalFeaturesObject.speed_find_hexadecimal_pattern, pid, addr, buf, hex_pattern)
