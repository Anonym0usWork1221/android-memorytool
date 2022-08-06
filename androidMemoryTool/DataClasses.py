"""
 *  @date   : 2022/03/23
 *  Version : 0.1
 *  @author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

import struct
import sys
import os
from dataclasses import dataclass
from .mapping import *

PKG_NAME = ""
DATA_TYPES = ""
IS_SPEED_MODE = False
TOTAL_WORKERS = 55

MAPS_ADDR = []
DATA_BYTE = 0
PID = ""


def get_pid(pkg: str) -> str:
    pid_id = None
    # print(proc_id)
    try:
        pid_id = os.popen("pidof {}".format(pkg))
    except Exception as e:
        print("[*]Exception ", e)

    pid_decode = pid_id.read()
    if pid_decode is not None:
        pid = pid_decode.replace("\n", "")
        return str(pid)
    else:
        return ""


@dataclass()
class DataTypes:
    DWORD: str = "DWORD"
    FLOAT: str = "FLOAT"
    DOUBLE: str = "DOUBLE"
    WORD: str = "WORD"
    BYTE: str = "BYTE"
    QWORD: str = "QWORD"
    XOR: str = "XOR"
    UTF_8: str = "UTF-8"
    UTF_16LE: str = "UTF-16LE"


class SettingUpTool:
    @staticmethod
    def init_setup(PKG, TYPE=DataTypes.DWORD, SPEED_MODE=False, WORKERS=55):
        global DATA_TYPES, PKG_NAME, IS_SPEED_MODE, TOTAL_WORKERS
        DATA_TYPES = TYPE
        PKG_NAME = PKG
        IS_SPEED_MODE = SPEED_MODE
        TOTAL_WORKERS = WORKERS


@dataclass()
class PMAP:
    ALL: bool = True
    B_BAD: bool = False
    C_ALLOC: bool = False
    C_BSS: bool = False
    C_DATA: bool = False
    C_HEAP: bool = False
    JAVA_HEAP: bool = False
    A_ANONYMOUS: bool = False
    CODE_SYSTEM: bool = False
    STACK: bool = False
    ASHMEM: bool = False
    J_Java: bool = False
    CODE_APP: bool = False
    V_video: bool = False


def IdentifyDict(P=PMAP()):
    global PKG_NAME
    wanted_ranges = [k for k, v in P.__dict__.items() if v == True]
    address = []

    for i in wanted_ranges:
        if i == "ALL":
            address = mappingALL(get_pid(PKG_NAME))["address"]
            return address
        elif i == "B_BAD":
            address.extend(mappingB(get_pid(PKG_NAME))["address"])
        elif i == "C_ALLOC":
            address.extend(mappingCA(get_pid(PKG_NAME))["address"])
        elif i == "C_BSS":
            address.extend(mappingCB(get_pid(PKG_NAME))["address"])
        elif i == "C_DATA":
            address.extend(mappingCD(get_pid(PKG_NAME))["address"])
        elif i == "C_HEAP":
            address.extend(mappingCH(get_pid(PKG_NAME))["address"])
        elif i == "JAVA_HEAP":
            address.extend(mappingJH(get_pid(PKG_NAME))["address"])
        elif i == "A_ANONYMOUS":
            address.extend(mappingA(get_pid(PKG_NAME))["address"])
        elif i == "CODE_SYSTEM":
            address.extend(mappingXS(get_pid(PKG_NAME))["address"])
        elif i == "STACK":
            address.extend(mappingS(get_pid(PKG_NAME))["address"])
        elif i == "ASHMEM":
            address.extend(mappingAS(get_pid(PKG_NAME))["address"])
        elif i == "J_Java":
            address.extend(mappingJ(get_pid(PKG_NAME))["address"])
        elif i == "CODE_APP":
            address.extend(mappingXA(get_pid(PKG_NAME))["address"])
        elif i == "V_video":
            address.extend(mappingV(get_pid(PKG_NAME))["address"])
    return address


def DataTypeEncoding(read, write=None):
    global DATA_TYPES
    if DATA_TYPES == "DWORD":
        if write:
            if sys.byteorder == 'little':
                search_value = struct.pack('<i', read)
                replace_value = struct.pack('<i', write)
            else:
                search_value = struct.pack('>i', read)
                replace_value = struct.pack('>i', write)

            return search_value, replace_value

        else:
            if sys.byteorder == 'little':
                search_value = struct.pack('<i', read)
            else:
                search_value = struct.pack('>i', read)
            return search_value

    elif DATA_TYPES == "FLOAT":
        if write:
            if sys.byteorder == 'little':
                search_value = struct.pack('<f', read)
                replace_value = struct.pack('<f', write)
            else:
                search_value = struct.pack('>f', read)
                replace_value = struct.pack('>f', write)

            return search_value, replace_value

        else:
            if sys.byteorder == 'little':
                search_value = struct.pack('<f', read)
            else:
                search_value = struct.pack('>f', read)
            return search_value

    elif DATA_TYPES == "DOUBLE":
        if write:
            if sys.byteorder == 'little':
                search_value = struct.pack('<d', read)
                replace_value = struct.pack('<d', write)
            else:
                search_value = struct.pack('>d', read)
                replace_value = struct.pack('>d', write)

            return search_value, replace_value

        else:
            if sys.byteorder == 'little':
                search_value = struct.pack('<d', read)
            else:
                search_value = struct.pack('>d', read)
            return search_value

    elif DATA_TYPES == "WORD":
        if write:
            if sys.byteorder == 'little':
                search_value = struct.pack('<h', read)
                replace_value = struct.pack('<h', write)
            else:
                search_value = struct.pack('>h', read)
                replace_value = struct.pack('>h', write)

            return search_value, replace_value

        else:
            if sys.byteorder == 'little':
                search_value = struct.pack('<i', read)
            else:
                search_value = struct.pack('>i', read)
            return search_value

    elif DATA_TYPES == "BYTE":
        if write:
            if sys.byteorder == 'little':
                search_value = struct.pack('<b', read)
                replace_value = struct.pack('<b', write)
            else:
                search_value = struct.pack('>b', read)
                replace_value = struct.pack('>b', write)

            return search_value, replace_value

        else:
            if sys.byteorder == 'little':
                search_value = struct.pack('<b', read)
            else:
                search_value = struct.pack('>b', read)
            return search_value

    elif DATA_TYPES == "QWORD":
        if write:
            if sys.byteorder == 'little':
                search_value = struct.pack('<q', read)
                replace_value = struct.pack('<q', write)
            else:
                search_value = struct.pack('>q', read)
                replace_value = struct.pack('>q', write)

            return search_value, replace_value

        else:
            if sys.byteorder == 'little':
                search_value = struct.pack('<q', read)
            else:
                search_value = struct.pack('>q', read)
            return search_value

    elif DATA_TYPES == "XOR":
        if write:
            if sys.byteorder == 'little':
                search_value = struct.pack('<l', read)
                replace_value = struct.pack('<l', write)
            else:
                search_value = struct.pack('>l', read)
                replace_value = struct.pack('>l', write)

            return search_value, replace_value

        else:
            if sys.byteorder == 'little':
                search_value = struct.pack('<l', read)
            else:
                search_value = struct.pack('>l', read)
            return search_value

    elif DATA_TYPES == "UTF-8":
        if write:
            search_value = read.encode('utf-8')
            replace_value = write.encode('utf-8')

            return search_value, replace_value

        else:
            search_value = read.encode('utf-8')
            return search_value

    elif DATA_TYPES == "UTF-16LE":
        if write:
            search_value = read.encode('utf-16LE')
            replace_value = write.encode('utf-16LE')

            return search_value, replace_value

        else:
            search_value = read.encode('utf-16LE')
            return search_value

    else:
        return None


def DataTypeBytes() -> int:
    global DATA_TYPES
    if DATA_TYPES == "DWORD":
        return 4

    elif DATA_TYPES == "FLOAT":
        return 4

    elif DATA_TYPES == "DOUBLE":
        return 8

    elif DATA_TYPES == "WORD":
        return 2

    elif DATA_TYPES == "BYTE":
        return 1

    elif DATA_TYPES == "QWORD":
        return 8

    elif DATA_TYPES == "XOR":
        return 4

    elif DATA_TYPES == "UTF-8":
        return 0

    elif DATA_TYPES == "UTF-16LE":
        return 0

    else:
        return -1


class InitMemoryTool:
    @staticmethod
    def init_tool(pMAP=PMAP()):
        global PKG_NAME, MAPS_ADDR, DATA_BYTE, PID
        MAPS_ADDR = IdentifyDict(pMAP)
        DATA_BYTE = DataTypeBytes()
        PID = get_pid(PKG_NAME)


def get_variables(is_speed=False, is_pkg=False, is_data_type=False, is_workers=False, is_map_addr=False,
                  is_data_byte=False, is_pid=False):
    global IS_SPEED_MODE, PKG_NAME, DATA_TYPES, TOTAL_WORKERS, MAPS_ADDR, DATA_BYTE, PID
    if is_speed:
        return IS_SPEED_MODE
    elif is_pkg:
        return PKG_NAME
    elif is_workers:
        return TOTAL_WORKERS
    elif is_data_type:
        return DATA_TYPES
    elif is_map_addr:
        return MAPS_ADDR
    elif is_data_byte:
        return DATA_BYTE
    elif is_pid:
        return PID
    else:
        return None
