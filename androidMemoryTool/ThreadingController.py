"""
 *  @date   : 2022/03/23
 *  Version : 0.1
 *  @author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

from concurrent.futures.thread import ThreadPoolExecutor

from .DataClasses import get_variables
from .search_and_writers import speed_search_and_write, speed_search_and_write_text
from .search_and_readers import speed_search_and_read, speed_search_and_read_text

total_threads = []


def fast_search_algorithms_text(PID: str, addr: list, read: any, write=None):
    if write:
        with ThreadPoolExecutor(max_workers=get_variables(is_workers=True)) as executor:
            executor.submit(speed_search_and_write_text, PID, addr, read, write)

    else:
        with ThreadPoolExecutor(max_workers=get_variables(is_workers=True)) as executor:
            executor.submit(speed_search_and_read_text, PID, addr, read)


def fast_search_algorithms_value(PID: str, addr: list, read: any, buf: int, write=None):
    if write:
        with ThreadPoolExecutor(max_workers=get_variables(is_workers=True)) as executor:
            executor.submit(speed_search_and_write, PID, addr, buf, read, write)

    else:
        with ThreadPoolExecutor(max_workers=get_variables(is_workers=True)) as executor:
            executor.submit(speed_search_and_read, PID, addr, buf, read)
