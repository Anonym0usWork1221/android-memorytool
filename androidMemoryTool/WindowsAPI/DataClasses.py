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

from ..errors_class import PIDException
from dataclasses import dataclass
import ctypes
import psutil


class DataClasses:

    @dataclass()
    class DataTypes(object):
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

    def __init__(self):
        """
           Initialize a new instance of the SearchAndRead class.
           This constructor does not take any parameters.
        """
        ...

    @staticmethod
    def get_pid(pkg: any((str, int))) -> int:
        """
        Retrieves the process ID (PID) for the given package name or PID.
        Args:
            pkg (str or int): The package name or PID.
        Returns:
            int: The process ID (PID).
        Raises:
            PIDException: If the process is not running in memory or if an error occurs during retrieval.
        """

        pkg = str(pkg)
        if pkg.isnumeric():  # If the input is already a PID
            pid = int(pkg)
            if psutil.pid_exists(pid):
                return int(pid)
            else:
                raise PIDException("Process is not running in memory. Try to restart the process and script.")
        else:  # If the input is a package name
            try:
                for proc in psutil.process_iter(attrs=['pid', 'name']):
                    if pkg.lower() in proc.info['name'].lower():
                        return int(proc.info['pid'])
                raise PIDException("Process is not running in memory. Try to restart the process and script.")
            except Exception:
                raise PIDException("Error occurred while retrieving PID for the process.")

    @staticmethod
    def data_type_buffer(data_type: str, read_value: any = None,
                         write: any = None, read_string: str = "", write_string: str = ""):
        """
        Create ctypes buffer objects for the specified data type.

        Args:
            data_type (str): The data type for which to create a buffer.
            write (any): Optional. The value to be used for creating the write buffer if provided.
            read_string (str): Optional. The string value to be used for creating the read buffer if provided.
            write_string (str): Optional. The string value to be used for creating the write buffer if provided.

        Returns:
            ctypes.Array: The read and write buffer objects.

        Raises:
            ValueError: If an unsupported data type is provided.
        """

        if data_type == "DWORD":
            if write:
                if read_value:
                    read_buffer = ctypes.c_int32(read_value)
                else:
                    read_buffer = ctypes.c_int32()
                write_buffer = ctypes.c_int32(write)
                return read_buffer, write_buffer
            if read_value:
                return ctypes.c_int32(read_value)
            return ctypes.c_int32()
        elif data_type == "FLOAT":
            if write:
                if read_value:
                    read_buffer = ctypes.c_float(read_value)
                else:
                    read_buffer = ctypes.c_float()
                write_buffer = ctypes.c_float(write)
                return read_buffer, write_buffer
            if read_value:
                return ctypes.c_float(read_value)
            return ctypes.c_float()
        elif data_type == "DOUBLE":
            if write:
                if read_value:
                    read_buffer = ctypes.c_double(read_value)
                else:
                    read_buffer = ctypes.c_double()
                write_buffer = ctypes.c_double(write)
                return read_buffer, write_buffer
            if read_value:
                return ctypes.c_double(read_value)
            return ctypes.c_double()
        elif data_type == "WORD":
            if write:
                if read_value:
                    read_buffer = ctypes.c_short(read_value)
                else:
                    read_buffer = ctypes.c_short()
                write_buffer = ctypes.c_short(write)
                return read_buffer, write_buffer
            if read_value:
                return ctypes.c_short(read_value)
            return ctypes.c_short()
        elif data_type == "BYTE":
            if write:
                if read_value:
                    read_buffer = ctypes.c_byte(read_value)
                else:
                    read_buffer = ctypes.c_byte()
                write_buffer = ctypes.c_byte(write)
                return read_buffer, write_buffer
            if read_value:
                return ctypes.c_byte(read_value)
            return ctypes.c_byte()
        elif data_type == "QWORD":
            if write:
                if read_value:
                    read_buffer = ctypes.c_longlong(read_value)
                else:
                    read_buffer = ctypes.c_longlong()
                write_buffer = ctypes.c_longlong(write)
                return read_buffer, write_buffer
            if read_value:
                return ctypes.c_longlong(read_value)
            return ctypes.c_longlong()
        elif data_type == "XOR":
            if write:
                if read_value:
                    read_buffer = ctypes.c_long(read_value)
                else:
                    read_buffer = ctypes.c_long()
                write_buffer = ctypes.c_long(write)
                return read_buffer, write_buffer
            if read_value:
                return ctypes.c_long(read_value)  # Signed long (XOR)
            return ctypes.c_long()
        elif data_type == "UTF-8":
            if write_string:
                read_buffer = ctypes.create_string_buffer(read_string.encode('utf-8'))
                write_buffer = ctypes.create_string_buffer(write_string.encode('utf-8'))
                return read_buffer, write_buffer
            return ctypes.create_string_buffer(read_string.encode('utf-8'))
        elif data_type == "UTF-16LE":
            if write_string:
                read_buffer = ctypes.create_unicode_buffer(read_string)
                write_buffer = ctypes.create_unicode_buffer(write_string)
                return read_buffer, write_buffer
            return ctypes.create_unicode_buffer(read_string)
        else:
            raise ValueError(f"Unsupported data type: {data_type}")
