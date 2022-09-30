from androidMemoryTool import AndroidMemoryTool

# initialize tool
tool = AndroidMemoryTool(PKG="ac_client", TYPE=AndroidMemoryTool.DataTypes.DWORD, SPEED_MODE=False, WORKERS=55,
                         pMAP=AndroidMemoryTool.PMAP(ALL=True))

# tool.raw_dump('client.dll')
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

dump = tool.raw_dump('client.so', '/home/kali/Documents/')
print(dump)
