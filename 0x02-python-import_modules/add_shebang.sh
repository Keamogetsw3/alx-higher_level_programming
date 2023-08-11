#!/bin/bash

# List of filenames to add the shebang line to
file_list=("0-add.py" "1-calculation.py" "2-args.py" "3-infinite_add.py" "4-hidden_discovery.py" "5-variable_load.py" "100-my_calculator.py" "101-easy_print.py" "102-magic_calculation.py" "103-fast_alphabet.py")

# Loop through the list of files and add the shebang line
for file in "${file_list[@]}"; do
    echo "#!/usr/bin/python3" > "$file"
done
