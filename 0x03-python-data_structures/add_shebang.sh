#!/bin/bash

# List of filenames to add the shebang line to
file_list=("0-print_list_integer.py" "1-element_at.py" "2-replace_in_list.py" "3-print_reversed_list_integer.py" "4-new_in_list.py" "5-no_c.py" "6-print_matrix_integer.py" "7-add_tuple.py" "8-multiple_returns.py" "100-print_python_list_info.c" "13-is_palindrome.c" "lists.h" "12-switch.py" "11-delete_at.py" "10-divisible_by_2.py" "9-max_integer.py")

# Loop through the list of files and add the shebang line
for file in "${file_list[@]}"; do
    echo "#!/usr/bin/python3" > "$file"
done
