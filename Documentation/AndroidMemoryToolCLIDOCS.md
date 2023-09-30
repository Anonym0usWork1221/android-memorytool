AndroidMemoryToolCLIDOCS
-----

The Android Memory Tool CLI is a command-line interface for the Android Memory Tool. It provides various commands to interact with memory in Android applications.
> Supported Platforms -> Linux, Android and Windows (Required Administer Permission)

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
* For Windows (Required Administer Permission CMD):
```
python -m androidMemoryTool <command> [options]
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
Replace `[command]` with the desired command to get help for that command. If no command is provided, general help information will be displayed.
