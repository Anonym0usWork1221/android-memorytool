AndroidMemoryTool
====


AndroidMemoryTool is a memory reader and writer tool designed for android and linux os's 
.This Tool is written in python using ctypes not affective as c.
If you find any bug or not working function you can contact me. 

 *  @date   : 2022/03/23
 *  @author : Abdul Moez
 *  @Study  : UnderGraduate in GCU Lahore, Pakistan
 *  @repos  :(https://github.com/Anonym0usWork1221/android-memorytool)
 MIT License

 Copyright (c) 2022 AbdulMoez

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


Requirments
-----------
No additional libraries need this tool si made with python built-in libraries

* Needed python version 3.x

* Android Requirments -> Rooted Device Needed

Installation, Documentation and Examples
----------------------------------------

This module of python is not fully completed yet. As a result i did not make its proper package.
Simple clone this repo and import in your project for usage.

Memort Tool with some examples which can be found in the `examples` folder.

## Usage
1. import the module and grab process id of target process.

For Linux os
```py
import androidMemoryTool

pid = androidMemoryTool.get_pid("ac_client")
```

For Android os use packagename of target application
```py
import androidMemoryTool

pid = androidMemoryTool.get_pid("com.jaratools.org")
```

2. After getting PID we are ready to read or write target process memory
Next steps are sath for both os's

```py
values_replaced = androidMemoryTool.write_dword_all(pid, 23, 100)

print(values_replaced)
```

3. Read process memory

```py
import androidMemoryTool

pid = androidMemoryTool.get_pid("ac_client")

offsets, total_values_found = androidMemoryTool.read_xor_all(pid, 23)

print(offsets[0], total_values_found)
```

4. Read direct lib offsets
```py
import androidMemoryTool

pid = androidMemoryTool.get_pid("com.somegame.org")
base_addr = androidMemoryTool.get_module_base_address(pid, "libUE4.so")
read = androidMemoryTool.read_lib_offsets_DOUBLE(pid, base_addr, 0xfff)
print(read)
```

4. Write direct lib offsets
```py
import androidMemoryTool

pid = androidMemoryTool.get_pid("com.somegame.org")
base_addr = androidMemoryTool.get_module_base_address(pid, "libUE4.so")
androidMemoryTool.write_lib_offsets_DOUBLE(pid, base_addr, 0xfff, 23)

```

this will find all the values realated to your search and replace them with replaced value
and return the number of values it changed

Supported Data Types
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


Assistance
----------
If you need assistance, you can ask for help on my mailing list:

* Email      : abdulmoez123456789@gmail.com

I also created a Discord group:

* Server     : https://discord.gg/RMNcqzmt9f


## Contributors

Feel free to contibute on this project.


Buy Me a coffe
--------------
If you want to support me you can buy me coffe.

BitCoin_addr: ``` 19vwfRXfthPY7f2aqDBpxQvZa6AJFKcdBS ```


