# py-syntax-checker
A comprehensive Python syntax checker that offers a range of useful features, including batch scanning, integration with Git's pre-commit hook and a user-friendly graphical interface. It also provides real-time directory monitoring and detailed error reporting with visual indicators. It's designed to be both lightweight and professional.

🐍 Python Syntax Checker Plus

A multi-mode Python Syntax Checker that goes beyond compile().
This tool can:

✅ Scan individual files or entire folders

✅ Run as a Git pre-commit hook (blocks broken commits)

✅ Provide a Tkinter GUI for non-coders

✅ Auto-check files in real time as you save them (watch mode)

✅ Show detailed error reports with line highlighting and caret pointers

🚀 Features

Single File Check – Validate syntax of any .py file

Batch Mode – Scan all Python files in a directory

Pre-Commit Hook Ready – Block commits with syntax errors

GUI Mode – Drag & drop Python files for syntax validation

Directory Watcher – Auto-check whenever files are saved

Detailed Error Reports – Highlights the offending line with a caret ^

📦 Installation

Clone this repo:

git clone https://github.com/your-username/python-syntax-checker-plus.git
cd python-syntax-checker-plus


(Optional) Install dependencies for watcher mode:

pip install watchdog

🛠️ Usage
🔹 Check a single file
python -m syntax_checker.checker example.py

🔹 Batch check a folder
python -m syntax_checker.batch ./my_project

🔹 GUI mode (Tkinter)
python -m syntax_checker.gui

🔹 Watch mode (auto-check on save)
python -m syntax_checker.watcher ./my_project

📘 Pre-Commit Hook

Add this to .pre-commit-config.yaml in your repo:

repos:
-   repo: local
    hooks:
    -   id: syntax-check
        name: Python Syntax Checker
        entry: python -m syntax_checker.batch .
        language: system
        types: [python]


Then install hooks:

pre-commit install

🖼️ Example Output

For a file with a missing parenthesis:

example.py: Syntax Error
Line 1: print("Hello world"
              ^
Error: unexpected EOF while parsing


For a valid file:

example.py: No Syntax Errors Found ✅
