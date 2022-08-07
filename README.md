AndroidMemoryTool
====


AndroidMemoryTool is a memory reader and writer tool designed for android and linux os's 
.This Tool is written in python using ctypes not affective as c.
If you find any bug or not working function you can contact me. 

 *  @date   : 2022/03/23
 *  @author : Abdul Moez
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  @repos  :(https://github.com/Anonym0usWork1221/android-memorytool)
 
 GNU General Public License

 Copyright (c) 2022 AbdulMoez

 The GNU General Public License is a free, copyleft license for software and other kinds of works.

The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.


Requirments
-----------
No additional libraries need this tool is made with python built-in libraries

* Needed python version 3.x

* Android Requirments -> Rooted Device Needed

Installation, Documentation and Examples
----------------------------------------
Simply install it by pip and use it in your project

```pip install androidMemoryTool==0.2```

or by cloning and then run command

``` pip install .```

Project live at 
```https://pypi.org/project/androidMemoryTool/0.2/```


Memory Tool with some examples which can be found in the `examples` folder.

## Usage
1. import the module and grab process id of target process.

For Linux os
```py
import androidMemoryTool
from androidMemoryTool import AndroidMemoryTool
pid = androidMemoryTool.get_pid("ac_client")
```

For Android os use packagename of target application
```py
import androidMemoryTool
from androidMemoryTool import AndroidMemoryTool
pid = androidMemoryTool.get_pid("com.jaratools.org")
```

2. After getting PID we are ready to read or write target process memory
Next steps are sath for both os's

```py
values_replaced = AndroidMemoryTool.write_dword_all(pid, 23, 100)

print(values_replaced)
```

3. Read process memory

```py
import androidMemoryTool
from androidMemoryTool import AndroidMemoryTool
pid = androidMemoryTool.get_pid("ac_client")

offsets, total_values_found = AndroidMemoryTool.read_xor_all(pid, 23)

print(offsets[0], total_values_found)
```

4. Read direct lib offsets
```py
import androidMemoryTool
from androidMemoryTool import AndroidMemoryTool

pid = androidMemoryTool.get_pid("com.somegame.org")
base_addr = AndroidMemoryTool.get_module_base_address(pid, "libUE4.so")
read = AndroidMemoryTool.read_lib_offsets_DOUBLE(pid, base_addr, 0xfff)
print(read)
```

4. Write direct lib offsets
```py
import androidMemoryTool
from androidMemoryTool import AndroidMemoryTool

pid = androidMemoryTool.get_pid("com.somegame.org")
base_addr = AndroidMemoryTool.get_module_base_address(pid, "libUE4.so")
AndroidMemoryTool.write_lib_offsets_DOUBLE(pid, base_addr, 0xfff, 23)

```

this will find all the values realated to your search and replace them with replaced value
and return the number of values it changed

# Video Demonstration
[![usage](https://img.youtube.com/vi/vebE1Rf1ogo/0.jpg)](https://www.youtube.com/watch?v=vebE1Rf1ogo)


Supported Data Types before update
-------------------
All data types are signed.

| **Range** | **Name** |  **Ctype** |
| ------- | -------- | ------------|
| -2,147,483,648 to 2,147,483,647 | DWORD | signed int 
| 3.4E +/- 38 (7 digits) | FLOAT | float
| 1.7E +/- 308 (15 digits) | DOUBLE | double
| -32,768 to 32,767 | WORD | signed short int
| -128 to 127 | BYTE | signed char
| -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | QWORD | signed long long
| -2,147,483,648 to 2,147,483,647 | XOR | signed long
| Random | UTF-8 | Text
| Random | UTF-16LE | Text

Supported Map Ranges
--------------------
| **Short Name** | **Name** |  **Description** |
| ------- | -------- | ------------|
| CA | C++ alloc | RAM c++ Allocated memory
| A  | Anonymous | Range with r-w access only
| XA | Code App  | shared libs memory
| ALL | Whole Memory | Whole Memory of current process (slow)



## Update 0.2

* Expanded Supported Maps Ranges

--------------------
| **Short Name** | **Name** |  **Description** |
| ------- | -------- | ------------|
| ALL | Whole Memory | Whole Memory of current process (slow)
| CA | C++ alloc | RAM c++ Allocated memory
| A  | Anonymous | Range with r-w access only
| Xa | Code App  | shared libs memory (dangerous)
|Jh|Java Heap| Java heap
|Ch|C++ Heap| Heap memory of cpp
|Cd|C++ .data| .Data Memory
|Cb|C++ .bss| .bss section memory
|J|Java| Java memory section
|S|Stack| Stack Memory
|As|Ashmen| Ashmen Memory
|V|Video| Video memory range 
|B_Bad|Bad| Bad Memory (dangerous)
|Xs|Code system| Code system memory (dangerous)

* Improved old mapping methods
* Added Structures in order to work easy
* Fixed crashing on UTF-8 and UTF-16 DataTypes
* Set mapping address to r-w permissions only to avoid I/O errors
* For Linux only use ALL memory range
* Improved Speed
* Added Support of multiple maps Ranges
* Fixed utf data types (values were not changing)
* Added data classes for fast search methods
* Changed License To GNU Public
* Added Fast Search algorithms
* Added Workers support in order to increase cpu speed up searches
* Fixed xrash on termux
* Created package

* UPDATED Usage
For Linux os
```py
from androidMemoryTool import AndroidMemoryTool
import androidMemoryTool
# initialize tool

androidMemoryTool.SettingUpTool().init_setup(PKG="ac_client", TYPE=androidMemoryTool.DataTypes.DWORD,
                                             SPEED_MODE=True, WORKERS=55)

# set True to maps you want to use
androidMemoryTool.InitMemoryTool().init_tool(pMAP=androidMemoryTool.PMAP(ALL=True, C_ALLOC=True, C_DATA=False
                                                                         , C_HEAP=False, CODE_APP=False, C_BSS=False
                                                                         , JAVA_HEAP=False, J_Java=False, CODE_SYSTEM=False
                                                                         , A_ANONYMOUS=False, ASHMEM=False, STACK=False
                                                                         , B_BAD=False))


# if you are reading you will get tuple of two values offset list and total values found

values = AndroidMemoryTool.read_value(100)

founded_offsets = values[0]
founded_values = values[1]
print(founded_offsets)

# if you are writing only return total value wrote

values1 = AndroidMemoryTool.read_write_value(100, 10)
print(values1)

```

For Android
```py
from androidMemoryTool import AndroidMemoryTool
import androidMemoryTool
# initialize tool

androidMemoryTool.SettingUpTool().init_setup(PKG="jaradevlopers.site", TYPE=androidMemoryTool.DataTypes.DWORD,
                                             SPEED_MODE=True, WORKERS=55)

# set True to maps you want to use
androidMemoryTool.InitMemoryTool().init_tool(pMAP=androidMemoryTool.PMAP(ALL=True, C_ALLOC=True, C_DATA=False
                                                                         , C_HEAP=False, CODE_APP=False, C_BSS=False
                                                                         , JAVA_HEAP=False, J_Java=False, CODE_SYSTEM=False
                                                                         , A_ANONYMOUS=False, ASHMEM=False, STACK=False
                                                                         , B_BAD=False))


# if you are reading you will get tuple of two values offset list and total values found

values = AndroidMemoryTool.read_value(100)

founded_offsets = values[0]
founded_values = values[1]
print(founded_offsets)

# if you are writing only return total value wrote

values1 = AndroidMemoryTool.read_write_value(100, 10)
print(values1)


```

Assistance
----------
If you need assistance, you can ask for help on my mailing list:

* Email      : abdulmoez123456789@gmail.com

I also created a Discord group:

* Server     : https://discord.gg/RMNcqzmt9f


Buy Me a coffe
--------------
If you want to support me you can buy me coffe.

BitCoin_addr: ``` 19vwfRXfthPY7f2aqDBpxQvZa6AJFKcdBS ```

