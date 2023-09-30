# from androidMemoryTool import AndroidMemoryTool, DataTypes, PMAP

# initialize tool.
# tool = AndroidMemoryTool(PKG="ac_client", TYPE=DataTypes.DWORD, SPEED_MODE=True, WORKERS=55,
#                          pMAP=PMAP(ALL=True))
# values = tool.read_value([20, 40], is_grouped=True, range_val=512)

# print(tool.get_pid("ac_client"))
# values = tool.read_value(100)
# founded_offsets = values[0]

# refined_address = tool.refiner_address(list_address=founded_offsets, value_to_refine=50)
# tool.read_lib('0x0', '0x100')
# tool.write_lib('0x0', '0x0', 10)

# pid = AndroidMemoryTool.get_pid("714")
# print(pid)

# if you are reading you will get tuple of two values offset list and total values found

# values = tool.read_value(100)
# founded_offsets = values[0]
# founded_values = values[1]
# print(founded_values)
# print(founded_offsets)


# if you are writing only return total value wrote
# values1 = tool.read_write_value(100, 10)
# print(values1)


# if you are reading lib offset only get the value at that place
# values1 = tool.read_lib(0x0, 0x100)
# print(values1)


# if you are writing lib offset only get the true/false at that place
# values1 = tool.write_lib(0x0, 0x100, 20)
# print(values1)

# dump = tool.raw_dump('client.so', '/home/kali/Documents/')
# print(dump)

# print(tool.read_value("19h"))

# Manually entered pid
# tool = AndroidMemoryTool(PKG=714, TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=True, WORKERS=55,
#                          pMAP=AndroidMemoryTool.PMAP(ALL=True))
# test_value = tool.read_value(42)
# print(test_value)

# to dump maps
# is_dumped = tool.dump_maps(path="./")
# print(is_dumped)

# utf8 lib tests
# tool = AndroidMemoryTool(PKG=662, TYPE=AndroidMemoryTool.DataTypes.UTF_8, SPEED_MODE=True, WORKERS=55,
#                          pMAP=AndroidMemoryTool.PMAP(ALL=True))
# off = tool.read_value("hi")
# print(off)

# off = tool.read_lib(0x5590fb61d8e2, 0x0, "hi")
# print(off)

# Hex pattern
# found_pattern = tool.find_hex_pattern("87 ?? 2B")
# for index in range(0, len(found_pattern[0])):
#     print(f"{found_pattern[0][index]}: {found_pattern[2][index]}")
# print(f"Total Pattern found: {found_pattern[1]}")

# Read Write Hex pattern
# found_pattern = tool.find_and_replace_hex_pattern("87 ?? 2B", "87 1D 2D")
# for index in range(0, len(found_pattern[0])):
#     print(f"{found_pattern[0][index]}: {found_pattern[2][index]}")
# print(f"Total Pattern found and replaced: {found_pattern[1]}")
