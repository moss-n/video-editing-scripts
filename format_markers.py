import csv
import sys
import os

# Get the input file name from the command line
input_file = sys.argv[1]

# Open the input file and read the data
with open(input_file, 'r') as file:
    data = list(csv.DictReader(file))

# Remove all columns except "Source In" and "Notes"
for row in data:
    for key in list(row.keys()):
        if key not in ['Source In', 'Notes']:
            del row[key]

# Modify the format of the values in the "Source In" column
for row in data:
    row['Source In'] = row['Source In'][3:8]
    # Remove new line at the end of Notes value
    row['Notes'] = row['Notes'].strip()

# Get the base name of the input file without the extension
base_name = os.path.splitext(os.path.basename(input_file))[0]

# Write the modified data to a new file
with open(f'formatted_{base_name}.txt', 'w') as file:
    for row in data:
        file.write(f"{row['Notes']}: {row['Source In']}\n")

