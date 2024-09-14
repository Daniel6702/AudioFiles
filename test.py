import os

def refactor_filenames(directory):
    for filename in os.listdir(directory):
        # Ensure we're only working with .mp3 files
        if filename.endswith(".mp3"):
            # Split the filename at the first ' - ' to get chapter number and title
            parts = filename.split(' - ')
            if len(parts) == 2 and parts[0].startswith("Chapter"):
                # Extract chapter number and title
                chapter_part = parts[0].replace("Chapter ", "").zfill(2)  # Extract chapter number and ensure 2 digits
                title_part = parts[1].replace(' ', '_')  # Replace spaces with underscores

                # Construct the new filename
                new_filename = f"{chapter_part}_{title_part}"
                
                # Full path to old and new file names
                old_file = os.path.join(directory, filename)
                new_file = os.path.join(directory, new_filename)

                # Rename the file
                os.rename(old_file, new_file)
                print(f"Renamed: {old_file} to {new_file}")

# Usage
directory = r'02_The_Lord_of_the_Rings\04_The_Hobbit'  # Replace with the actual path to your directory
refactor_filenames(directory)
