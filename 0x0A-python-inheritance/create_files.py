#!/usr/bin/python3

import os

# List of filenames to be created
filenames = [
    "0-lookup.py",
    "1-my_list.py",
    "2-is_same_class.py",
    "3-is_kind_of_class.py",
    "4-inherits_from.py",
    "5-base_geometry.py",
    "6-base_geometry.py",
    "7-base_geometry.py",
    "8-rectangle.py",
    "9-rectangle.py",
    "10-square.py",
    "11-square.py",
    "100-my_int.py",
    "101-add_attribute.py"
]

# Shebang line
shebang = "#!/usr/bin/env python3\n"

# Create each file and write the shebang line
for filename in filenames:
    with open(filename, 'w') as file:
        file.write(shebang)

print("Files created successfully with shebang lines.")
