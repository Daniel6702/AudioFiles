import os
import json

# Define the base URL structure for audio files
base_url = "https://github.com/Daniel6702/AudioFiles/raw/main/"

# Define the paths for the different Lord of the Rings books
lotr_book_paths = {
    "The Fellowship of the Ring": r"02_The_Lord_of_the_Rings\01_The_Fellowship_of_the_Ring",
    "The Two Towers": r"02_The_Lord_of_the_Rings\02_The_Two_Towers",
    "The Return of the King": r"02_The_Lord_of_the_Rings\03_The_Return_of_the_King",
    "The Hobbit": r"02_The_Lord_of_the_Rings\04_The_Hobbit"
}

# Load the existing JSON file (replace with your file path if necessary)
with open('book_series.json', 'r') as json_file:
    book_series_data = json.load(json_file)

# Find the Lord of the Rings series by title
for series in book_series_data["book_series"]:
    if series["title"] == "The Lord of the Rings":
        # Loop through each book in the Lord of the Rings series
        for book in series["books"]:
            # Get the book name and find its corresponding directory
            book_name = book["name"]
            if book_name in lotr_book_paths:
                book_dir = lotr_book_paths[book_name]
                
                # Initialize an empty list to store chapters
                chapters = []

                # Iterate over the mp3 files in the corresponding book directory
                for i, file_name in enumerate(os.listdir(book_dir), start=1):
                    if file_name.endswith(".mp3"):
                        # Extract the chapter name from the file name
                        chapter_name = file_name.split('_', 1)[1].replace('_', ' ').replace(".mp3", "").title()

                        # Create the chapter entry
                        chapter = {
                            "id": i,
                            "name": chapter_name,
                            "url": f"{base_url}{book_dir}/{file_name}"
                        }

                        # Append to the chapters list
                        chapters.append(chapter)

                # Add chapters to the book if they don't already exist
                if "chapters" not in book:
                    book["chapters"] = chapters

# Save the updated JSON file (replace with your desired output file path)
with open('book_series.json', 'w') as json_file:
    json.dump(book_series_data, json_file, indent=4)

print("Chapters have been added to the Lord of the Rings books in 'book_series_updated.json'.")
