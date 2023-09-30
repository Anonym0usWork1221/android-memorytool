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
from androidMemoryTool import AndroidMemoryToolCLI, AndroidMemoryTool


def execute_cli():
    cli_tool = AndroidMemoryToolCLI(AndroidMemoryTool)
    cli_tool.cli_handler()


if __name__ == '__main__':
    execute_cli()
