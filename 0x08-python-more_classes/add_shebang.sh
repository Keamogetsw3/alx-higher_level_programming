#!/bin/bash

# List of file names and their content
declare -A files=(
    ["0-rectangle.py"]=""
    ["1-rectangle.py"]=""
    ["2-rectangle.py"]=""
    ["3-rectangle.py"]=""
    ["4-rectangle.py"]=""
    ["5-rectangle.py"]=""
    ["6-rectangle.py"]=""
    ["7-rectangle.py"]=""
    ["8-rectangle.py"]=""
    ["9-rectangle.py"]=""
    ["101-nqueens.py"]=""
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
            chmod u+x "$file"  # Add execute permissions
            echo "Added shebang to $file"
        else
            echo "Shebang already exists in $file"
        fi
    fi
done
