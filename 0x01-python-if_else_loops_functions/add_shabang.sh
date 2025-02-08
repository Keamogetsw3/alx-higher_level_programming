#!/bin/bash

# List of filenames to add the shebang line to
file_list=("3-print_alphabt.py" "4-print_hexa.py" "5-print_comb2.py" "6-print_comb3.py" "7-islower.py" "8-uppercase.py" "9-print_last_digit.py" "10-add.py" "11-pow.py" "12-fizzbuzz.py" "102-magic_calculation.py")

# Loop through the list of files and add the shebang line
for file in "${file_list[@]}"; do
    echo "#!/usr/bin/python3" > "$file"
done
