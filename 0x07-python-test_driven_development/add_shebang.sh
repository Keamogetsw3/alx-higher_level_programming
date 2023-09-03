#!/bin/bash

# List of file names and their content
declare -A files=(
    ["0-add_integer.py"]=""
    ["3-say_my_name.py"]=""
    ["2-matrix_divided.py"]=""
    ["4-print_square.py"]=""
    ["5-text_indentation.py"]=""
    ["100-matrix_mul.py"]=""
    ["101-lazy_matrix_mul.py"]=""
    ["100-singly_linked_list.py"]=""
    ["102-python.c"]=""
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
