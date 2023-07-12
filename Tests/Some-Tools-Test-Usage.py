import r2pipe


def disassemble_binary(binary_path):
    r2 = r2pipe.open(binary_path)
    r2.cmd("aaa")  # Analyze all functions

    functions = r2.cmdj("aflj")  # Get a list of functions

    pseudocode = ""
    for function in functions:
        r2.cmd("aaa")
        address = function['offset']
        r2.cmd(f"s {address}")
        pseudocode += r2.cmd(f"pdc\n")  # Generate pseudocode for each function

    r2.quit()
    return pseudocode


binary_path = "./c"
pseudocode = disassemble_binary(binary_path)
print(pseudocode)
