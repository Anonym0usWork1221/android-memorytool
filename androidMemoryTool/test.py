from .androidMemoryTool import AndroidMemoryTool
import .androidMemoryTool
# initialize tool

androidMemoryTool.SettingUpTool().init_setup(PKG="ac_client", TYPE=androidMemoryTool.DataTypes.DWORD,
                                             SPEED_MODE=True, WORKERS=55)

# set True to maps you want to use
androidMemoryTool.InitMemoryTool().init_tool(pMAP=androidMemoryTool.PMAP(ALL=True, C_ALLOC=True, C_DATA=False
                                                                         , C_HEAP=False, CODE_APP=False, C_BSS=True
                                                                         , JAVA_HEAP=False, J_Java=False, CODE_SYSTEM=False
                                                                         , A_ANONYMOUS=True, ASHMEM=False, STACK=False
                                                                         , B_BAD=False))


# if you are reading you will get tuple of two values offset list and total values found

values = AndroidMemoryTool.read_value(100)

founded_offsets = values[0]
founded_values = values[1]
print(founded_offsets)

# if you are writing only return total value wrote

values1 = AndroidMemoryTool.read_write_value(100, 10)
print(values1)
