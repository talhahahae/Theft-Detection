import os

# Specify the directory containing the images
directory = 'Data/NotStealing'

# Loop through each file in the directory
for filename in os.listdir(directory):
    # Check if the file has the .png extension and matches the pattern
    if filename.endswith('.png') and 'Normal_Videos' in filename:
        # Construct the new filename
        new_filename = filename.replace('Normal_Videos', 'NotSteal_1_')
        
        # Full paths for the old and new filenames
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f'Renamed: {filename} -> {new_filename}')
