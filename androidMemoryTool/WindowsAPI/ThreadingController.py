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

from .complex_api_for_all import ComplexApiController
from concurrent.futures import ThreadPoolExecutor


class FastSearchAlgo(object):

    def __init__(self, workers: int = 2):
        super(FastSearchAlgo, self).__init__()
        self._workers = workers
        self.main_controller = ComplexApiController()

    def fast_search_algorithms_value(self, handle, buf: any, string: bool = False,
                                     write_buf=None) -> None:
        if write_buf:
            with ThreadPoolExecutor(max_workers=self._workers) as executor:
                executor.submit(self.main_controller.search_and_write_in_memory, handle, buf, write_buf, string)
        else:
            with ThreadPoolExecutor(max_workers=self._workers) as executor:
                executor.submit(self.main_controller.speed_search_and_read_in_memory, handle, buf)

    def fast_search_algorithms_group_values(self, handle, buf: any, range_val: int, string: bool = False,
                                            write_buf=None) -> None:
        if write_buf:
            with ThreadPoolExecutor(max_workers=self._workers) as executor:
                executor.submit(self.main_controller.speed_group_search_and_write, handle, buf, write_buf, range_val,
                                string)
        else:
            with ThreadPoolExecutor(max_workers=self._workers) as executor:
                executor.submit(self.main_controller.speed_group_search_and_read, handle, buf, range_val)

    def fast_search_algorithms_hex_patterns(self, handle, search_pattern: str, replacement_pattern: str = None) -> None:
        if replacement_pattern:
            with ThreadPoolExecutor(max_workers=self._workers) as executor:
                executor.submit(self.main_controller.speed_find_and_replace_hex_pattern_in_memory, handle,
                                search_pattern, replacement_pattern)
        else:
            with ThreadPoolExecutor(max_workers=self._workers) as executor:
                executor.submit(self.main_controller.speed_find_hex_pattern_in_memory, handle, search_pattern)
