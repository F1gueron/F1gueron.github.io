import os

# Define the directory containing the files
directory = '_posts/pwn-college/fundamentals/program-misuse'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    # Check if the filename matches the expected format
    if filename.startswith('2024-04-10-Level-') and filename.endswith('.md'):
        # Extract the level number from the filename
        level_number = filename.split('-')[4].split('.')[0]
        
        # Define the new filename
        new_filename = f'2024-04-10-level-{level_number}-PM.md'
        
        # Rename the file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f'Renamed {filename} to {new_filename}')
    else:
        print(f"Skipping file with unexpected format: {filename}")