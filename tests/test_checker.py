import os
import tempfile
from py_syntax_checker.checker import check_syntax

def test_valid_code():
    code = 'print("Hello World")'
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as f:
        f.write(code)
        f_name = f.name
    output = check_syntax(f_name, return_output=True)
    os.remove(f_name)
    assert "No Syntax Errors Found" in output

def test_invalid_code():
    code = 'print("Hello World"'
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w") as f:
        f.write(code)
        f_name = f.name
    output = check_syntax(f_name, return_output=True)
    os.remove(f_name)
    assert "Syntax Error" in output
