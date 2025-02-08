#!/bin/bash

# List of file names and their content
declare -A files=(
    ["0-square.py"]=""
    ["1-square.py"]=""
    ["2-square.py"]=""
    ["3-square.py"]=""
    ["4-square.py"]=""
    ["5-square.py"]=""
    ["6-square.py"]=""
    ["100-singly_linked_list.py"]=""
    ["101-square.py"]=""
    ["102-square.py"]=""
    ["103-magic_class.py"]=""
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
