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
import sys


# mapping XA
def mappingXA(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_xa = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split()
        region = temp_details[len(temp_details) - 1]
        re_region = temp_details[len(temp_details) - 2]
        perm = temp_details[1]

        # Xa -> code app:r-xp, lib, .so, .jar
        if ("lib" in region or "lib" in re_region) and ("r" in perm or "w" in perm) and (
                ".so" in region or ".so" in re_region) and ("system" in region or "system" in re_region):
            details_xa["address"].append(temp_details[0])
            details_xa["permissions"].append(temp_details[1])
            details_xa["allocated"].append(region)

    map_file.close()
    return details_xa


# mapping CA
def mappingCA(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_ca = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split()
        region = temp_details[len(temp_details) - 1]
        re_region = temp_details[len(temp_details) - 2]
        perm = temp_details[1]

        # ca anon, key -> anon:libc_malloc, rw-p, rwxp
        if ("anon" in region or "anon" in re_region) and ("r" in perm or "w" in perm) and (
                "libc_malloc" in region or "libc_malloc" in re_region):
            details_ca["address"].append(temp_details[0])
            details_ca["permissions"].append(temp_details[1])
            details_ca["allocated"].append(region)

    map_file.close()
    return details_ca


# mapping A
def mappingA(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_a = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split()
        region = temp_details[len(temp_details) - 1]
        re_region = temp_details[len(temp_details) - 2]
        perm = temp_details[1]

        # A -> Anonymous: just rw-p
        if ("0" in region or ":" in re_region) and ("r" in perm or "w" in perm):
            details_a["address"].append(temp_details[0])
            details_a["permissions"].append(temp_details[1])
            details_a["allocated"].append(region)

    map_file.close()
    return details_a


# mapping ALL
def mappingALL(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_all = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split()
        region = temp_details[len(temp_details) - 1]

        details_all["address"].append(temp_details[0])
        details_all["permissions"].append(temp_details[1])
        details_all["allocated"].append(region)

    map_file.close()
    return details_all


# finding mapping all
def mappings(pid: str) -> tuple[dict, dict, dict, dict]:
    try:
        map_file = open(f"/proc/{pid}/maps", "r")

    except Exception as e:
        print("[*]Exception ", e)
        sys.exit()
    # names

    '''
    O->others:others -> --p, anon, system/framework, etc
    Jh->:rw-p, anon:dalvik-main space
    Xs->system: --xp, lib, .so, system
    J->Java: 
    ch -> c++heap: 
    ca -> c++ alloc: anon, key -> anon:libc_malloc, rw-p, rwxp
    cd -> c++ data:
    cb -> c++ bss:
    PS -> PPSSPP: 
    A -> Anonymous: just rw-p
    S -> Stack:
    As -> Ashmem:
    V -> Video:
    B -> Bad(dang):
    Xa -> code app:r-xp, lib, .so, .jar
    '''

    # order
    '''
                0               1           2           3       4           5           6
    ['76a01ae000-76a01af000', 'r--p', '00000000', '00:00', '26', '[anon:atexit', 'handler]']

    A -> 4[]
    '''
    details_all = {"address": [], "permissions": [], "allocated": []}
    details_ca = {"address": [], "permissions": [], "allocated": []}
    details_xa = {"address": [], "permissions": [], "allocated": []}
    details_a = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split()
        region = temp_details[len(temp_details) - 1]
        re_region = temp_details[len(temp_details) - 2]
        perm = temp_details[1]

        details_all["address"].append(temp_details[0])
        details_all["permissions"].append(temp_details[1])
        details_all["allocated"].append(region)

        # ca anon, key -> anon:libc_malloc, rw-p, rwxp
        if ("anon" in region or "anon" in re_region) and ("r" in perm or "w" in perm) and (
                "libc_malloc" in region or "libc_malloc" in re_region):
            details_ca["address"].append(temp_details[0])
            details_ca["permissions"].append(temp_details[1])
            details_ca["allocated"].append(region)

        # A -> Anonymous: just rw-p
        elif ("0" in region or ":" in re_region) and ("r" in perm or "w" in perm):
            details_a["address"].append(temp_details[0])
            details_a["permissions"].append(temp_details[1])
            details_a["allocated"].append(region)

        # Xa -> code app:r-xp, lib, .so, .jar
        elif ("lib" in region or "lib" in re_region) and ("r" in perm or "w" in perm) and (
                ".so" in region or ".so" in re_region) and ("system" in region or "system" in re_region):
            details_xa["address"].append(temp_details[0])
            details_xa["permissions"].append(temp_details[1])
            details_xa["allocated"].append(region)

        else:
            pass
    map_file.close()
    return details_ca, details_a, details_xa, details_all
