import os
import re

def rename_files(directory):
    # Get the list of all files in the directory
    files = sorted(os.listdir(directory))
    
    # Loop through each file
    for index, filename in enumerate(files, start=1):
        # Only process .mp3 files
        if filename.endswith(".mp3"):
            # Extract the file name without extension
            name_without_extension = os.path.splitext(filename)[0]
            
            # Split based on the first occurrence of "_" to separate the number and title
            parts = name_without_extension.split("_", 1)
            
            # Generate the new index with two digits
            new_index = f"{index:02d}"

            # Format the rest of the name (replace spaces with underscores)
            if len(parts) == 2:
                title = parts[1].strip().replace(" ", "_")
                new_name = f"{new_index}_{title}.mp3"
            else:
                new_name = f"{new_index}_{name_without_extension.replace(' ', '_')}.mp3"
            
            # Get the full paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_name)
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {filename} -> {new_name}")

# Example usage
directory = r"04_A_Song_of_Ice_and_Fire\02_A_Clash_of_Kings"  # Replace with the path to your directory
rename_files(directory)
