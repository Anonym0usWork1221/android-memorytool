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

from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
license = (this_directory / "LICENSE.md").read_text()
# with open("./requirements.txt", "r") as requirement_file:
#     tool_requirements = requirement_file.readlines()
#     requirement_file.close()

setup(
    name='androidMemoryTool',
    version='0.6',
    packages=["androidMemoryTool", "androidMemoryTool.WindowsAPI", "androidMemoryTool.LinuxAPI",
              "androidMemoryTool.CommonAPI"],
    license="GPL-3.0 license",
    author='Abdul Moez',
    author_email='abdulmoez123456789@gmail.com',
    description='Proficiently Managing Runtime RAM Memory for Windows, Android, and Linux Platforms',
    url='https://github.com/Anonym0usWork1221/android-memorytool',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown',
    data_files=[
        ('', ['LICENSE.md']),
    ],
    install_requires=['psutil'],
    entry_points={
        'console_scripts': ['amt=androidMemoryTool.__main__:execute_cli']
    },
    keywords=[
            'ps', 'top', 'kill', 'free', 'lsof', 'netstat', 'nice', 'tty',
            'ionice', 'uptime', 'taskmgr', 'process', 'df', 'iotop', 'iostat',
            'ifconfig', 'taskset', 'who', 'pidof', 'pmap', 'smem', 'pstree',
            'monitoring', 'ulimit', 'prlimit', 'smem', 'performance',
            'metrics', 'agent', 'observability', 'Memory Profiler', 'Memory Tool', 'Memory Leak Detection',
            'Cross-Platform Memory Analysis', 'Windows Memory Profiling', 'Linux Memory Monitoring',
            'Android Memory Analyzer', 'Memory Performance Metrics', 'Memory Optimization', 'Software Development Tool',
            'Memory Management', 'Memory Churn Analysis', 'Memory Profiling Library', 'Memory Debugging',
            'Resource Monitoring', 'Performance Metrics', 'Memory Analysis Software', 'Cross-Platform Development',
            'Memory Efficiency', 'Memory Improvement',
        ],
    python_requires=">=3.6",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: Microsoft :: Windows :: Windows 8",
        "Operating System :: Microsoft :: Windows :: Windows 7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
        "Topic :: Software Development :: Embedded Systems",
        "Topic :: System :: Operating System",
        "Topic :: System :: Systems Administration",
        "Topic :: Software Development :: Disassemblers",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Console",
    ],
)
