from androidMemoryTool import AndroidMemoryToolCLI, AndroidMemoryTool

def execute_cli():
    cli_tool = AndroidMemoryToolCLI(AndroidMemoryTool)
    cli_tool.cli_handler()

if __name__ == '__main__':
    execute_cli()

