import os
from .checker import check_syntax

def check_folder(folder_path="."):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                check_syntax(file_path)


def main():
    import sys
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"Scanning Python files in: {folder}\n")
    check_folder(folder)


if __name__ == "__main__":
    main()
