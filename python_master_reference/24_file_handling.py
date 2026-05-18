"""
24 - File Handling
Python can create, write, and read files.
"""

# Open the file example.txt in write mode.
# If the file does not exist, Python will create it.
# If the file already exists, Python will overwrite it.
with open("example.txt", "w", encoding="utf-8") as file:
    # Write the first line into the file.
    file.write("Hello file!\n")

    # Write the second line into the file.
    file.write("This line is written by Python.\n")


# Open the same file in read mode.
with open("example.txt", "r", encoding="utf-8") as file:
    # Read the whole content of the file and save it in a variable.
    content = file.read()

print(content)