import os

def rename_mp3_files(directory):
    # Get a list of all .mp3 files in the directory
    mp3_files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    
    # Sort the files to maintain consistent numbering
    mp3_files.sort()

    # Loop through and rename each file
    for i, filename in enumerate(mp3_files, start=1):
        # Create the new name with the format 01_Chapter_01, 02_Chapter_02, etc.
        new_name = f"{i:02d}_Chapter_{i:02d}.mp3"
        
        # Full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {filename} -> {new_name}")

# Specify the path to the directory containing the mp3 files
directory_path = r'06_Percy_Jackson_And_The_Olympians\03_The_Titans_Curse'

# Call the function to rename files
rename_mp3_files(directory_path)
