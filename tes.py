import ffmpeg
import math
import os

# Function to split the audio file using ffmpeg
def split_audio_ffmpeg(file_path, output_prefix, num_splits):
    # Get the total duration of the audio file using ffmpeg
    probe = ffmpeg.probe(file_path)
    audio_length = float(probe['format']['duration'])  # Audio duration in seconds
    
    # Calculate the length of each split
    split_length = math.ceil(audio_length / num_splits)
    
    print(f"Total audio length: {audio_length:.2f} seconds")
    print(f"Each split will be approximately {split_length} seconds")

    for i in range(num_splits):
        # Calculate the start and end times for the split
        start_time = i * split_length
        end_time = min(start_time + split_length, audio_length)  # Ensure we don't go beyond the total length
        
        # Generate the output file name
        output_file_name = f"{i+1:02d}_Chapter_{i+1:02d}.mp3"
        
        # Use ffmpeg to extract the audio chunk
        print(f"Processing segment {i+1} from {start_time:.2f} to {end_time:.2f} seconds...")
        (
            ffmpeg
            .input(file_path, ss=start_time, t=(end_time - start_time))
            .output(output_file_name)
            .run(quiet=True)  # You can remove quiet=True to see ffmpeg logs
        )
        
        # Print progress
        print(f"Exported: {output_file_name} | {100 * (i + 1) / num_splits:.2f}% complete")

    print("Audio splitting complete!")

# Example usage
file_path = r"06_Percy_Jackson_And_The_Olympians\05_The_Last_Olympian\audio.mp3"  # Replace with your actual file path
output_prefix = "Chapter"          # Prefix for the output files
num_splits = 10                    # Number of splits

# Ensure the file exists before proceeding
if os.path.exists(file_path):
    split_audio_ffmpeg(file_path, output_prefix, num_splits)
else:
    print(f"File not found: {file_path}")
