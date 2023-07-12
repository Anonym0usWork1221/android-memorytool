AndroidMemoryTool
====
![PyPI - Version](https://img.shields.io/pypi/v/androidMemoryTool?label=pypi%20package)
![PyPI - Downloads](https://img.shields.io/pypi/dm/androidMemoryTool)
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

 *  Date   : 2023/07/11
 *  Author : **__Abdul Moez__**
 *  Version : 0.5
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  Repository  : https://github.com/Anonym0usWork1221/android-memorytool
 *  Documentation: https://github.com/Anonym0usWork1221/android-memorytool/tree/main/Documentation  


 GNU General Public License 

 Copyright (c) 2022 AbdulMoez

-----------

# Note
    1. This documentation is for 0.5 version (UPDATED)
    2. You can find old version on pypi if you want to use them

-----------

# Version 0.5
    -> ----------------------------------------MOD-LOGS-------------------------------------------------- <-

    -> Fixed the invalid output of hex address in reading process
    -> Fixed the read_lib and write_lib hex issue the now pass the hex as a
       string in old method the calculation was generating errors due to hex value passed as integer
    -> Optimize the code of DataClass.py
    -> Fixed Initializers of some classes (e.g: ThreadingController and DataClasses)
    -> Added Complete self explaining doc strings to all the classes and functions
    -> Rewrite the Mapping class inorder to reduce junk size and correct the mapping of anonymous range.
    -> Added new function of find_and_replace_hex_pattern() for search wild card and replace that in hex form
       e.g: find_and_replace_hex_pattern(search_pattern='2D??3D', replace_pattern='1D4D2D')
    -> Added CLI for command line interface
    
    -> ----------------------------------------TO-DO---------------------------------------------------- <-
    
    -> TODO: Add Reverse engineering Support for offline binaries using known disassemblers (capstone, keystone, r2pipe)
    -> TODO: Add Assembly support for reading and writing memory at runtime
    
    -> ----------------------------------------SUGGESTIONS---------------------------------------------- <-
    
    -> SUGGESTIONS: You can leave your suggestions either on my mailbox or discord server.


-----------    

Requirements
-----------

* Python 3.x

* Android Requirements -> Rooted Device Needed

-----------

Installation
----------------------------------------
1. **Simply install it by pip and use it in your project**  
    ``pip install androidMemoryTool==0.5``

2. **Or by cloning and then run command**  
    ``pip install .``

3. **Project live at**   
    https://pypi.org/project/androidMemoryTool/0.5/


Memory Tool with example which can be found in the   
`Android-Py-Cheats-Script @ 9d2520e`.

-----------
Video Demo
-----------
[![Video Demo](https://img.youtube.com/vi/Ivyy6GQzm3w/0.jpg)](https://www.youtube.com/watch?v=Ivyy6GQzm3w)

-----------

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

* Find and replace hex Patterns
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG=662, SPEED_MODE=True, WORKERS=55,
                         pMAP=AndroidMemoryTool.PMAP(ALL=True))
found_pattern = tool.find_and_replace_hex_pattern("87 ?? 2B", "87 1D 2B")
for index in range(0, len(found_pattern[0])):
    #              address                      hex value
    print(f"{found_pattern[0][index]}: {found_pattern[2][index]}")
print(f"Total Pattern found and replaced: {found_pattern[1]}") # returns number
```

* Dump Maps
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client")
is_dumped = tool.dump_maps(path="./")
print(is_dumped)
```

-----------

## Android Memory Tool CLI Documentation
```
-> This Version is come with an exciting feature called CLI (command line interface) means you dont need to execute the code everytime just use the tools cli to do short work.
```

The Android Memory Tool CLI is a command-line interface for the Android Memory Tool. It provides various commands to interact with memory in Android applications.

### Usage  
* For Linux:  
```
python3 -m androidMemoryTool <command> [options]
```
* For Android:
Execute the tool with root privileges using `sudo`:
```
sudo python3 -m androidMemoryTool <command> [options]
```

* If you added the bin path of python libraries to environment variable then you can execute it directly
````
amt <command> [options]
````
**and use sudo for android**

### Available Commands
* `read_value`: Read a value from memory.
* `read_write_value`: Read and write a value in memory.
* `write_lib`: Write a value to a library.
* `read_lib`: Read a value from a library.
* `refiner_address`: Refine a list of addresses.
* `get_module_base_address`: Get the base address of a module.
* `raw_dump`: Dump a library as raw binary.
* `find_hex_pattern`: Find a hexadecimal pattern in memory.
* `find_and_replace_hex_pattern`: Find and replace a hexadecimal pattern in memory.
* `dump_maps`: Dump memory maps.
* `get_pid`: Return the PID of a process.
* `help`: Display help information.

### Command-line Data Types
Pass them with just name as given below
* `DWORD`
* `FLOAT`
* `DOUBLE`
* `WORD`
* `BYTE`
* `QWORD`
* `XOR`
* `UTF_8`
* `UTF_16LE`

### Command Details
You can get detailed information about each command and its usage by running:
```
python3 -m androidMemoryTool help <command>
```
For example, to get help for the read_value command, run:
```
python3 -m androidMemoryTool help read_value
```

### Examples
* Read a value from memory:
````
python3 -m androidMemoryTool read_value <pkg> <type> <speed_mode> <workers> <read>
````
Replace <pkg>, <type>, <speed_mode>, <workers>, and <read> with the appropriate values.  

* Read and write a value in memory:
````
python3 -m androidMemoryTool read_write_value <pkg> <type> <speed_mode> <workers> <read> <write>
````
Replace <pkg>, <type>, <speed_mode>, <workers>, <read>, and <write> with the appropriate values.

* Write a value to a library:
````
python3 -m androidMemoryTool write_lib <pkg> <type> <base_address> <offset> <write_value>
````
Replace <pkg>, <type>, <base_address>, <offset>, and <write_value> with the appropriate values.

* Read a value from a library:
````
python3 -m androidMemoryTool read_lib <pkg> <type> <base_address> <offset> [--value <value>]
````
Replace <pkg>, <type>, <base_address>, <offset>, and <value> with the appropriate values.

* Refine a list of addresses:
````
python3 -m androidMemoryTool refiner_address <pkg> <type> <speed_mode> <workers> <list_address> <value_to_refine>
````
Replace <pkg>, <type>, <speed_mode>, <workers>, <list_address>, and <value_to_refine> with the appropriate values.

* Get the base address of a module:
````
python3 -m androidMemoryTool get_module_base_address <pid> <module_name>
````
Replace <pid> and <module_name> with the appropriate values.

* Dump a library as raw binary:
````
python3 -m androidMemoryTool raw_dump <pkg> <lib_name> [<path>]
````
Replace <pkg>, <lib_name>, and <path> with the appropriate values. The <path> argument is optional and defaults to the current directory.

* Find a hexadecimal pattern in memory:
````
python3 -m androidMemoryTool find_hex_pattern <pkg> <type> <speed_mode> <workers> <hex_pattern>
````
Replace <pkg>, <type>, <speed_mode>, <workers>, and <hex_pattern> with the appropriate values.

* Find and replace a hexadecimal pattern in memory:
````
python3 -m androidMemoryTool find_and_replace_hex_pattern <pkg> <type> <speed_mode> <workers> <search_pattern> <replace_pattern>
````
Replace <pkg>, <type>, <speed_mode>, <workers>, <search_pattern>, and <replace_pattern> with the appropriate values.

* Dump memory maps:
````
python3 -m androidMemoryTool dump_maps <pkg> [--path <path>]
````
Replace <pkg> and <path> with the appropriate values. The <path> argument is optional and defaults to the current directory.

* Return the PID of a process:
````
python3 -m androidMemoryTool get_pid <pkg>
````
Replace <pkg> with the appropriate package name.

### Version
To get the version of the Android Memory Tool, use the following command:
````
python3 -m androidMemoryTool -v
````
### Help
To display general help information or help for a specific command, use the help command:
````
python3 -m androidMemoryTool help [command]
````
Replace [command] with the desired command to get help for that command. If no command is provided, general help information will be displayed.


-----------

# Detailed Documentation
You can find detailed documentation [here](https://github.com/Anonym0usWork1221/android-memorytool/tree/main/Documentation)

-----------

# Errors
Some known errors and their solutions can be found [here](https://github.com/Anonym0usWork1221/android-memorytool/blob/main/ERRORS.md)   

-----------

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

-----------

# Contributor

<a href = "https://github.com/Anonym0usWork1221/android-memorytool/graphs/contributors">
  <img src = "https://contrib.rocks/image?repo=Anonym0usWork1221/android-memorytool"/>
</a>

-----------

Assistance
----------
If you need assistance, you can ask for help on my mailing list:

* Email      : abdulmoez123456789@gmail.com

I also created a Discord group:

* Server     : https://discord.gg/RMNcqzmt9f

-----------

Buy Me a coffee
--------------
If you want to support me you can buy me coffee.

BTC: ``` 19vwfRXfthPY7f2aqDBpxQvZa6AJFKcdBS ```

