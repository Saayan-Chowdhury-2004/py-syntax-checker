# 🐍 Python Syntax Checker

A **multi-mode Python Syntax Checker** that goes beyond `compile()`.

---

## 1) Overview

Python Syntax Checker is a lightweight yet powerful tool to validate Python scripts without executing them.
It is designed for:

* Beginners learning Python (instant feedback on mistakes)
* Developers working in teams (pre-commit enforcement)
* Educators or trainers (teaching code correctness)

---

## 2) Features

### 🔹 Core

* Check syntax of **single files**
* **Batch mode**: validate all `.py` files in a folder
* Generate **detailed error reports** with line + caret pointer

### 🔹 Advanced

* **GUI mode**: simple Tkinter interface for non-coders
* **Watch mode**: continuously monitor a folder and re-check files on save

---

## 3) Project Structure

```
py-syntax-checker/
│── example_files/       # Sample buggy Python files
│── py_syntax_checker/
│   ├── __init__.py
│   ├── checker.py       # Single file check
│   ├── batch.py         # Batch folder scan
│   ├── watcher.py       # Real-time directory watcher
│   ├── gui.py           # Tkinter GUI interface
│── tests/
│   ├── test_checker.py  # Unit tests
│── .gitignore       
│── README.md
│── setup.py
```

---

## 4) Installation

### Clone Repository

```bash
git clone https://github.com/your-username/py-syntax-checker.git
cd py-syntax-checker
```

### Install Dependencies

```bash
pip install watchdog
```

*(GUI and batch modes don’t require extra dependencies.)*

---

## 5) Usage

### a. Check a Single File

```bash
python -m syntax_checker.checker example.py
```

### b. Batch Mode (check a folder)

```bash
python -m syntax_checker.batch ./my_project
```

### c. GUI Mode (Tkinter interface)

```bash
python -m syntax_checker.gui
```

### d. Watch Mode (auto-check on file save)

```bash
python -m syntax_checker.watcher ./my_project
```

---

## 6) Example Outputs

### ✅ Valid File

```
example.py: No Syntax Errors Found
```

### ❌ File with Error

```
example.py: Syntax Error
Line 1: print("Hello world"
              ^
Error: unexpected EOF while parsing
```

---

## 7) Future Enhancements

### Planned upgrades for py-syntax-checker include:

|                                                     |
|-----------------------------------------------------|
| Auto-fix suggestions for common syntax issues |
| IDE/editor plugins (VS Code, PyCharm) |
| Web-based syntax checking interface |
| Configurable team-specific rules |
| CI/CD pipeline integration for automated checks |

---

## Conclusion

py-syntax-checker is built to make error detection simple, fast, and reliable. Whether you’re checking a single file, scanning an entire project, or watching code in real time, it keeps your workflow clean and stress-free.

---
