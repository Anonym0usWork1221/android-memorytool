from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
license = (this_directory / "LICENSE.md").read_text()

setup(
    name='androidMemoryTool',
    version='0.2',
    packages=['androidMemoryTool'],
    license=license,
    author='Abdul Moez',
    author_email='abdulmoez123456789@gmail.com',
    description='Read/Write android/linux Runtime RAM Memory',
    zip_safe=False,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
