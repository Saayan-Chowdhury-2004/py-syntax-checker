import tkinter as tk
from tkinter import filedialog, messagebox
from .checker import check_syntax

def run_gui():
    root = tk.Tk()
    root.title("Python Syntax Checker")

    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if file_path:
            result = check_syntax(file_path, return_output=True)
            messagebox.showinfo("Result", result)

    btn = tk.Button(root, text="Select Python File", command=browse_file, width=30)
    btn.pack(pady=20)

    root.mainloop()

def main():
    run_gui()

if __name__ == "__main__":
    main()
