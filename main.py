from os import listdir
from os.path import isfile, join, abspath

# Get directory from user to search
print("Path must be the full path to the directory on your machine")
directory = input("Enter directory to search: ")

extension = input("Enter extension to search for: ")

# Handles cases where the user inputs a . in the path, as this is not wanted
if "." in extension:
    extension = extension.replace(".", "")

# Gets a list of all files in the directory using list comprehension
files = [f for f in listdir(directory) if isfile(join(directory, f))]

matches = []
# Loops through the list of files and prints the ones that match the extension
for file in files:
    if file.endswith(extension):
        matches.append(file)

# Prints the number of files found
print("Found " + str(len(matches)) + " files")

# Prints the files found
for match in matches:
    print(f"{match}: {abspath(join(directory, match))}")

