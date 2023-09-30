# In this update you need to load PMAP and DataTypes separately from androidMemoryTool
# PMAP only work with Linux and Android.
# (Work on all Linux, Android and Windows)
from androidMemoryTool import AndroidMemoryTool, DataTypes, PMAP

# Initialize the tool set the speed_mode to off for working on Windows in this version only.
# (Work on all Linux, Android and Windows)
tool = AndroidMemoryTool(PKG="Tutorial-x86_64.exe",
                         SPEED_MODE=False,
                         TYPE=DataTypes.DWORD,
                         # half of cores available in operating system
                         WORKERS=AndroidMemoryTool.get_cpu_counts(fraction=2),
                         pMAP=PMAP(ALL=True)  # This will not affect windows search rage
                         )
# Don't use speed mode on group search on WindowsAPI there is bug in threads in Windows api
# Group search get value list which contain list of addresses and total number of addresses in it
# (Work on all Linux, Android and Windows)
tool.read_value(read=[1000, 100], is_grouped=True, range_val=510)  # by default range_val=512 (adjust as you like)

# Find hex pattern in memory (Not available for widows in this update (0.6)
tool.find_hex_pattern(search_pattern='8A ?? 2B')
# Find hex pattern and replace it with new pattern in memory (Not available for widows in this update (0.6)
tool.find_and_replace_hex_pattern(search_pattern='8A ?? 3B', replace_pattern='88 22 3B')
# Search for some value in whole memory (Work on all Linux, Android and Windows)
tool.read_value(read=100)
# Get base address of some dll in windows and lib in linux and android (Work on all Linux, Android and Windows)
tool.get_module_base_address(module_name="ntdll.dll")
# Read the address value of some offset (Work on all Linux, Android and Windows)
tool.read_lib(base_address='015E24F8', offset='0x0')
# Write the address value of some offset (Work on all Linux, Android and Windows)
tool.write_lib(base_address='015E24F8', offset='0x0', write_value=1000)
# Dump the memory of some dlls or libs (Work on all Linux, Android and Windows)
tool.raw_dump(lib_name="ntdll.dll")
# Refine address and get new value from old address (Work on all Linux, Android and Windows)
tool.refiner_address(list_address=[], value_to_refine=97)
# Just Search all values and replace all with new value (Work on all Linux, Android and Windows)
tool.read_write_value(read=100, write=200)
# Dump the memory maps (Work on all Linux, Android and Windows)
tool.dump_maps()
# Get the pid of process by their name (Work on all Linux, Android and Windows)
tool.get_pid()

# --- Static methods (From 0.6 version to onward) ---
# Name of developer
print(AndroidMemoryTool.get_developer())
# Version of Tool
print(AndroidMemoryTool.get_version_code())
# Number of cores available on your device
print(AndroidMemoryTool.get_cpu_counts())
# Known Platform = ['Android', 'Linux', 'Windows'] (Get Non-supported message if platform is
# not supported by script on verbose=True)
print(AndroidMemoryTool.get_platform(verbose=True))
# Check if the script running on rooted terminal or non-rooted
print(AndroidMemoryTool.is_root_acquired())


# Get the Memory profiler (you can customize it for that read the Profiler Documentation)
# (Work on all Linux, Android and Windows)
memory_profiler = tool.get_memory_profiler()
# Run the profiler by default configurations
memory_profiler.start_profiling(logging=False)  # Logging will disable saving output in file


