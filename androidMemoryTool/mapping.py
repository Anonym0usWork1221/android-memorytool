"""
 *  @date   : 2022/03/23
 *  Version : 0.1
 *  @author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# finding mapping all

'''
O->others:others -> --p, anon, system/framework, etc
Jh->:rw-p, anon:dalvik-main space
Xs->system: --xp, lib, .so, system
J->Java: rw-p, javalib
ch -> c++heap: 
ca -> c++ alloc: anon, key -> anon:libc_malloc, rw-p, rwxp *
cd -> c++ data: *
cb -> c++ bss:
PS -> PPSSPP: 
A -> Anonymous: just rw-p   *
S -> Stack:
As -> Ashmem:
V -> Video:
B -> Bad(dang):
Xa -> code app:r-xp, lib, .so, .jar
'''

# order
'''
#address                  perms      offset    device  inode         pathname

            0                1        2          3       4             5
['76a01ae000-76a01af000', 'r--p', '00000000', '00:00', '26', '[anon:atexit handler]']

A -> 4[]
'''


# ! /usr/bin/env python


# mapping XA
def mappingXA(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_xa = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        # Xa -> code app:r-xp, lib, .so, .jar
        if ("lib" in region) and ("rw" in perm) and (
                ".so" in region) and ("system" in region):
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
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        # ca anon, key -> anon:libc_malloc, rw-p, rwxp
        if ("anon" in region) and ("rw" in perm) and ("libc_malloc" in region):
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
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        # A -> Anonymous: just rw-p
        if (len(line) < 46) and ("rw" in perm):
            details_a["address"].append(temp_details[0])
            details_a["permissions"].append(temp_details[1])
            details_a["allocated"].append(region)

    map_file.close()
    return details_a


# ----------------------------------------- NEW maps----------------------------
# mapping B = bad
def mappingB(PID: str) -> dict:
    """B->"""

    map_file = open(f"/proc/{PID}/maps", "r")
    details_o = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        # B

        if ("fonts" in region) and ("rw" in perm):
            details_o["address"].append(temp_details[0])
            details_o["permissions"].append(temp_details[1])
            details_o["allocated"].append(region)

    map_file.close()
    return details_o


# mapping CB = c++ bss
def mappingCB(PID: str) -> dict:
    """CB->"""

    map_file = open(f"/proc/{PID}/maps", "r")
    details_cb = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        # CB

        if ("[anon:.bss]" in region) and ("rw" in perm):
            details_cb["address"].append(temp_details[0])
            details_cb["permissions"].append(temp_details[1])
            details_cb["allocated"].append(region)

    map_file.close()
    return details_cb


# mapping CD = c++ data
def mappingCD(PID: str) -> dict:
    """CD->"""

    map_file = open(f"/proc/{PID}/maps", "r")
    details_cd = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        # CD

        if ("/data/app/" in region) and ("rw" in perm):
            details_cd["address"].append(temp_details[0])
            details_cd["permissions"].append(temp_details[1])
            details_cd["allocated"].append(region)

    map_file.close()
    return details_cd


# mapping CH = C++ heap
def mappingCH(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_ch = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        if ("[heap]" in region) and ("rw" in perm):
            details_ch["address"].append(temp_details[0])
            details_ch["permissions"].append(temp_details[1])
            details_ch["allocated"].append(region)

    map_file.close()
    return details_ch


# mapping JH = Java heap
def mappingJH(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_jh = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        if ("/dev/ashmem/" in region) and ("rw" in perm):
            details_jh["address"].append(temp_details[0])
            details_jh["permissions"].append(temp_details[1])
            details_jh["allocated"].append(region)

    map_file.close()
    return details_jh


# mapping XS = Code system
def mappingXS(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_xs = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        if ("/system" in region) and ("rw" in perm):
            details_xs["address"].append(temp_details[0])
            details_xs["permissions"].append(temp_details[1])
            details_xs["allocated"].append(region)

    map_file.close()
    return details_xs


# mapping S = Stack
def mappingS(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_s = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        if ("[stack]" in region) and ("rw" in perm):
            details_s["address"].append(temp_details[0])
            details_s["permissions"].append(temp_details[1])
            details_s["allocated"].append(region)

    map_file.close()
    return details_s


# mapping AS = Ashmem
def mappingAS(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_as = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        if ("/dev/ashmem/" in region and "dalvik" in region) and ("rw" in perm):
            details_as["address"].append(temp_details[0])
            details_as["permissions"].append(temp_details[1])
            details_as["allocated"].append(region)

    map_file.close()
    return details_as


# mapping J = Java
def mappingJ(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_j = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        if ("javalib" in region and "dalvik" in region) and ("rw" in perm):
            details_j["address"].append(temp_details[0])
            details_j["permissions"].append(temp_details[1])
            details_j["allocated"].append(region)

    map_file.close()
    return details_j


# mapping V = video
def mappingV(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_v = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split(" ", 5)
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        if ("kgsl-3d0" in region) and ("rw" in perm):
            details_v["address"].append(temp_details[0])
            details_v["permissions"].append(temp_details[1])
            details_v["allocated"].append(region)

    map_file.close()
    return details_v


# mapping ALL
def mappingALL(PID: str) -> dict:
    map_file = open(f"/proc/{PID}/maps", "r")
    details_all = {"address": [], "permissions": [], "allocated": []}
    for line in map_file.readlines():
        temp_details = line.split()
        region = temp_details[len(temp_details) - 1]
        perm = temp_details[1]

        if "rw" in perm:
            details_all["address"].append(temp_details[0])
            details_all["permissions"].append(temp_details[1])
            details_all["allocated"].append(region)

    map_file.close()
    return details_all
