# Detailed Documentation
**__Supported Data__**
----------------------

* **__Supported Maps__**  

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

* **__Supported Data Types__**  
__All data types are signed.__  

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

**__Classes__**
----------------------
* **AndroidMemoryTool**: AndroidMemoryTool is the only main class in androidMemoryTool package which is based on **__Multilevel Inheritance__**

**__Return Types & Parameters of Functions__**
----------------------
1. **_read_value()_** (SPEED_MODE_OFF): 
   * Return Types: **None** or **list([offsets, total_values_found])**  
   * Parameters: **read**: any value according to chosen data type (e.g: UTF_8, UTF_16E = String | DWORD, WORD, BYTE, QWORD, XOR=int, FLOAT, DOUBLE=float). If you got value in hex in add h after hex ``read="9D5h""``. Hex supports data types (Float, Dword, Double).  
     
2. **_read_value()_** (SPEED_MODE_ON): 
   * Return Types: **None** or **tuple[list[offsets], total_values_found]**
   * Parameters: **read**: any value according to chosen data type (e.g: UTF_8, UTF_16E = String | DWORD=int, FLOAT=float etc). If you got value in hex in add h after hex ``read="9D5h""``. Hex supports data types (Float, Dword, Double).  
   
3. **_read_write_value()_** (SPEED_MODE_ON/OFF): 
   * Return Types: **None** or **int(total_values_replaced)**
   * Parameters:   
     **read**: any value to read according to chosen data type. If you got value in hex in add h after hex ``read="9D5h""``. Hex supports data types (Float, Dword, Double).    
     **write**: any value to write according to chosen data type. If you got value in hex in add h after hex ``write="9D5h""``. Hex supports data types (Float, Dword, Double).
   
4. **_write_lib()_**:
   * Return Types: **None** or **bool(True/False)**
   * Parameters:   
     **base_address**: Starting Address of lib,   
     **offset**: The Offset from starting address,  
     **write_value**: The Value according to chosen data type to replace on that address

5. **_read_lib()_**:  
   * Return Types: **None** or **any(founded_value_on_address)**
   * Parameters:   
     **base_address**: Starting Address of lib,   
     **offset**: The Offset from starting address,  
     **value**: The Value parameter is an optional parameter it is use for reading UTF_8 and UTF_16E. It takes either length of word or word itself. ``value="hello"`` or ``value=5``

6. **_refiner_address()_**: 
   * Return Types: **None** or **list(refined_address)**
   * Parameters:   
     **list_address**: The list of address returned by read_value() function,   
     **value_to_refine**: The changed value in returned address list

7. **_get_module_base_address()_**: 
   * Return Types: **None** or **hex_str(base_address)**
   * Parameters:  
     **pid**: THe process id,   
     **module_name**: lib_name

8. **_raw_dump()_**: 
   * Return Types: **bool(True/False)**
   * Parameters:  
     **lib_name**: **module name** to dump or **manually** pass dump section address (startAddress-endAddress)
     **path**: This is an optional parameter used for specify output path (default="./")   

9. **_find_hex_pattern()_** (SPEED_MODE_ON/OFF): 
   * Return Types: **list([offsets, total_values_found, founded_patterns])**
   * Parameters:  
     **hex_pattern**: Hex pattern to find (e.g: 89 ?? 79) the unknown hex must be ??. 

10. **_dump_maps()_**: 
    * Return Types: **bool(True/False)**
    * Parameters:  
     **path**: This is an optional parameter used for specify output path (default="./").  

11. **_get_pid()_**: 
    * Return Types: **str(PID)**
    * Parameters:  
     **pkg**: PACKAGE parameter is necessary to create an object you can pass the name of a process or PID of a process to initialize the tool ``PKG="ac_client"`` or ``PKG=714``.


**__Import__**
----------------------
* **_Import_**: As there is only one Main class in androidMemoryTool we will import it as follows.
```python
from androidMemoryTool import AndroidMemoryTool
```

**__Initialization/Object__**
----------------------
To use this tool we need to create an object of AndroidMemoryTool.  
```python 
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.UTF_8, SPEED_MODE=True, WORKERS=55,
                         pMAP=AndroidMemoryTool.PMAP(ALL=True))
```
* **PKG**: PACKAGE parameter is necessary to create an object you can pass the name of a process or PID of a process to initialize the tool
  ``PKG="ac_client"`` or ``PKG=714``.
* **TYPE**: TYPE parameter is necessary to create an object you can pass the DataTypes from the above table of supported data types.
  ``TYPE=AndroidMemoryTool.DataTypes.DWORD`` or ``TYPE=AndroidMemoryTool.DataTypes.FLOAT`` Just change the name of the DataType as given in above table.
* **SPEED_MODE**: SPEED_MODE is an optional parameter used to speed up process by threading it can be either True (toActive) or False (toDeactivate). By default, it is False.
  ``SPEED_MODE=True`` or ``SPEED_MODE=False``.
* **WORKERS**: WORKERS is an optional parameter used to set up the total Threads on speeding up process by default it is 55. Only used if SPEED_MODE is enabled.
* **pMAP**: pMAP is an optional parameter used to set up MAPS. By default, it is set on ALL memory region. Maps are the memory regions inside the Linux OS. ALL is slow as it scan whole Memory of current process.
  If you want to change maps or want to use multiple maps you need to False (Off) the ALL memory region. You can use the multiple maps ranges as follows. Names are same as given in supported MAPS table above.  
    ```python 
    tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.UTF_8, SPEED_MODE=True, WORKERS=55,
                             pMAP=AndroidMemoryTool.PMAP(ALL=False, C_ALLOC=True, C_HEAP=True))
    ```

**__READ_FROM_MEMORY__**
----------------------
After initializing or creating an object of AndroidMemoryTool class we are ready to reading from memory according to the **DataType** and **Map** we specified in tool.
     
* **_DWORD_**  
  To read DWORD data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(100)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```

* **_FLOAT_**  
  To read FLOAT data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.FLOAT, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(100.0)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```

* **_DOUBLE_**  
  To read DOUBLE data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool

tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DOUBLE, SPEED_MODE=True, WORKERS=55,
                         pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(1001.4)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```

* **_WORD_**  
  To read WORD data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.WORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(10)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```

* **_DWORD_**  
  To read DWORD data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(100)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```

* **_BYTE_**  
  To read BYTE data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(120)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```
* **_QWORD_**  
  To read QWORD data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.UTF_16LE, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(9743264348)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```

* **_XOR_**  
  To read XOR data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.XOR, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(2147)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```

* **_UTF_8_**  
  To read UTF_8 data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.UTF_8, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value("Hello")
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```

* **_UTF_16LE_**  
  To read UTF_16LE data type we specify the DataType and Maps and call **_read_value_** function in **_tool_** object  
  **read_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.QWORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value("hell")
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```


**__WRITE_TO_MEMORY__**
----------------------
After initializing/creating an object of AndroidMemoryTool class we are ready to write to memory according to the **DataType** and **Map** we specified in tool.
     
* **_DWORD_**  
  To read DWORD data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value(100, 20)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```

* **_FLOAT_**  
  To read FLOAT data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.FLOAT, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value(100.0, 20.0)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```

* **_DOUBLE_**  
  To read DOUBLE data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool

tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DOUBLE, SPEED_MODE=True, WORKERS=55,
                         pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value(1001.4, 20.0)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```

* **_WORD_**  
  To read WORD data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.WORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value(10, 20)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```

* **_DWORD_**  
  To read DWORD data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value(100, 20)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```

* **_BYTE_**  
  To read BYTE data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value(120, 20)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```

* **_XOR_**  
  To read XOR data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.XOR, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value(2147, 20)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```

* **_UTF_8_**  
  To read UTF_8 data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.UTF_8, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value("Hello", "King")
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```

* **_UTF_16LE_**  
  To read UTF_16LE data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.QWORD, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value("hell", "nah")
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
 ```

* **_QWORD_**  
  To read QWORD data type we specify the DataType and Maps and call **_read_write_value_** function in **_tool_** object  
  **read_write_value**
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.UTF_16LE, SPEED_MODE=True, WORKERS=55,
                      pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_write_value(484845, 20)
print(f"offsets: {values[0]}")
print(f"Total values found: {values[1]}")
```




**__READ_FROM_ADDRESS__**
----------------------
In reading from address we need pid and the base address of lib. If ou have your own full address you can use it. Then we add offset from base address. If the address is complete put base address as 0x0.
We need to specify what data type is of the address and for that we need to initialize the tool.
If we want to read UTF_8 or UTF_16E we can use optional parameter named value. It takes either the string or length of string we want to read.
like ``value="hello`` or ``value=5``
As example given below.
```python
from androidMemoryTool import AndroidMemoryTool
pid = AndroidMemoryTool.get_pid('ac_client')
base_addr = AndroidMemoryTool.get_module_base_address(pid, "client.so")
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD)
values1 = tool.read_lib(base_addr, 0xfff150d, value=None)
print(values1)
```

**__WRITE_TO_ADDRESS__**
----------------------
In writing to address we need pid and the base address of lib. If ou have your own full address you can use it. Then we add offset from base address. If the address is complete put base address as 0x0.
We need to specify what data type is of the address and for that we need to initialize the tool. We need to specify the write parameter to replace value. 
As given below.
```python
from androidMemoryTool import AndroidMemoryTool
pid = AndroidMemoryTool.get_pid('ac_client')
base_addr = AndroidMemoryTool.get_module_base_address(pid, "client.so")
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD)
values1 = tool.write_lib(base_addr, 0xfff150d, 58)
print(values1)
```



**__GETTING_PROCESS_ID__**
----------------------
Sometimes we need to fetch pid of some process we can use following function to fetch it.
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool.get_pid('ac_client') # for android use package name e.g(com.app.org)
print(tool)
```

**__GETTING_LIB/MODULE_BASE_ADDRESS__**
----------------------
We can get the module base address by get_module_base_address() function as follows
```python
from androidMemoryTool import AndroidMemoryTool
pid = AndroidMemoryTool.get_pid('ac_client')
base_addr = AndroidMemoryTool.get_module_base_address(pid, "client.so")
print(base_addr)
```


**__ADDRESS_REFINER__**
----------------------
If we want to check if any value is changed from previous fetched list of address we can use refiner function and pass list of address and new changed value as follows
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=False, WORKERS=55,
                     pMAP=AndroidMemoryTool.PMAP(ALL=True))
values = tool.read_value(100)
founded_offsets = values[0]
refined_address = tool.refiner_address(list_address=founded_offsets, value_to_refine=50)
print(refined_address)
```



**__MEMORY_DUMPER__**
----------------------
You can also dump specific area or any lib by using raw_dump() function you can specify either lib name or give starting address and ending address separated by hyphen(-)

```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client")
dump = tool.raw_dump(lib_name='client.so', path='/home/kali/Documents/')
print(dump) # True or False
```
OR

```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client")
dump = tool.raw_dump(lib_name='198d77a4-298d77a4', path='/home/kali/Documents/')
print(dump) # True or False
```



**__FIND_HEX_PATTERN__**
----------------------
You can also find some specific hex patterns from memory by using find_hex_pattern() function as follows
It needs MAP and SPEED_MODE if you want else disable it.

```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG=662, SPEED_MODE=True, WORKERS=55,
                         pMAP=AndroidMemoryTool.PMAP(ALL=True))
found_pattern = tool.find_hex_pattern("87 ?? 2B")
for index in range(0, len(found_pattern[0])):
    print(f"{found_pattern[0][index]}: {found_pattern[2][index]}")
print(f"Total Pattern found: {found_pattern[1]}")
```


**__DUMP_MAPS__**
----------------------
You can dump map file to some path using dump_map() function as follows
```python
from androidMemoryTool import AndroidMemoryTool
tool = AndroidMemoryTool(PKG="ac_client")
is_dumped = tool.dump_maps(path="./")
print(is_dumped)
```
