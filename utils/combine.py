import os
from pydub import AudioSegment
from natsort import natsorted

# Function to combine a list of audio files into one
def combine_audio_files(file_list, output_path):
    combined_audio = AudioSegment.empty()
    for file in file_list:
        audio = AudioSegment.from_mp3(file)
        combined_audio += audio
    combined_audio.export(output_path, format="mp3")
    print(f"Exported: {output_path}")

def process_directory(directory, num_output_files):
    # Get all mp3 files in the directory
    mp3_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".mp3")]
    
    # Sort files using natural sort (e.g., 1, 2, 3, 10, 11)
    mp3_files = natsorted(mp3_files)
    
    # Number of files per output file
    files_per_output = len(mp3_files) // num_output_files
    remainder = len(mp3_files) % num_output_files  # If there are some leftover files

    start_index = 0
    for i in range(1, num_output_files + 1):
        # Determine how many files to include in this output
        end_index = start_index + files_per_output + (1 if i <= remainder else 0)
        
        # Prepare the file list for this chapter
        files_to_combine = mp3_files[start_index:end_index]
        
        # Generate the output file name
        chapter_num = str(i).zfill(2)
        output_filename = os.path.join(directory, f"{chapter_num}_Chapter_{chapter_num}.mp3")
        
        # Combine the selected files and save the output
        combine_audio_files(files_to_combine, output_filename)
        
        # Update the start index for the next set of files
        start_index = end_index

if __name__ == "__main__":
    # Set the path to your directory containing mp3 files
    directory_path = r"06_Percy_Jackson_And_The_Olympians\04_The_Battle_Of_The_Labyrinth"
    
    # Set the number of output files you want (10 in this case)
    num_output_files = 10
    
    # Call the function to process the directory
    process_directory(directory_path, num_output_files)
