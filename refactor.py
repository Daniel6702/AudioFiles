import os
import re

# Function to refactor file names
def refactor_filename(filename):
    # Remove "_recompressed" if present
    filename = filename.replace("_recompressed", "")
    
    # Remove the year in parentheses (e.g., (2014))
    filename = re.sub(r"\(\d{4}\)", "", filename)
    
    # Separate the track number and the title using regex (preserve hyphens within the title)
    match = re.match(r"(\d+)\s-\s(.+)", filename)
    if match:
        track_number = match.group(1)
        title = match.group(2)
        
        # Replace spaces in the title with underscores
        title = title.replace(" ", "_")
        
        # Strip any trailing or leading underscores
        title = title.strip("_")
        
        # Combine the track number with the processed title
        filename = f"{track_number}_{title}"
    
    return filename

# Path to the directory containing the files
directory = "01_The_Fellowship_of_the_Ring"

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Only process files (ignore directories)
    if os.path.isfile(os.path.join(directory, filename)):
        # Split the filename into name and extension
        name, ext = os.path.splitext(filename)
        
        # Refactor the name
        new_name = refactor_filename(name)
        
        # Construct the new filename with the original extension
        new_filename = f"{new_name}{ext}"
        
        # Get the full path for old and new file names
        old_file_path = os.path.join(directory, filename)
        new_file_path = os.path.join(directory, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")

print("File renaming complete.")
