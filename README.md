# 🐍 Python Syntax Checker Plus

A **multi-mode Python Syntax Checker** that goes beyond `compile()`.

---

## 1) Overview

Python Syntax Checker Plus is a lightweight yet powerful tool to validate Python scripts without executing them.
It is designed for:

* 👩‍💻 Beginners learning Python (instant feedback on mistakes)
* 🛠️ Developers working in teams (pre-commit enforcement)
* 📊 Educators or trainers (teaching code correctness)

---

## 2) Features

### 🔹 Core

* Check syntax of **single files**
* **Batch mode**: validate all `.py` files in a folder
* Generate **detailed error reports** with line + caret pointer

### 🔹 Advanced

* **Pre-commit hook ready**: stop bad code before it hits Git
* **GUI mode**: simple Tkinter interface for non-coders
* **Watch mode**: continuously monitor a folder and re-check files on save

---

## 3) Project Structure

```
python-syntax-checker-plus/
│── syntax_checker/
│   ├── __init__.py
│   ├── checker.py       # Single file check
│   ├── batch.py         # Batch folder scan
│   ├── watcher.py       # Real-time directory watcher
│   ├── gui.py           # Tkinter GUI interface
│── tests/
│   ├── test_checker.py  # Unit tests
│── requirements.txt
│── README.md
│── setup.py
│── .pre-commit-config.yaml
│── example_files/       # Sample buggy Python files
```

---

## 4) Installation

### Clone Repository

```bash
git clone https://github.com/your-username/python-syntax-checker-plus.git
cd python-syntax-checker-plus
```

### Install Dependencies

```bash
pip install watchdog
```

*(GUI and batch modes don’t require extra dependencies.)*

---

## 5) Usage

### 1️⃣ Check a Single File

```bash
python -m syntax_checker.checker example.py
```

### 2️⃣ Batch Mode (check a folder)

```bash
python -m syntax_checker.batch ./my_project
```

### 3️⃣ GUI Mode (Tkinter interface)

```bash
python -m syntax_checker.gui
```

### 4️⃣ Watch Mode (auto-check on file save)

```bash
python -m syntax_checker.watcher ./my_project
```

---

## 🖼6) Example Outputs

### ✅ Valid File

```
example.py: No Syntax Errors Found ✅
```

### ❌ File with Error

```
example.py: Syntax Error
Line 1: print("Hello world"
              ^
Error: unexpected EOF while parsing
```

---

## 7) Pre-Commit Hook Setup

1. Add to `.pre-commit-config.yaml` in your project:

```yaml
repos:
-   repo: local
    hooks:
    -   id: syntax-check
        name: Python Syntax Checker
        entry: python -m syntax_checker.batch .
        language: system
        types: [python]
```

2. Install hooks:

```bash
pre-commit install
```

With this, commits with syntax errors will be **blocked automatically**.
