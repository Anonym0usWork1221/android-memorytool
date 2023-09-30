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

from psutil import cpu_count, virtual_memory, Process, NoSuchProcess
from ..errors_class import PIDException
from threading import Event, Thread
from time import sleep, strftime
from os import system
import platform

if platform.system() == "Windows":
    _CLEAR_CMD = "cls"
else:
    _CLEAR_CMD = "clear"


class MemoryProfiler:
    def __init__(self, pid: int, logging_file_path: str = "memory_log.txt") -> None:
        # Private variables
        self._logging_file: str = logging_file_path
        self._break_profile_loop = Event()
        self._pid: int = pid
        self._data = []

        # Accessible variables
        self.highest_memory_usage = self.get_memory_usage()
        self.churn_flag = Event()
        self.leak_flag = Event()
        self.memory_history = []

    def create_data_from_files(self) -> None:
        system_info = self.get_system_info()
        self._data.append({
            'time': strftime("%H:%M:%S"),
            'ram': system_info['RAM'],
            'cores': system_info['Cores'],
            'process_memory': self.get_memory_usage() / (1024 ** 2),
            'leak': "Yes" if self.leak_flag.is_set() else "No",
            'churn': "Yes" if self.churn_flag.is_set() else "No",
            'pid': self._pid
        })

    def clean_current_status_print_string(self) -> str:
        self.create_data_from_files()
        formatted_status_print_header = f"{'Time':<10}{'RAM (GB)':<10}{'Cores':<10}{'Process RSS (MB)':<30}" \
                                        f"{'Memory Leak':<15}{'Memory Churn':<15}{'PID':<6}\n"
        formatted_status_print_string = formatted_status_print_header
        for entry in self._data:
            current_body = f"{entry['time']:<10}{entry['ram']:<10}{entry['cores']:<10}" \
                           f"{entry['process_memory'] / (1024 * 1024):<30}{entry['leak']:<15}" \
                           f"{entry['churn']:<15}{entry['pid']:<6}\n"
            formatted_status_print_string += current_body

        return formatted_status_print_string

    @staticmethod
    def get_system_info() -> dict:
        system_info = {
            'RAM': virtual_memory().total // (1024 ** 3),
            'Cores': cpu_count(logical=False),
        }
        return system_info

    def get_memory_usage(self) -> any:
        try:
            process = Process(self._pid)
            memory_info = process.memory_info()
            memory_usage_bytes = memory_info.rss
            return memory_usage_bytes
        except NoSuchProcess:
            raise PIDException(f"Processes with PID {self._pid} is not running in memory either "
                               f"it crashed or stoped working restart process.")

    def stop_profiling(self) -> None:
        self._break_profile_loop.set()  # Signal the monitoring thread to stop

    def current_memory_data(self, threshold_in_mb: float = 10.0) -> None:
        memory_usage = self.get_memory_usage()
        self.memory_history.append(memory_usage)

        if memory_usage > self.highest_memory_usage + int(threshold_in_mb * 1024.0 * 1024.0):
            self.leak_flag.set()
            self.churn_flag.clear()  # Clear churn flag if leakage occurs
        elif memory_usage > self.highest_memory_usage:
            if not self.leak_flag.is_set():
                self.churn_flag.set()  # Set churn flag if memory usage increases
                self.highest_memory_usage = memory_usage
        else:
            self.leak_flag.clear()
            self.churn_flag.clear()

    def monitor_memory(self, threshold_in_mb: float = 10.0, update_interval_delay: float = 1.0) -> None:
        while not self._break_profile_loop.is_set():
            self.current_memory_data(threshold_in_mb=threshold_in_mb)
            sleep(update_interval_delay)  # Update interval

    def log_memory_data(self) -> None:
        with open(self._logging_file, 'w') as log_file:
            log_file.write(f"{'Time':<10}{'RAM (GB)':<10}"
                           f"{'Cores':<10}{'Process RSS (BYTES)':<40}{'Memory Leak':<15}"
                           f"{'Memory Churn':<15}{'PID':<10}\n")
            for entry in self._data:
                log_file.write(
                    f"{entry['time']:<10}{entry['ram']:<10}"
                    f"{entry['cores']:<10}{entry['process_memory']:<40}{entry['leak']:<15}"
                    f"{entry['churn']:<15}{entry['pid']:<10}\n"
                )

    def get_current_data(self) -> list:
        return self._data

    def start_profiling(self,
                        verbose: bool = True,
                        threshold_in_mb: float = 10.0,
                        update_interval_delay: float = 1.0,
                        logging: bool = True) -> None:
        monitor_thread = Thread(target=self.monitor_memory, args=(threshold_in_mb, update_interval_delay))
        monitor_thread.daemon = True
        monitor_thread.start()

        try:
            while True:
                if logging:
                    self.log_memory_data()
                if verbose:
                    global _CLEAR_CMD
                    system(_CLEAR_CMD)
                    print(self.clean_current_status_print_string())

                sleep(update_interval_delay)
        except KeyboardInterrupt:
            self.stop_profiling()  # Stop thread properly
            self.log_memory_data()


# if __name__ == "__main__":
#     target_pid = int(input("Enter the PID of the process to profile: "))
#     profiler = MemoryProfiler(target_pid)
#     profiler.start_profiling()
