# 0x0B. Python - Input/Output

## Project Overview

In this project, you will learn how to perform input and output operations in Python, particularly file handling and working with JSON data. The focus will be on how to read and write files, as well as understand the concepts of serialization and deserialization.

## Resources

You should read or watch the following resources:

- 7.2. Reading and Writing Files
- 8.7. Predefined Clean-up Actions
- Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))
- JSON encoder and decoder
- Learn to Program 8 : Reading / Writing Files
- Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)
- All about py-file I/O

## Learning Objectives

At the end of this project, you are expected to be able to explain the following concepts to anyone:

### General

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use `pycodestyle` (version 2.8.*)
- All files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases

- Allowed editors: vi, vim, emacs
- All files should end with a new line
- All test files should be inside a folder called `tests`
- All test files should be text files (extension: .txt)
- All tests should be executed using this command: `python3 -m doctest ./tests/*`
- All modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (use `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation is not just a simple word; it should explain the purpose of the module, class, or method in full sentences. The length of the documentation will be verified.
- We strongly encourage you to work together on test cases to avoid missing any edge cases.