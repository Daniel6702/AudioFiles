import os

def fix_chapter_filenames(directory):
    for filename in os.listdir(directory):
        # Ensure we're only working with .mp3 files
        if filename.endswith(".mp3"):
            # Skip '01_Prologue' as it is already correct
            if filename.startswith('01_Prologue'):
                continue
            
            # Extract the current chapter number (e.g., '02_Chapter_00_-_The_Prophet')
            parts = filename.split('_', 2)
            if len(parts) < 3:
                continue
            
            # Extract the current filename parts
            file_number = parts[0]  # e.g., '02'
            chapter_info = parts[1]  # e.g., 'Chapter'
            rest_of_name = parts[2]  # e.g., '00_-_The_Prophet.mp3'
            
            # Extract the current chapter number within the file name (e.g., '00')
            internal_parts = rest_of_name.split('_-_', 1)
            chapter_number_in_filename = internal_parts[0]  # e.g., '00'
            rest_of_title = internal_parts[1]  # e.g., 'The_Prophet.mp3'
            
            # Calculate the new chapter number for both filename prefix and the chapter within the name
            new_file_number = str(int(file_number) + 1).zfill(2)  # e.g., '02' becomes '03'
            new_chapter_number_in_filename = str(int(chapter_number_in_filename) + 1).zfill(2)  # e.g., '00' becomes '01'
            
            # Construct the new filename
            new_filename = f"{new_file_number}_Chapter_{new_chapter_number_in_filename}_-_{rest_of_title}"
            
            # Full path to old and new file names
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} to {new_file}")

# Usage
directory = r'03_A_Song_of_Ice_and_Fire\04_A_Feast_For_Crows'  # Replace with the actual path to your directory
fix_chapter_filenames(directory)
