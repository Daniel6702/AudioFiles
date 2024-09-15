import os
import json

# Define the base URL structure for audio files
base_url = "https://github.com/Daniel6702/AudioFiles/raw/main/"

# Define the paths for the different Percy Jackson books
percy_jackson_book_paths = {
    "The Lightning Thief": "06_Percy_Jackson_And_The_Olympians/01_The_Lightning_Thief",
    "The Sea of Monsters": "06_Percy_Jackson_And_The_Olympians/02_The_Sea_Of_Monsters",
    "The Titan's Curse": "06_Percy_Jackson_And_The_Olympians/03_The_Titans_Curse",
    "The Battle of the Labyrinth": "06_Percy_Jackson_And_The_Olympians/04_The_Battle_Of_The_Labyrinth",
    "The Last Olympian": "06_Percy_Jackson_And_The_Olympians/05_The_Last_Olympian"
}

# Load the existing JSON file (replace with your file path if necessary)
with open('book_series.json', 'r') as json_file:
    book_series_data = json.load(json_file)

# Function to clean up the chapter name
def clean_chapter_name(file_name):
    # Remove the number prefix and extension
    chapter_name = file_name.split('_', 1)[1].replace(".mp3", "")
    
    # Replace underscores with spaces
    chapter_name = chapter_name.replace('_', ' ')
    
    # Replace hyphens with spaces and properly title case
    chapter_name = chapter_name.replace('-', ' ').title()
    
    return chapter_name

# Find the Percy Jackson series by title
for series in book_series_data["book_series"]:
    if series["title"] == "Percy Jackson & the Olympians":
        # Loop through each book in the Percy Jackson series
        for book in series["books"]:
            # Get the book name and find its corresponding directory
            book_name = book["name"]
            if book_name in percy_jackson_book_paths:
                book_dir = percy_jackson_book_paths[book_name]
                
                # Initialize an empty list to store chapters
                chapters = []

                # Iterate over the mp3 files in the corresponding book directory
                for i, file_name in enumerate(os.listdir(book_dir), start=1):
                    if file_name.endswith(".mp3"):
                        try:
                            # Clean the chapter name using the helper function
                            chapter_name = clean_chapter_name(file_name)

                            # Create the chapter entry
                            chapter = {
                                "id": i,
                                "name": chapter_name,
                                "url": f"{base_url}{book_dir}/{file_name}"
                            }

                            # Append to the chapters list
                            chapters.append(chapter)
                        except IndexError:
                            print(f"Skipping file: {file_name} due to unexpected format.")
                
                # Add chapters to the book if they don't already exist
                if "chapters" not in book:
                    book["chapters"] = chapters

# Save the updated JSON file (replace with your desired output file path)
with open('book_series.json', 'w') as json_file:
    json.dump(book_series_data, json_file, indent=4)

print("Chapters have been added to the Percy Jackson books in 'book_series_updated.json'.")
