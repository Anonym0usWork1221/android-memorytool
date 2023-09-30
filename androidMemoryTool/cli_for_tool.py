"""
/*
 *  Date     : 2023/09/30
 *  Version  : 0.6
 *  Author   : Abdul Moez
 *  Email    : abdulmoez123456789@gmail.com
 *  Affiliation : Undergraduate at Government College University (GCU) Lahore, Pakistan
 *  GitHub   : https://github.com/Anonym0usWork1221/android-memorytool
 *
 *  Description:
 *  This code is governed by the GNU General Public License, version 3 or later.
 *  You should have received a copy of the GNU General Public License
 *  along with this program. If not, see <https://www.gnu.org/licenses/>.
 */
"""

# !/usr/bin/env python
import argparse


class AndroidMemoryToolCLI:
    """Command-line interface for the Android Memory Tool."""

    def __init__(self, android_tool: __build_class__):
        """
            Initialize the AndroidMemoryToolCLI.

            Args:
                android_tool: An instance of the AndroidMemoryTool class.
        """

        self._android_memory_tool = android_tool

    @staticmethod
    def _get_data_type(user_type):
        """
            Get the data type based on the user input.

            Args:
                user_type: The user input for the data type.

            Returns:
                The corresponding data type from the AndroidMemoryTool class.

            Raises:
                SystemExit: If the user_type is not a valid data type.
        """

        data_types = {
            "DWORD": "DWORD",
            "FLOAT": "FLOAT",
            "DOUBLE": "DOUBLE",
            "WORD": "WORD",
            "BYTE": "BYTE",
            "QWORD": "QWORD",
            "XOR": "XOR",
            "UTF_8": "UTF_8",
            "UTF_16LE": "UTF_16LE"
        }
        if user_type in data_types:
            return data_types[user_type]

        print("Unknown DataType: Available data types are:")
        print(" DWORD")
        print(" FLOAT")
        print(" DOUBLE")
        print(" WORD")
        print(" BYTE")
        print(" QWORD")
        print(" XOR")
        print(" UTF_8")
        print(" UTF_16LE")
        exit()

    def read_value(self, args):
        """
            Read a value from memory.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                The read value from memory.
        """

        value_to_read = self.convert_to_appropriate_type(args.read)
        data_type = self._get_data_type(args.type)
        tool = self._android_memory_tool(args.pkg, data_type, args.speed_mode, args.workers)
        result = tool.read_value(value_to_read)
        if result is not None:
            print(f"Read value: {result}")

    def read_write_value(self, args):
        """
            Read and write a value in memory.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                The read value from memory.
        """

        value_to_write = self.convert_to_appropriate_type(args.write_value)
        value_to_read = self.convert_to_appropriate_type(args.read)

        data_type = self._get_data_type(args.type)
        tool = self._android_memory_tool(args.pkg, data_type, args.speed_mode, args.workers)
        result = tool.read_write_value(value_to_read, value_to_write)
        if result is not None:
            print(f"Read value: {result}")

    @staticmethod
    def convert_to_appropriate_type(value):
        """
        Convert the input string to the appropriate type (float, int, or str).

        Args:
            value (str): The input value to be converted.

        Returns:
            The converted value as float, int, or str, depending on the content of the input.

        """
        try:
            converted_value = float(value)
            if converted_value.is_integer():
                return int(converted_value)
            else:
                return converted_value
        except (ValueError, TypeError):
            return value

    def write_lib(self, args):
        """
            Write a value to a library.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                A message indicating the write operation was successful.
        """

        value_to_write = self.convert_to_appropriate_type(args.write_value)
        data_type = self._get_data_type(args.type)
        tool = self._android_memory_tool(args.pkg, data_type)
        result = tool.write_lib(args.base_address, args.offset, value_to_write)
        if result is not None:
            print("Write successful")

    def read_lib(self, args):
        """
            Read a value from a library.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                The read value from the library.
        """

        value_to_read = self.convert_to_appropriate_type(args.value)
        data_type = self._get_data_type(args.type)
        tool = self._android_memory_tool(args.pkg, data_type)
        result = tool.read_lib(args.base_address, args.offset, value_to_read)
        if result is not None:
            print(f"Read value: {result}")

    def refiner_address(self, args):
        """
            Refine a list of addresses.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                The refined addresses.
        """

        value_to_refine = self.convert_to_appropriate_type(args.value_to_refine)
        data_type = self._get_data_type(args.type)
        tool = self._android_memory_tool(args.pkg, data_type, args.speed_mode, args.workers)
        result = tool.refiner_address(args.list_address, value_to_refine)
        if result is not None:
            print(f"Refined addresses: {result}")

    def get_module_base_address(self, args):
        """
            Get the base address of a module.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                The base address of the module.
        """
        tool = self._android_memory_tool(PKG=args.pid)
        pid = tool.get_pid()
        result = self._android_memory_tool.get_module_base_address(pid, args.module_name)
        if result is not None:
            print(f"Base address: {result}")

    def raw_dump(self, args):
        """
            Dump a library as raw binary.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                A message indicating the raw dump was successful.
        """

        tool = self._android_memory_tool(args.pkg)
        success = tool.raw_dump(args.lib_name, args.path)
        if success:
            print("Raw dump successful")

    def find_hex_pattern(self, args):
        """
            Find a hexadecimal pattern in memory.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                The addresses where the pattern was found.
        """

        data_type = self._get_data_type(args.type)
        tool = self._android_memory_tool(args.pkg, data_type, args.speed_mode, args.workers)
        result = tool.find_hex_pattern(args.hex_pattern)
        if result is not None:
            print(f"Pattern found at addresses: {result}")

    def find_and_replace_hex_pattern(self, args):
        """
            Find and replace a hexadecimal pattern in memory.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                The addresses where the pattern was replaced.
        """

        data_type = self._get_data_type(args.type)
        tool = self._android_memory_tool(args.pkg, data_type, args.speed_mode, args.workers)
        result = tool.find_and_replace_hex_pattern(args.search_pattern, args.replace_pattern)
        if result is not None:
            print(f"Pattern replaced at addresses: {result}")

    def dump_maps(self, args):
        """
            Dump memory maps.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                A message indicating the memory maps were dumped successfully.
        """

        tool = self._android_memory_tool(args.pkg)
        success = tool.dump_maps(args.path)
        if success:
            print("Maps dumped successfully")

    def get_pid(self, args):
        """
            Return the PID of a process.

            Args:
                args: The arguments parsed from the command-line.

            Prints:
                The PID of the process.
        """

        tool = self._android_memory_tool(PKG=args.pkg)
        pid = tool.get_pid()
        if tool:
            print(f"Pid of process: {pid}")

    def get_version(self):
        """
            Get the version information.

            Prints:
                The version and developer information.
        """

        version = self._android_memory_tool.get_version_code()
        developer = self._android_memory_tool.get_developer()
        print(f"Version: {version}\nDeveloper: {developer}")

    def parse_arguments(self):
        """
            Parse the command-line arguments.

            Returns:
                The parsed arguments.
        """

        parser = argparse.ArgumentParser(description="Android Memory Tool CLI")
        subparsers = parser.add_subparsers(title="subcommands", dest="command")

        # Read value command
        read_value_parser = subparsers.add_parser("read_value", help="Read a value from memory")
        read_value_parser.add_argument("pkg", type=str, help="Package name or PID")
        read_value_parser.add_argument("type", type=str, help="Data type")
        read_value_parser.add_argument("speed_mode", type=bool, help="Speed mode")
        read_value_parser.add_argument("workers", type=int, help="Number of workers")
        read_value_parser.add_argument("read", type=str, help="Value to read")
        read_value_parser.set_defaults(func=self.read_value)

        # Read-write value command
        read_write_value_parser = subparsers.add_parser("read_write_value", help="Read and write a value in memory")
        read_write_value_parser.add_argument("pkg", type=str, help="Package name or PID")
        read_write_value_parser.add_argument("type", type=str, help="Data type")
        read_write_value_parser.add_argument("speed_mode", type=bool, help="Speed mode")
        read_write_value_parser.add_argument("workers", type=int, help="Number of workers")
        read_write_value_parser.add_argument("read", type=str, help="Value to read")
        read_write_value_parser.add_argument("write", type=str, help="Value to write")
        read_write_value_parser.set_defaults(func=self.read_write_value)

        # Write lib command
        write_lib_parser = subparsers.add_parser("write_lib", help="Write a value to a library")
        write_lib_parser.add_argument("pkg", type=str, help="Package name or PID")
        write_lib_parser.add_argument("type", type=str, help="Data type")
        write_lib_parser.add_argument("base_address", type=str, help="Base address")
        write_lib_parser.add_argument("offset", type=str, help="Offset")
        write_lib_parser.add_argument("write_value", type=str, help="Value to write")
        write_lib_parser.set_defaults(func=self.write_lib)

        # Read lib command
        read_lib_parser = subparsers.add_parser("read_lib", help="Read a value from a library")
        read_lib_parser.add_argument("pkg", type=str, help="Package name or PID")
        read_lib_parser.add_argument("type", type=str, help="Data type")
        read_lib_parser.add_argument("base_address", type=str, help="Base address")
        read_lib_parser.add_argument("offset", type=str, help="Offset")
        read_lib_parser.add_argument("--value", type=str, help="Value to compare")
        read_lib_parser.set_defaults(func=self.read_lib)

        # Refiner address command
        refiner_address_parser = subparsers.add_parser("refiner_address", help="Refine a list of addresses")
        refiner_address_parser.add_argument("pkg", type=str, help="Package name or PID")
        refiner_address_parser.add_argument("type", type=str, help="Data type")
        refiner_address_parser.add_argument("speed_mode", type=bool, help="Speed mode")
        refiner_address_parser.add_argument("workers", type=int, help="Number of workers")
        refiner_address_parser.add_argument("list_address", nargs="+", type=str, help="List of addresses")
        refiner_address_parser.add_argument("value_to_refine", type=str, help="Value to refine")
        refiner_address_parser.set_defaults(func=self.refiner_address)

        # Get module base address command
        get_module_base_address_parser = subparsers.add_parser("get_module_base_address",
                                                               help="Get the base address of a module")
        get_module_base_address_parser.add_argument("pid", type=str, help="Package name or Process ID")
        get_module_base_address_parser.add_argument("module_name", type=str, help="Module name")
        get_module_base_address_parser.set_defaults(func=self.get_module_base_address)

        # Raw dump command
        raw_dump_parser = subparsers.add_parser("raw_dump", help="Dump a library as raw binary")
        raw_dump_parser.add_argument("pkg", type=str, help="Package name or PID")
        raw_dump_parser.add_argument("lib_name", type=str, help="Library name")
        raw_dump_parser.add_argument("path", type=str, help="Output path (default: current directory)", nargs="?",
                                     default="./")
        raw_dump_parser.set_defaults(func=self.raw_dump)

        # Find hex pattern command
        find_hex_pattern_parser = subparsers.add_parser("find_hex_pattern", help="Find a hexadecimal pattern in memory")
        find_hex_pattern_parser.add_argument("pkg", type=str, help="Package name or PID")
        find_hex_pattern_parser.add_argument("type", type=str, help="Data type")
        find_hex_pattern_parser.add_argument("speed_mode", type=bool, help="Speed mode")
        find_hex_pattern_parser.add_argument("workers", type=int, help="Number of workers")
        find_hex_pattern_parser.add_argument("hex_pattern", type=str, help="Hexadecimal pattern to find")
        find_hex_pattern_parser.set_defaults(func=self.find_hex_pattern)

        # Find and replace hex pattern command
        find_and_replace_hex_pattern_parser = subparsers.add_parser("find_and_replace_hex_pattern",
                                                                    help="Find and replace a hexadecimal pattern in memory")
        find_and_replace_hex_pattern_parser.add_argument("pkg", type=str, help="Package name or PID")
        find_and_replace_hex_pattern_parser.add_argument("type", type=str, help="Data type")
        find_and_replace_hex_pattern_parser.add_argument("speed_mode", type=bool, help="Speed mode")
        find_and_replace_hex_pattern_parser.add_argument("workers", type=int, help="Number of workers")
        find_and_replace_hex_pattern_parser.add_argument("search_pattern", type=str,
                                                         help="Hexadecimal pattern to search for")
        find_and_replace_hex_pattern_parser.add_argument("replace_pattern", type=str,
                                                         help="Hexadecimal pattern to replace with")
        find_and_replace_hex_pattern_parser.set_defaults(func=self.find_and_replace_hex_pattern)

        # Dump maps command
        dump_maps_parser = subparsers.add_parser("dump_maps", help="Dump memory maps")
        dump_maps_parser.add_argument("pkg", type=str, help="Package name or PID")
        dump_maps_parser.add_argument("--path", type=str, help="Output path (default: current directory)", nargs="?",
                                      default="./")
        dump_maps_parser.set_defaults(func=self.dump_maps)

        # get pid command
        get_pid_parser = subparsers.add_parser("get_pid", help="Return the pid of process")
        get_pid_parser.add_argument("pkg", type=str, help="Package name")
        get_pid_parser.set_defaults(func=self.get_pid)

        # Help command
        help_parser = subparsers.add_parser("help", help="Display help information")
        help_parser.add_argument("command", type=str, help="Command to get help for", nargs="?")
        help_parser.set_defaults(func=self.display_help)

        # Get version
        parser.add_argument("-v", "--version", help="Return Version of tool", action="store_true")
        return parser.parse_args()

    @staticmethod
    def display_help(args):
        """
            Display help information for a command or general help information.

            Args:
                args: The parsed command-line arguments.

            Returns:
                None.
        """

        if args.command:
            print("Help for command:", args.command)
            print("-" * 50)
            # Added help information for each command
            if args.command == "read_value":
                print("Command: read_value")
                print("Description: Read a value from memory")
                print("Usage: read_value <pkg> <type> <speed_mode> <workers> <read>")
                print("\nParameters:")
                print("  <pkg>        Package name or PID")
                print("  <type>       Data type")
                print("  <speed_mode> Speed mode (True or False)")
                print("  <workers>    Number of workers")
                print("  <read>       Value to read")
            elif args.command == "read_write_value":
                print("Command: read_write_value")
                print("Description: Read and write a value in memory")
                print("Usage: read_write_value <pkg> <type> <speed_mode> <workers> <read> <write>")
                print("\nParameters:")
                print("  <pkg>        Package name or PID")
                print("  <type>       Data type")
                print("  <speed_mode> Speed mode (True or False)")
                print("  <workers>    Number of workers")
                print("  <read>       Value to read")
                print("  <write>      Value to write")
            elif args.command == "write_lib":
                print("Command: write_lib")
                print("Description: Write a value to a library")
                print("Usage: write_lib <pkg> <type> <speed_mode> <workers> <base_address> <offset> <write_value>")
                print("\nParameters:")
                print("  <pkg>           Package name or PID")
                print("  <type>          Data type")
                print("  <base_address>  Base address")
                print("  <offset>        Offset")
                print("  <write_value>   Value to write")
            elif args.command == "read_lib":
                print("Command: read_lib")
                print("Description: Read a value from a library")
                print("Usage: read_lib <pkg> <type> <speed_mode> <workers> <base_address> <offset> [--value <value>]")
                print("\nParameters:")
                print("  <pkg>           Package name or PID")
                print("  <type>          Data type")
                print("  <base_address>  Base address")
                print("  <offset>        Offset")
                print("  --value         Value to compare (optional)")
            elif args.command == "refiner_address":
                print("Command: refiner_address")
                print("Description: Refine a list of addresses")
                print("Usage: refiner_address <pkg> <type> <speed_mode> <workers> <list_address> <value_to_refine>")
                print("\nParameters:")
                print("  <pkg>              Package name or PID")
                print("  <type>             Data type")
                print("  <speed_mode>       Speed mode (True or False)")
                print("  <workers>          Number of workers")
                print("  <list_address>     List of addresses")
                print("  <value_to_refine>  Value to refine")
            elif args.command == "get_module_base_address":
                print("Command: get_module_base_address")
                print("Description: Get the base address of a module")
                print("Usage: get_module_base_address <pid> <module_name>")
                print("\nParameters:")
                print("  <pid>          Package name or Process ID")
                print("  <module_name>  Module name")
            elif args.command == "raw_dump":
                print("Command: raw_dump")
                print("Description: Dump a library as raw binary")
                print("Usage: raw_dump [<path>] <lib_name>")
                print("\nParameters:")
                print("  <pkg>        Package name or PID")
                print("  <lib_name>   Library name")
                print("  <path>       Output path (default: current directory)")
            elif args.command == "find_hex_pattern":
                print("Command: find_hex_pattern")
                print("Description: Find a hexadecimal pattern in memory")
                print("Usage: find_hex_pattern <pkg> <type> <speed_mode> <workers> <hex_pattern>")
                print("\nParameters:")
                print("  <pkg>           Package name or PID")
                print("  <type>          Data type")
                print("  <speed_mode>    Speed mode (True or False)")
                print("  <workers>       Number of workers")
                print("  <hex_pattern>   Hexadecimal pattern to find")
            elif args.command == "find_and_replace_hex_pattern":
                print("Command: find_and_replace_hex_pattern")
                print("Description: Find and replace a hexadecimal pattern in memory")
                print("Usage: find_and_replace_hex_pattern <pkg> <type> <speed_mode> <workers> "
                      "<search_pattern> <replace_pattern>")
                print("\nParameters:")
                print("  <pkg>             Package name or PID")
                print("  <type>            Data type")
                print("  <speed_mode>      Speed mode (True or False)")
                print("  <workers>         Number of workers")
                print("  <search_pattern>  Hexadecimal pattern to search for")
                print("  <replace_pattern> Hexadecimal pattern to replace with")
            elif args.command == "dump_maps":
                print("Command: dump_maps")
                print("Description: Dump memory maps")
                print("Usage: dump_maps <pkg> <type> <speed_mode> <workers> [--path <path>]")
                print("\nParameters:")
                print("  <pkg>        Package name or PID")
                print("  --path       Output path (default: current directory)")
            elif args.command == "dump_maps":
                print("Command: dump_maps")
                print("Description: Dump memory maps")
                print("Usage: dump_maps <pkg> <type> <speed_mode> <workers> [--path <path>]")
                print("\nParameters:")
                print("  <pkg>        Package name or PID")
                print("  --path       Output path (default: current directory)")

            elif args.command == "get_pid":
                print("Command: get_pid")
                print("Description: Return pid of process")
                print("Usage: get_pid <pkg>")
                print("\nParameters:")
                print("  <pkg>        Package name")

            else:
                print("Error: Unknown command:", args.command)
                return
        else:
            print("General help information")
            print("-" * 50)
            print("Available commands:")
            print("  find_hex_pattern       Find a hexadecimal pattern in memory")
            print("  read_write_value       Read and write a value in memory")
            print("  raw_dump               Dump a library as raw binary")
            print("  read_lib               Read a value from a library")
            print("  write_lib              Write a value to a library")
            print("  refiner_address        Refine a list of addresses")
            print("  read_value             Read a value from memory")
            print("  get_pid                Returns pid of process")
            print("  dump_maps              Dump memory maps")
            print("  get_module_base_address Get the base address of a module")
            print("  find_and_replace_hex_pattern  Find and replace a hexadecimal pattern in memory")

    def cli_handler(self):
        """
        Handle the command-line interface (CLI) for the Android Memory Tool.

            This function parses the command-line arguments using the `parse_arguments` method.
            It then checks if the `--version` flag is set and calls the `get_version`
            method to display the version information.
            If no command is provided, it calls the `display_help` method to show general help information.
            Otherwise, it calls the appropriate method based on the command specified in the arguments.

            Args:
                self: The current instance of the `AndroidMemoryToolCLI` class.

            Returns:
                None.
        """
        args = self.parse_arguments()

        if args.version:
            self.get_version()
        elif args.command is None:
            self.display_help(args)
        else:
            args.func(args)

# def execute_cli():
#     from androidMemoryTool import AndroidMemoryTool
#     cli_tool = AndroidMemoryToolCLI(AndroidMemoryTool)
#     cli_tool.cli_handler()
#
# if __name__ == '__main__':
#     execute_cli()
