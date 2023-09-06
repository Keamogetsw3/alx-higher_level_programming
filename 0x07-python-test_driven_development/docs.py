import os
import ast
import astor

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
                    code = astor.to_source(node)
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
        function_name = code.strip().split('(')[0].strip()
        doctest_doc += f"# The ``{function_name}`` module\n"
        doctest_doc += "=" * (len(function_name) + 23) + "\n\n"

        doctest_doc += f"Using ``{function_name}`` function\n"
        doctest_doc += "=" * (len(f"Using ``{function_name}`` function") + 32) + "\n\n"

        doctest_doc += f"Importing the function {function_name}.\n"
        doctest_doc += f">>> {function_name} = __import__('0-add_integer').{function_name}\n\n"

        doctest_doc += f"`{function_name}()` returns the sum of its arguments. The default argument for b is 98. For numbers, that value is equivalent to using the ``+`` operator:\n"
        doctest_doc += f">>> {function_name}(1, 2)\n"
        doctest_doc += "3\n\n"

        # Add more test cases as needed, following the same pattern

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

            # Remove the ".py" extension from the output filename
            output_filename = f"tests/{filename[:-3]}.txt"
            with open(output_filename, "w") as output_file:
                output_file.write(doctest_doc)

if __name__ == "__main__":
    input_folder = "/alx-higher_level_programming/0x07-python-test_driven_development"  # Replace with the correct folder path
    process_files_in_folder(input_folder)
