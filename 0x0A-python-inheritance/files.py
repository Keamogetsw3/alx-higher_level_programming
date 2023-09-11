import os

# Define the list of file names
file_names = [
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
    "101-add_attribute.py",
]

# Shebang line
shebang = "#!/usr/bin/python3"

# Create files with shebang lines
for file_name in file_names:
    with open(file_name, "w") as file:
        file.write(shebang + "\n")
    print(f"Created {file_name}")

print("All files created successfully.")
