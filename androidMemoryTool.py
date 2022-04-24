"""
 *  @date   : 2022/03/23
 *  @author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

 MIT License

 Copyright (c) 2022 AbdulMoez (abdulmoez123456789@gmail.com)

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NON INFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.
"""

# ! /usr/bin/env python
import os
from mapping import *
from search_and_writers import *
from libsDirectWriter import *
from libsDirectRead import *
from search_and_readers import *


# getting pids
def get_pid(pkg: str) -> str:
    pid_id = None
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


# Float Writers

def write_float_xa(PID: str, read: float, write: float) -> int:
    details_xa = mappingXA(PID)
    return search_and_write_float_XA(PID, details_xa, read, write)


def write_float_ca(PID: str, read: float, write: float) -> int:
    details_ca = mappingCA(PID)
    return search_and_write_float_CA(PID, details_ca, read, write)


def write_float_a(PID: str, read: float, write: float) -> int:
    details_a = mappingA(PID)
    return search_and_write_float_A(PID, details_a, read, write)


def write_float_all(PID: str, read: float, write: float) -> int:
    details_all = mappingALL(PID)
    return search_and_write_float_ALL(PID, details_all, read, write)


# Double Writers

def write_double_xa(PID: str, read: float, write: float) -> int:
    details_xa = mappingXA(PID)
    return search_and_write_double_XA(PID, details_xa, read, write)


def write_double_ca(PID: str, read: float, write: float) -> int:
    details_ca = mappingCA(PID)
    return search_and_write_double_CA(PID, details_ca, read, write)


def write_double_a(PID: str, read: float, write: float) -> int:
    details_a = mappingA(PID)
    return search_and_write_double_A(PID, details_a, read, write)


def write_double_all(PID: str, read: float, write: float) -> int:
    details_all = mappingALL(PID)
    return search_and_write_double_ALL(PID, details_all, read, write)


# Dword Writers

def write_dword_xa(PID: str, read: int, write: int) -> int:
    details_xa = mappingXA(PID)
    return search_and_write_dword_XA(PID, details_xa, read, write)


def write_dword_ca(PID: str, read: int, write: int) -> int:
    details_ca = mappingCA(PID)
    return search_and_write_dword_CA(PID, details_ca, read, write)


def write_dword_a(PID: str, read: int, write: int) -> int:
    details_a = mappingA(PID)
    return search_and_write_dword_A(PID, details_a, read, write)


def write_dword_all(PID: str, read: int, write: int) -> int:
    details_all = mappingALL(PID)
    return search_and_write_dword_ALL(PID, details_all, read, write)


# UTF-8 Writers

def write_utf8_xa(PID: str, read: str, write: str) -> int:
    details_xa = mappingXA(PID)
    return search_and_write_utf8_XA(PID, details_xa, read, write)


def write_utf8_ca(PID: str, read: str, write: str) -> int:
    details_ca = mappingCA(PID)
    return search_and_write_utf8_CA(PID, details_ca, read, write)


def write_utf8_a(PID: str, read: str, write: str) -> int:
    details_a = mappingA(PID)
    return search_and_write_utf8_A(PID, details_a, read, write)


def write_utf8_all(PID: str, read: str, write: str) -> int:
    details_all = mappingALL(PID)
    return search_and_write_utf8_ALL(PID, details_all, read, write)


# UTF-16LE Writers

def write_utf16le_xa(PID: str, read: str, write: str) -> int:
    details_xa = mappingXA(PID)
    return search_and_write_utf16LE_XA(PID, details_xa, read, write)


def write_utf16le_ca(PID: str, read: str, write: str) -> int:
    details_ca = mappingCA(PID)
    return search_and_write_utf16LE_CA(PID, details_ca, read, write)


def write_utf16le_a(PID: str, read: str, write: str) -> int:
    details_a = mappingA(PID)
    return search_and_write_utf16LE_A(PID, details_a, read, write)


def write_utf16le_all(PID: str, read: str, write: str) -> int:
    details_all = mappingALL(PID)
    return search_and_write_utf16LE_ALL(PID, details_all, read, write)


# Qword Writers

def write_qword_xa(PID: str, read: int, write: int) -> int:
    details_xa = mappingXA(PID)
    return search_and_write_qword_XA(PID, details_xa, read, write)


def write_qword_ca(PID: str, read: int, write: int) -> int:
    details_ca = mappingCA(PID)
    return search_and_write_qword_CA(PID, details_ca, read, write)


def write_qword_a(PID: str, read: int, write: int) -> int:
    details_a = mappingA(PID)
    return search_and_write_qword_A(PID, details_a, read, write)


def write_qword_all(PID: str, read: int, write: int) -> int:
    details_all = mappingALL(PID)
    return search_and_write_qword_ALL(PID, details_all, read, write)


# Word Writers

def write_word_xa(PID: str, read: int, write: int) -> int:
    details_xa = mappingXA(PID)
    return search_and_write_word_XA(PID, details_xa, read, write)


def write_word_ca(PID: str, read: int, write: int) -> int:
    details_ca = mappingCA(PID)
    return search_and_write_word_CA(PID, details_ca, read, write)


def write_word_a(PID: str, read: int, write: int) -> int:
    details_a = mappingA(PID)
    return search_and_write_word_A(PID, details_a, read, write)


def write_word_all(PID: str, read: int, write: int) -> int:
    details_all = mappingALL(PID)
    return search_and_write_word_ALL(PID, details_all, read, write)


# Byte Writers

def write_byte_xa(PID: str, read: int, write: int) -> int:
    details_xa = mappingXA(PID)
    return search_and_write_byte_XA(PID, details_xa, read, write)


def write_byte_ca(PID: str, read: int, write: int) -> int:
    details_ca = mappingCA(PID)
    return search_and_write_byte_CA(PID, details_ca, read, write)


def write_byte_a(PID: str, read: int, write: int) -> int:
    details_a = mappingA(PID)
    return search_and_write_byte_A(PID, details_a, read, write)


def write_byte_all(PID: str, read: int, write: int) -> int:
    details_all = mappingALL(PID)
    return search_and_write_byte_ALL(PID, details_all, read, write)


# Xor Writers

def write_xor_xa(PID: str, read: int, write: int) -> int:
    details_xa = mappingXA(PID)
    return search_and_write_xor_XA(PID, details_xa, read, write)


def write_xor_ca(PID: str, read: int, write: int) -> int:
    details_ca = mappingCA(PID)
    return search_and_write_xor_CA(PID, details_ca, read, write)


def write_xor_a(PID: str, read: int, write: int) -> int:
    details_a = mappingA(PID)
    return search_and_write_xor_A(PID, details_a, read, write)


def write_xor_all(PID: str, read: int, write: int) -> int:
    details_all = mappingALL(PID)
    return search_and_write_xor_ALL(PID, details_all, read, write)


""" ################################################################################################## """
"""                                 Readers Block                          """


# Float Readers

def read_float_xa(PID: str, read: float) -> tuple[list, int]:
    details_xa = mappingXA(PID)
    return search_and_read_float_XA(PID, details_xa, read)


def read_float_ca(PID: str, read: float) -> tuple[list, int]:
    details_ca = mappingCA(PID)
    return search_and_read_float_CA(PID, details_ca, read)


def read_float_a(PID: str, read: float) -> tuple[list, int]:
    details_a = mappingA(PID)
    return search_and_read_float_A(PID, details_a, read)


def read_float_all(PID: str, read: float) -> tuple[list, int]:
    details_all = mappingALL(PID)
    return search_and_read_float_ALL(PID, details_all, read)


# Double Readers

def read_double_xa(PID: str, read: float) -> tuple[list, int]:
    details_xa = mappingXA(PID)
    return search_and_read_double_XA(PID, details_xa, read)


def read_double_ca(PID: str, read: float) -> tuple[list, int]:
    details_ca = mappingCA(PID)
    return search_and_read_double_CA(PID, details_ca, read)


def read_double_a(PID: str, read: float) -> tuple[list, int]:
    details_a = mappingA(PID)
    return search_and_read_double_A(PID, details_a, read)


def read_double_all(PID: str, read: float) -> tuple[list, int]:
    details_all = mappingALL(PID)
    return search_and_read_double_ALL(PID, details_all, read)


# Dword Readers

def read_dword_xa(PID: str, read: int) -> tuple[list, int]:
    details_xa = mappingXA(PID)
    return search_and_read_dword_XA(PID, details_xa, read)


def read_dword_ca(PID: str, read: int) -> tuple[list, int]:
    details_ca = mappingCA(PID)
    return search_and_read_dword_CA(PID, details_ca, read)


def read_dword_a(PID: str, read: int) -> tuple[list, int]:
    details_a = mappingA(PID)
    return search_and_read_dword_A(PID, details_a, read)


def read_dword_all(PID: str, read: int) -> tuple[list, int]:
    details_all = mappingALL(PID)
    return search_and_read_dword_ALL(PID, details_all, read)


# UTF-8 Readers

def read_utf8_xa(PID: str, read: str) -> tuple[list, int]:
    details_xa = mappingXA(PID)
    return search_and_read_utf8_XA(PID, details_xa, read)


def read_utf8_ca(PID: str, read: str) -> tuple[list, int]:
    details_ca = mappingCA(PID)
    return search_and_read_utf8_CA(PID, details_ca, read)


def read_utf8_a(PID: str, read: str) -> tuple[list, int]:
    details_a = mappingA(PID)
    return search_and_read_utf8_A(PID, details_a, read)


def read_utf8_all(PID: str, read: str) -> tuple[list, int]:
    details_all = mappingALL(PID)
    return search_and_read_utf8_ALL(PID, details_all, read)


# UTF-16LE Readers

def read_utf16le_xa(PID: str, read: str) -> tuple[list, int]:
    details_xa = mappingXA(PID)
    return search_and_read_utf16LE_XA(PID, details_xa, read)


def read_utf16le_ca(PID: str, read: str) -> tuple[list, int]:
    details_ca = mappingCA(PID)
    return search_and_read_utf16LE_CA(PID, details_ca, read)


def read_utf16le_a(PID: str, read: str) -> tuple[list, int]:
    details_a = mappingA(PID)
    return search_and_read_utf16LE_A(PID, details_a, read)


def read_utf16le_all(PID: str, read: str) -> tuple[list, int]:
    details_all = mappingALL(PID)
    return search_and_read_utf16LE_ALL(PID, details_all, read)


# Qword Readers

def read_qword_xa(PID: str, read: int) -> tuple[list, int]:
    details_xa = mappingXA(PID)
    return search_and_read_qword_XA(PID, details_xa, read)


def read_qword_ca(PID: str, read: int) -> tuple[list, int]:
    details_ca = mappingCA(PID)
    return search_and_read_qword_CA(PID, details_ca, read)


def read_qword_a(PID: str, read: int) -> tuple[list, int]:
    details_a = mappingA(PID)
    return search_and_read_qword_A(PID, details_a, read)


def read_qword_all(PID: str, read: int) -> tuple[list, int]:
    details_all = mappingALL(PID)
    return search_and_read_qword_ALL(PID, details_all, read)


# Word Readers

def read_word_xa(PID: str, read: int) -> tuple[list, int]:
    details_xa = mappingXA(PID)
    return search_and_read_word_XA(PID, details_xa, read)


def read_word_ca(PID: str, read: int) -> tuple[list, int]:
    details_ca = mappingCA(PID)
    return search_and_read_word_CA(PID, details_ca, read)


def read_word_a(PID: str, read: int) -> tuple[list, int]:
    details_a = mappingA(PID)
    return search_and_read_word_A(PID, details_a, read)


def read_word_all(PID: str, read: int) -> tuple[list, int]:
    details_all = mappingALL(PID)
    return search_and_read_word_ALL(PID, details_all, read)


# Byte Readers

def read_byte_xa(PID: str, read: int) -> tuple[list, int]:
    details_xa = mappingXA(PID)
    return search_and_read_byte_XA(PID, details_xa, read)


def read_byte_ca(PID: str, read: int) -> tuple[list, int]:
    details_ca = mappingCA(PID)
    return search_and_read_byte_CA(PID, details_ca, read)


def read_byte_a(PID: str, read: int) -> tuple[list, int]:
    details_a = mappingA(PID)
    return search_and_read_byte_A(PID, details_a, read)


def read_byte_all(PID: str, read: int) -> tuple[list, int]:
    details_all = mappingALL(PID)
    return search_and_read_byte_ALL(PID, details_all, read)


# Xor Readers

def read_xor_xa(PID: str, read: int) -> tuple[list, int]:
    details_xa = mappingXA(PID)
    return search_and_read_xor_XA(PID, details_xa, read)


def read_xor_ca(PID: str, read: int) -> tuple[list, int]:
    details_ca = mappingCA(PID)
    return search_and_read_xor_CA(PID, details_ca, read)


def read_xor_a(PID: str, read: int) -> tuple[list, int]:
    details_a = mappingA(PID)
    return search_and_read_xor_A(PID, details_a, read)


def read_xor_all(PID: str, read: int) -> tuple[list, int]:
    details_all = mappingALL(PID)
    return search_and_read_xor_ALL(PID, details_all, read)
