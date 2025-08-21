def check_syntax(file_path, return_output=False):
    try:
        with open(file_path, "r") as f:
            code = f.read()
        compile(code, file_path, "exec")
        msg = f"{file_path}: No Syntax Errors Found"
    except SyntaxError as e:
        # Read file lines to show context
        with open(file_path, "r") as f:
            lines = f.readlines()
        error_line = lines[e.lineno - 1] if e.lineno - 1 < len(lines) else ""
        pointer = " " * (e.offset - 1 if e.offset else 0) + "^"
        msg = (
            f"{file_path}: Syntax Error\n"
            f"Line {e.lineno}: {error_line.strip()}\n"
            f"       {pointer}\n"
            f"Error: {e.msg}"
        )
    except Exception as e:
        msg = f"{file_path}: Unexpected Error → {e}"

    print(msg)
    return msg if return_output else None


def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m syntax_checker.checker <file1.py> <file2.py> ...")
        return
    for file_path in sys.argv[1:]:
        check_syntax(file_path)


if __name__ == "__main__":
    main()
