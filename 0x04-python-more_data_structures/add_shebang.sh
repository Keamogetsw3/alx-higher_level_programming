#!/bin/bash

# List of file names and their content
declare -A files=(
    ["0-square_matrix_simple.py"]=""
    ["1-search_replace.py"]=""
    ["2-uniq_add.py"]=""
    ["3-common_elements.py"]=""
    ["4-only_diff_elements.py"]=""
    ["5-number_keys.py"]=""
    ["6-print_sorted_dictionary.py"]=""
    ["7-update_dictionary.py"]=""
    ["8-simple_delete.py"]=""
    ["9-multiply_by_2.py"]=""
    ["10-best_score.py"]=""
    ["11-multiply_list_map.py"]=""
    ["12-roman_to_int.py"]=""
    ["100-weight_average.py"]=""
    ["101-square_matrix_map.py"]=""
    ["102-complex_delete.py"]=""
    ["103-python.c"]=""
)

# Loop through the files and create if they don't exist
for file in "${!files[@]}"; do
    if [ ! -f "$file" ]; then
        touch "$file"
        chmod u+x "$file"  # Add execute permissions
        echo "#!/usr/bin/python3" > "$file"  # Add shebang line
        echo "Created and added shebang to $file"
    else
        # Check if the shebang line already exists
        if ! grep -q "#!/usr/bin/python3" "$file"; then
            # Add the shebang line to the beginning of the file
            echo "#!/usr/bin/python3" | cat - "$file" > temp && mv temp "$file"
            chmod +x "$file"  # Add execute permissions
            echo "Added shebang to $file"
        else
            echo "Shebang already exists in $file"
        fi
    fi
done
