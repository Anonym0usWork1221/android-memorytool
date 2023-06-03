AndroidMemoryTool
====
[![GitHub stars](https://img.shields.io/github/stars/Anonym0usWork1221/android-memorytool.svg)](https://github.com/Anonym0usWork1221/android-memorytool/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Anonym0usWork1221/android-memorytool.svg)](https://github.com/Anonym0usWork1221/android-memorytool/network/members)
[![GitHub issues](https://img.shields.io/github/issues/Anonym0usWork1221/android-memorytool.svg)](https://github.com/Anonym0usWork1221/android-memorytool/issues)
[![GitHub watchers](https://img.shields.io/github/watchers/Anonym0usWork1221/android-memorytool.svg)](https://github.com/Anonym0usWork1221/android-memorytool/watchers)
[![Python](https://img.shields.io/badge/language-Python%203-blue.svg)](https://www.python.org)
[![GPT_LICENSE](https://img.shields.io/badge/license-GPL-red.svg)](https://opensource.org/licenses/)
![code size](https://img.shields.io/github/languages/code-size/Anonym0usWork1221/android-memorytool)


-----------


**_AndroidMemoryTool_** is a memory reader and writer tool designed for android and linux os's 
.This Tool is written in python using ctypes not affective as c.
If you find any bug or not working function you can contact me. 

 *  Date   : 2022/03/23
 *  Author : **__Abdul Moez__**
 *  Version : 0.4
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  Repository  : https://github.com/Anonym0usWork1221/android-memorytool
 *  Documentation: https://github.com/Anonym0usWork1221/android-memorytool/tree/main/Documentation  


 GNU General Public License 

 Copyright (c) 2022 AbdulMoez

# Note
    1. This documentation is for 0.4 version (UPDATED)
    2. You can find old version on pypi if you want to use them

# Version 0.4
    -> Optimized the code
    -> Increase Stability
    -> Fixed Known bugs:
        -> Fixed Simple Text search returning same values as previous search problem
        -> Fixed Increasing Values/address problem in Fast search algorithms
        -> Fixed output pattern in raw dump
    
    -> Added Reset function for queue
    -> Added Hex Pattern Finder 87 ?? BB
    -> Added Hex search for (Float, Dword, Double)
    -> Added support for fork() process (by default takes first pid as parent)
    -> Added Manually PID entering support either in int or string (pid=714 or pid="714")
    -> Can raw dump from Custom start_address-end_address ("4754D6E6-5754D6E6" or "client.so")
    -> Added Known error files and its fixes in (ERRORS.md) file
    -> Added Support to dump map file
    -> Added UTF-8 and UTF-16E support for lib read/write
    -> Added a Detailed Documentation File
    -> Added Documentation string stub in AndroidMemoryTool class

    

Requirements
-----------

* Python 3.x

* Android Requirements -> Rooted Device Needed

Installation
----------------------------------------
1. **Simply install it by pip and use it in your project**  
    ``pip install androidMemoryTool==0.4``

2. **Or by cloning and then run command**  
    ``pip install .``

3. **Project live at**   
    https://pypi.org/project/androidMemoryTool/0.4/


Memory Tool with example which can be found in the   
`Android-Py-Cheats-Script @ 9d2520e`.

## Documentation  

* Getting Process ID

```py
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool.get_pid('ac_client') # for android use package name e.g(com.app.org)
print(tool)
```
* Getting Module Base

```py
from androidMemoryTool import AndroidMemoryTool
pid = AndroidMemoryTool.get_pid('ac_client')
base_addr = AndroidMemoryTool.get_module_base_address(pid, "client.so")
print(base_addr)
```

* Searching and Read process memory

```py
from androidMemoryTool import AndroidMemoryTool

# initialize tool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=False, WORKERS=55,
                        pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(100)
founded_offsets = values[0]
founded_values = values[1]
print(founded_values)
print(founded_offsets)
```

* Search and Write process memory

```py
from androidMemoryTool import AndroidMemoryTool

# initialize tool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=False, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))

values1 = tool.read_write_value(100, 10)
print(values1)
```

* Read address value
```py
from androidMemoryTool import AndroidMemoryTool
pid = AndroidMemoryTool.get_pid('ac_client')
base_addr = AndroidMemoryTool.get_module_base_address(pid, "client.so")
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD)
values1 = tool.read_lib(base_addr, 0xfff150d)
print(values1)
```

* Write address value
```py
from androidMemoryTool import AndroidMemoryTool
pid = AndroidMemoryTool.get_pid('ac_client')
base_addr = AndroidMemoryTool.get_module_base_address(pid, "client.so")
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD)
values1 = tool.write_lib(base_addr, 0xfff150d, 58)
print(values1)
```

* Raw Dump Process memory 
```py
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client")
dump = tool.raw_dump(lib_name='client.so', path='/home/kali/Documents/')
print(dump) # True or False
```

* Address Refiner 
```py
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=False, WORKERS=55,
                     pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(100)
founded_offsets = values[0]
refined_address = tool.refiner_address(list_address=founded_offsets, value_to_refine=50)
print(refined_address)
```

* Find Hex Pattern
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG=662, SPEED_MODE=True, WORKERS=55,
                         pMAP=AndroidMemoryTool.PMAP(ALL=True))
found_pattern = tool.find_hex_pattern("87 ?? 2B")
for index in range(0, len(found_pattern[0])):
    print(f"{found_pattern[0][index]}: {found_pattern[2][index]}")
print(f"Total Pattern found: {found_pattern[1]}")
```
* Dump Maps
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client")
is_dumped = tool.dump_maps(path="./")
print(is_dumped)
```

# Detailed Documentation
You can found detailed documentation [here](https://github.com/Anonym0usWork1221/android-memorytool/tree/main/Documentation)

# Errors
Some known errors and their solutions can be found [here](https://github.com/Anonym0usWork1221/android-memorytool/blob/main/ERRORS.md)   

Supported Data Types
-------------------

All data types are signed.

| **Range**                                               | **Name** | **Type**         |
|---------------------------------------------------------|----------|------------------|
| -2,147,483,648 to 2,147,483,647                         | DWORD    | signed int       |
| 3.4E +/- 38 (7 digits)                                  | FLOAT    | float            |
| 1.7E +/- 308 (15 digits)                                | DOUBLE   | double           |
| -32,768 to 32,767                                       | WORD     | signed short int |
| -128 to 127                                             | BYTE     | signed char      |
| -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | QWORD    | signed long long |
| -2,147,483,648 to 2,147,483,647                         | XOR      | signed long      |
| Random                                                  | UTF_8    | Text             |
| Random                                                  | UTF_16LE | Text             |



Supported Map Ranges
--------------------
| **Script Name** | **Name**     | **Description**                        |
|-----------------|--------------|----------------------------------------|
| ALL             | Whole Memory | Whole Memory of current process (slow) |
| C_ALLOC         | C++ alloc    | RAM c++ Allocated memory               |
| A_ANONYMOUS     | Anonymous    | Range with r-w access only             |
| CODE_APP        | Code App     | shared libs memory (dangerous)         |
| JAVA_HEAP       | Java Heap    | Java heap                              |
| C_HEAP          | C++ Heap     | Heap memory of cpp                     |
| C_DATA          | C++ .data    | .Data Memory                           |
| C_BSS           | C++ .bss     | .bss section memory                    |
| J_Java          | Java         | Java memory section                    |
| STACK           | Stack        | Stack Memory                           |
| ASHMEM          | Ashmen       | Ashmen Memory                          |
| V_video         | Video        | Video memory range                     |
| B_Bad           | Bad          | Bad Memory (dangerous)                 |
| CODE_SYSTEM     | Code system  | Code system memory (dangerous)         |

# Contributor

<a href = "https://github.com/Anonym0usWork1221/android-memorytool/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=Anonym0usWork1221/android-memorytool"/>
</a>


Assistance
----------
If you need assistance, you can ask for help on my mailing list:

* Email      : abdulmoez123456789@gmail.com

I also created a Discord group:

* Server     : https://discord.gg/RMNcqzmt9f


Buy Me a coffee
--------------
If you want to support me you can buy me coffee.

BTC: ``` 19vwfRXfthPY7f2aqDBpxQvZa6AJFKcdBS ```

