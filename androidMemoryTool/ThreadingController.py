"""
 *  date   : 2022/03/23
 *  Version : 0.3
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

from concurrent.futures.thread import ThreadPoolExecutor

from .DataClasses import DataClasses
from .search_and_writers import SearchAndWrite
from .search_and_readers import SearchAndRead

total_threads = []


class FastSearchAlgo(DataClasses):
    _SearchAndWriteObject = SearchAndWrite()
    _SearchAndReadObject = SearchAndRead()

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
