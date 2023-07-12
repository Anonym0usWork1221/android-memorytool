
import platform
import subprocess
import sys


def install_radare2():
    current_platform = platform.system()

    if current_platform == 'Linux':
        print(f"Platform Detected as {current_platform}: Installing Additional tools as sudo."
              f" By using apt-get method.")
        subprocess.check_call(['sudo', 'apt-get', 'update'])
        subprocess.check_call(['sudo', 'apt-get', 'install', 'radare2'])

    elif current_platform == 'Windows':
        install_path = 'C:\\Radare2\\'
        print(f"Platform Detected as {current_platform}: Installing Additional tools. Using Default directory as: "
              f"{install_path}")
        subprocess.check_call(['powershell', 'Invoke-WebRequest', '-Uri',
                               'https://github.com/radareorg/radare2/releases/latest/download/radare2_windows.zip',
                               '-OutFile', 'radare2.zip'])
        subprocess.check_call(
            ['powershell', 'Expand-Archive', '-Path', 'radare2.zip', '-DestinationPath', install_path])
        subprocess.check_call(['del', 'radare2.zip'], shell=True)
        subprocess.check_call(['setx', 'PATH', f'%PATH%;{install_path}'])

    elif current_platform == 'Android':
        print(f"Platform Detected as {current_platform}: Installing Additional tools. Assuming the tool is termux.")
        subprocess.check_call(['pkg', 'install', 'radare2'])

    else:
        print(f"Platform Detected as {current_platform}: Auto-installation of Additional tools is unsupported.")
        print("Please install Radare2 manually. And it is to environment variable")
        sys.exit(1)


try:
    import r2pipe
except ImportError:
    print("r2pipe not found. Installing Radare2...")
    install_radare2()
    try:
        import r2pipe
    except ImportError:
        print("Additional tools not found installing automatically...")
        sys.exit(1)

print("Radare2 and r2pipe successfully installed!")
