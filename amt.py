"""
 *  date   : 2023/07/11
 *  Version : 0.5
 *  author : Abdul Moez (abdulmoez123456789@gmail.com)
 *  Study  : UnderGraduate in GCU Lahore, Pakistan
 *  https://github.com/Anonym0usWork1221/android-memorytool

"""

# !/usr/bin/env python
from androidMemoryTool import AndroidMemoryToolCLI, AndroidMemoryTool

def execute_cli():
    cli_tool = AndroidMemoryToolCLI(AndroidMemoryTool)
    cli_tool.cli_handler()

if __name__ == '__main__':
    execute_cli()
