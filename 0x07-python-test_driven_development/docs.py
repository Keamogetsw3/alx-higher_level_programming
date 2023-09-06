import os
import ast

def extract_docstrings_and_code(file_path):
    """
    Extract docstrings and code from a Python file.

    Args:
        file_path (str): The path to the Python file.

    Returns:
        list: A list of tuples containing (docstring, code) pairs.
    """
    docstring_code_pairs = []
    with open(file_path, 'r') as file:
        source_code = file.read()
        tree = ast.parse(source_code)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                docstring = ast.get_docstring(node)
                if docstring:
                    code = ast.unparse(node)
                    docstring_code_pairs.append((docstring, code))
    return docstring_code_pairs

def generate_doctest_documentation(docstring_code_pairs):
    """
    Generate doctest documentation from docstring-code pairs.

    Args:
        docstring_code_pairs (list): A list of tuples containing (docstring, code) pairs.

    Returns:
        str: Doctest documentation.
    """
    doctest_doc = ""
    for docstring, code in docstring_code_pairs:
        doctest_doc += f'"""\n{docstring}\n"""\n'
        doctest_doc += f"def test_{code.strip().split('(')[0]}():\n"
        doctest_doc += f'    r"""\n    >>> {code.strip()}\n    """\n'
        doctest_doc += f'    pass\n\n'
    return doctest_doc

def process_files_in_folder(folder_path):
    """
    Process all Python files in a folder and generate doctest documentation.

    Args:
        folder_path (str): The path to the folder containing Python files.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            file_path = os.path.join(folder_path, filename)
            docstring_code_pairs = extract_docstrings_and_code(file_path)
            doctest_doc = generate_doctest_documentation(docstring_code_pairs)
            
            output_filename = f"tests/doctest_{filename}.txt"
            with open(output_filename, "w") as output_file:
                output_file.write(doctest_doc)

if __name__ == "__main__":
    input_folder = "/alx-higher_level_programming/0x07-python-test_driven_development"  # Replace with the correct folder path
    process_files_in_folder(input_folder)
