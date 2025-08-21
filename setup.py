from setuptools import setup, find_packages

setup(
    name="py-syntax-checker",                     # Package name (PyPI-style)
    version="0.1.0",                              # Semantic versioning
    description="A Python Syntax Checker with CLI, batch scanning, GUI, and real-time watching.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Saayan Chowdhury",
    url="https://github.com/Saayan-Chowdhury-2004/py-syntax-checker",  # update with your repo
    packages=find_packages(include=["py_syntax_checker", "py_syntax_checker.*"]),
    install_requires=[
        "watchdog",   # for directory watching
        "tk",         # GUI (tkinter wrapper, some OSes already ship it)
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "py-syntax-check=py_syntax_checker.checker:main",
            "py-syntax-check-batch=py_syntax_checker.batch:main",
            "py-syntax-check-watch=py_syntax_checker.watcher:main",
            "py-syntax-check-gui=py_syntax_checker.gui:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
