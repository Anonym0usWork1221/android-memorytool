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


<br>
<br>
<p align="center">
  <img src="assets/android_memory_tool.jpg"  title="Android Memory Tool" width="500px">
</p>

-----------

__*AndroidMemoryTool*__: A Powerful Memory Reader and Writer Tool for Android, Linux, and Windows Operating Systems

AndroidMemoryTool is a sophisticated memory manipulation tool meticulously crafted for use on Android, Linux, and 
Windows operating systems. This versatile tool is meticulously coded in Python, utilizing ctypes and struct datatypes, 
ensuring efficiency comparable to C.

Our commitment to excellence extends to our support system. If you encounter any bugs or non-functional features, 
please do not hesitate to contact us. Your feedback is invaluable in our pursuit of continuous improvement.

 *  Date   : 2023/09/30
 *  Author : **__Abdul Moez__**
 *  Version : 0.6 (+Windows Support)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  Repository  : [Main Branch](https://github.com/Anonym0usWork1221/android-memorytool)
 *  Documentation: [AndroidMemoryToolExtensiveDocumentation](https://github.com/Anonym0usWork1221/android-memorytool/tree/main/Documentation)


 GNU General Public License  
 Copyright (c) 2023 AbdulMoez

-----------

# Note
    1. This documentation is for 0.6 version (UPDATED)
    2. You can find old version on pypi if you want to use them

-----------

# Version 0.6

````
-----------------------------------------MODIFICATION LOG--------------------------------------------------

1. Added Support for Windows OS (while maintaining compatibility with existing API calls).
2. Introduced a Robust Memory Profiler capable of threshold-based memory leak and churn detection using process IDs.
3. Customizability of the Memory Profiler has been enhanced (Please refer to the documentation for details).
4. Introduced several static methods, including:
  - get_developer
  - get_version_code
  - get_cpu_counts
  - get_platform
  - is_root_acquired
5. We are pleased to announce the addition of group search support with a new parameter, "is_grouped," 
   which can be set to True. This enhancement allows users to perform grouped searches effectively and efficiently. 
   By default, the value of the range is set to 512, aligning with the capabilities of Game Guardian.

6. We have recently introduced two new error classes to enhance the functionality of our memory tool: 
   WINAPIException and PIDException. These additions further bolster our product's robustness and error-handling 
   capabilities, ensuring a more seamless and reliable user experience.
7. We've meticulously updated and expanded our documentation to ensure that it's more informative, user-friendly, 
   and grammatically impeccable than ever before.
--------------------------------------------TO-DO LIST----------------------------------------------------

1. FIXME: Resolve the speed mode bug on Windows OS.
2. TODO: Implement Reverse Engineering Support for offline binaries using renowned disassemblers such as Capstone, 
         Keystone, and R2pipe.
3. TODO: Add Assembly support for runtime memory reading and writing.
4. TODO: Incorporate wildcard support in Windows API.
5. TODO: Expand the functionality with additional API handling methods.

----------------------------------------SUGGESTIONS-------------------------------------------------------

Your valuable suggestions are welcome through either direct messages or our Discord server.

-------------------------------------------NOTICE--------------------------------------------------------

This update has significantly increased the complexity of the Memory Tool, making it increasingly challenging for a 
single individual to manage its development. Therefore, we warmly welcome contributions from anyone interested in 
collaborating on its further enhancement.
````


-----------
Supported Platforms
-----------
* Windows Support (Started from 0.6 Version)
* Linux Support (Started From 0.2 Version)
* Android Support (Started From 0.1 Version)

-----------
Supported ByteOrders
-----------
* Little-Endian
* Big-Endian

-----------
Tested Platforms
-----------
> Our tool has been rigorously tested and proven to run seamlessly on the following platforms:

* Windows 11 (64-bit)
* Linux - Kali Linux (64-bit)
* Android - Xiaomi 11T (Termux, 64-bit, Android 13)

> Rest assured, our commitment to compatibility ensures a smooth and efficient user experience across these platforms.

-----------
Requirements
-----------

* Python 3.5+
* Android Requirements: Rooted Device Required
* Linux Requirements: Root access may be necessary on certain Linux platforms.
* Windows Requirements: Administrator permissions required


-----------
Dependencies
-----------
* Pip Dependencies (Automatically Installed in Requirements): `psutil`

-----------
Installation
----------------------------------------
1. **Installation via Pip for Easy Integration into Your Project**  
    To effortlessly incorporate the Android Memory Tool into your project, execute the following pip command:  
    > pip install androidMemoryTool==0.6

2. **Installation by Cloning the Repository and Running Commands**  
    Alternatively, you can acquire the Android Memory Tool by cloning the GitHub repository and executing the 
    subsequent commands:
   > git clone https://github.com/Anonym0usWork1221/android-memorytool/tree/main   
    cd android-memorytool  
    pip install .

3. **Project live at**  
    [PyPi-0.6](https://pypi.org/project/androidMemoryTool/0.6/)


Utilize our cutting-edge Memory Tool, replete with intricate examples, readily accessible within the designated folder.
[Access Android-Py-Cheats-Script @ 9d2520e](https://github.com/Anonym0usWork1221/Android-Py-Cheats-Script/tree/014497b78538930082109e8dd3da123e7f75197e).

-----------
Video Demo - 0.5
-----------
[![Video Demo](https://img.youtube.com/vi/5jV1haoEyWQ/0.jpg)](https://www.youtube.com/watch?v=5jV1haoEyWQ)

-----------

## Documentation  

* **Getting Process ID**  
To obtain the Process ID (PID) of a target process, you can use the following code snippet:

```py
from androidMemoryTool import AndroidMemoryTool
# Initialize the tool and set the speed_mode to off for Windows in this version only.
tool = AndroidMemoryTool(PKG="ac_client")
pid = tool.get_pid()
print(pid)
```
* **Getting Module Base**  
To retrieve the base address of a specific module in the target process, you can use the following code snippet:

```py
from androidMemoryTool import AndroidMemoryTool

tool = AndroidMemoryTool(PKG="ac_client")
base_addr = tool.get_module_base_address("client.so")
print(base_addr)
```

* **Searching and Reading Process Memory**  
To search for a specific value in the process memory and read the results, use the following code:

```py
from androidMemoryTool import AndroidMemoryTool, DataTypes, PMAP

# Initialize the tool and set the speed_mode to off for Windows in this version only.
tool = AndroidMemoryTool(PKG="Tutorial-x86_64.exe",
                         SPEED_MODE=False,
                         TYPE=DataTypes.DWORD,
                         WORKERS=AndroidMemoryTool.get_cpu_counts(fraction=2),
                         pMAP=PMAP(ALL=True)
                         )
# Search for a value in the entire memory.
values = tool.read_value(100)
founded_offsets = values[0]
founded_values = values[1]
print(founded_values)
print(founded_offsets)
```

* **Searching and Writing Process Memory**  
You can search for a specific value in the process memory and replace it with a new value using the following code:

```py
from androidMemoryTool import AndroidMemoryTool, DataTypes, PMAP

# Initialize the tool and set the speed_mode to off for Windows in this version only.
tool = AndroidMemoryTool(PKG="Tutorial-x86_64.exe",
                         SPEED_MODE=False,
                         TYPE=DataTypes.DWORD,
                         WORKERS=AndroidMemoryTool.get_cpu_counts(fraction=2),
                         pMAP=PMAP(ALL=True)
                         )
# Search for all values and replace them with a new value.
values1 = tool.read_write_value(100, 10)
print(values1)
```

* **Reading Address Value**  
To read the value at a specific memory address, use the following code:

```py
from androidMemoryTool import AndroidMemoryTool, DataTypes

tool = AndroidMemoryTool(PKG="ac_client",
                         TYPE=DataTypes.DWORD
                         )
base_addr = tool.get_module_base_address("client.so")
values1 = tool.read_lib(base_addr, '0xfff150d')
print(values1)

```

* **Writing Address Value**  
To write a value to a specific memory address, use the following code:

```py
from androidMemoryTool import AndroidMemoryTool, DataTypes

tool = AndroidMemoryTool(PKG="ac_client", TYPE=DataTypes.DWORD)
base_addr = tool.get_module_base_address("client.so")
values1 = tool.write_lib(base_addr, '0xfff150d', 58)
print(values1)
```

* **Raw Dump Process Memory**  
You can dump the memory of a process using the following code:

```py
from androidMemoryTool import AndroidMemoryTool

tool = AndroidMemoryTool(PKG="ac_client")
dump = tool.raw_dump(lib_name='client.so', path='./')
print(dump)
```

* **Address Refiner**  
To refine addresses based on a value, use the following code:

```py
from androidMemoryTool import AndroidMemoryTool, DataTypes, PMAP

tool = AndroidMemoryTool(PKG="Tutorial-x86_64.exe",
                         SPEED_MODE=False,
                         TYPE=DataTypes.DWORD,
                         WORKERS=AndroidMemoryTool.get_cpu_counts(fraction=2),
                         pMAP=PMAP(ALL=True)
                         )
values = tool.read_value(100)
founded_offsets = values[0]
refined_address = tool.refiner_address(list_address=founded_offsets, value_to_refine=50)
print(refined_address)

```

* **Finding Hex Patterns (Linux and Android only)**   
To locate hex patterns in memory, use the following code (Linux and Android only):

```python
from androidMemoryTool import AndroidMemoryTool, DataTypes, PMAP

tool = AndroidMemoryTool(PKG="Tutorial-x86_64.exe",
                         SPEED_MODE=False,
                         TYPE=DataTypes.DWORD,
                         WORKERS=AndroidMemoryTool.get_cpu_counts(fraction=2),
                         pMAP=PMAP(ALL=True)
                         )
found_pattern = tool.find_hex_pattern("87 ?? 2B")
for index in range(0, len(found_pattern[0])):
    print(f"{found_pattern[0][index]}: {found_pattern[2][index]}")
print(f"Total Pattern found: {found_pattern[1]}")

```

* **Finding and Replacing Hex Patterns (Linux and Android only)**  
To find and replace hex patterns in memory, use the following code (Linux and Android only):

```python
from androidMemoryTool import AndroidMemoryTool, DataTypes, PMAP

tool = AndroidMemoryTool(PKG="Tutorial-x86_64.exe",
                         SPEED_MODE=False,
                         TYPE=DataTypes.DWORD,
                         WORKERS=AndroidMemoryTool.get_cpu_counts(fraction=2),
                         pMAP=PMAP(ALL=True)
                         )
found_pattern = tool.find_and_replace_hex_pattern("87 ?? 2B", "87 1D 2B")
for index in range(0, len(found_pattern[0])):
    print(f"{found_pattern[0][index]}: {found_pattern[2][index]}")
print(f"Total Pattern found and replaced: {found_pattern[1]}")
```

* **Dumping Memory Maps**  
You can dump the memory maps of a process using the following code:

```python
from androidMemoryTool import AndroidMemoryTool

tool = AndroidMemoryTool(PKG="ac_client")
is_dumped = tool.dump_maps(path="./")
print(is_dumped)
```

* **Group Search**  
Perform a group search to read and modify multiple values at once in specific range:

```python
from androidMemoryTool import AndroidMemoryTool, DataTypes, PMAP

tool = AndroidMemoryTool(PKG="Tutorial-x86_64.exe",
                         SPEED_MODE=False,
                         TYPE=DataTypes.DWORD,
                         WORKERS=AndroidMemoryTool.get_cpu_counts(fraction=3),
                         pMAP=PMAP(ALL=True)
                         )
values = tool.read_value(read=[1000, 100], is_grouped=True, range_val=510)
for value in values[0]:
    tool.write_lib(value, '0x0', 1000)
print(f"Total Values Modified: {values[1]}")
```

* **Prebuilt Memory Profiler**  
Utilize the prebuilt Memory Profiler to analyze memory usage:

```python
from androidMemoryTool import AndroidMemoryTool

tool = AndroidMemoryTool(PKG="Tutorial-x86_64.exe")
memory_profiler = tool.get_memory_profiler()
memory_profiler.start_profiling(logging=False)
```

* **Static Methods**  
The AndroidMemoryTool also provides static methods for various functionalities:

```python
from androidMemoryTool import AndroidMemoryTool

# Get the name of the developer
print(AndroidMemoryTool.get_developer())

# Get the version code of the tool
print(AndroidMemoryTool.get_version_code())

# Get the number of CPU cores available on your device (can specify a fraction)
print(AndroidMemoryTool.get_cpu_counts())

# Get the platform the script is running on (Linux, Android, Windows)
print(AndroidMemoryTool.get_platform(verbose=True))

# Check if the script is running on a rooted terminal or non-rooted
print(AndroidMemoryTool.is_root_acquired())
```

-----------
## Error Handling Enhancements
> We have introduced new error handling classes to enhance the robustness of our code. 
> These error handling classes will help you better manage and troubleshoot issues that may arise during the 
> execution of your code.

*  **PIDException**:  
The `PIDException` is raised when there is an issue with connecting to the specified process. 
This error message provides valuable information to help you diagnose and resolve the problem efficiently.  

```python
try:
    from androidMemoryTool import AndroidMemoryTool, PIDException
    tool = AndroidMemoryTool(PKG="ac_client")
except PIDException as e:
    print(f"An error occurred while trying to connect to the process: {e}")
```

*  **WINAPIException (Only occur on Windows)**:  
The `WINAPIException` is specific to Windows environments and is raised when an error occurs during a read operation. 
This error message provides detailed information about the issue encountered during the reading process, making it 
easier for you to pinpoint and rectify the problem.

```python
try:
    from androidMemoryTool import AndroidMemoryTool, WINAPIException
    tool = AndroidMemoryTool(PKG="ac_client")
    tool.read_value(read="some_wrong_value")
except WINAPIException as e:
    print(f"An error occurred while reading a value: {e}")

```

-----------
## Android Memory Tool CLI Documentation
> CLI Documentation Relocated: The CLI documentation has been relocated to the Documentation folder. 
> You can access it by visiting the [AndroidMemoryToolCLIDOCS](https://github.com/Anonym0usWork1221/android-memorytool/tree/main/Documentation) on GitHub.

-----------
## Custom Android Memory Profiling Documentation
> You can make custom Profiling tools by going to [MemoryProfilerDOCS](https://github.com/Anonym0usWork1221/android-memorytool/tree/main/Documentation) on GitHub.

-----------
# Comprehensive Documentation
> For in-depth and comprehensive documentation, please refer to the following link:
 [Comprehensive Documentation](https://github.com/Anonym0usWork1221/android-memorytool/tree/main/Documentation)
-----------

# Troubleshooting Errors
* **Windows ERROR ON `SPEED_MODE`**  
An issue has been identified on Windows systems related to the SPEED_MODE option, 
which may result in the application getting stuck in a thread indefinitely. As a temporary solution, 
we recommend disabling the SPEED_MODE for Windows.

> Some other known errors and their solutions can be found [here](https://github.com/Anonym0usWork1221/android-memorytool/blob/main/ERRORS.md)   

-----------

Supported Data Types (For all Linux, Android and Windows)
-------------------

All data types are signed.

| **Range**                                               | **Name** | **Type**         | **Bytes** |
|---------------------------------------------------------|----------|------------------|-----------|
| -2,147,483,648 to 2,147,483,647                         | DWORD    | signed int       | 4         |
| 3.4E +/- 38 (7 digits)                                  | FLOAT    | float            | 4         |
| 1.7E +/- 308 (15 digits)                                | DOUBLE   | double           | 8         |
| -32,768 to 32,767                                       | WORD     | signed short int | 2         |
| -128 to 127                                             | BYTE     | signed char      | 1         |
| -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807 | QWORD    | signed long long | 8         |
| -2,147,483,648 to 2,147,483,647                         | XOR      | signed long      | 4         |
| Random                                                  | UTF_8    | char[]           | Random    |
| Random                                                  | UTF_16LE | char[]           | Random    |



Supported Map Ranges (Linux and Android only)
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
Support and Contact Information
----------
> If you require any assistance or have questions, please feel free to reach out to me through the following channels:  
* **Email**: `abdulmoez123456789@gmail.com`

> I have also established a dedicated Discord group for more interactive communication:  
* **Discord Server**: `https://discord.gg/RMNcqzmt9f`


-----------

Buy Me a coffee
--------------
__If you'd like to show your support and appreciation for my work, you can buy me a coffee using the 
following payment option:__

**Payoneer**: `abdulmoez123456789@gmail.com`

> Your support is greatly appreciated and helps me continue providing valuable assistance and resources. 
Thank you for your consideration.

