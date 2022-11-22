from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
license = (this_directory / "LICENSE.md").read_text()

setup(
    name='androidMemoryTool',
    version='0.4',
    packages=["androidMemoryTool"],
    license="GPL-3.0 license",
    author='Abdul Moez',
    author_email='abdulmoez123456789@gmail.com',
    description='Read/Write android/linux Runtime RAM Memory',
    url='https://github.com/Anonym0usWork1221/android-memorytool',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown',
    data_files=[
        ('', ['LICENSE.md']),
    ],
    install_requires=['wheel'],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Disassemblers",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Console",
    ],
)
