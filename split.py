import os
from pydub import AudioSegment

# Function to recompress the audio to make it smaller
def recompress_audio(file_path, output_path, bitrate="192k"):
    audio = AudioSegment.from_mp3(file_path)
    audio.export(output_path, format="mp3", bitrate=bitrate)
    print(f"Recompressed {file_path} to {output_path}")

# Function to split audio into two parts
def split_and_recompress(file_path, output_path, bitrate="192k"):
    audio = AudioSegment.from_mp3(file_path)
    half_duration = len(audio) // 2
    
    # First half
    first_half = audio[:half_duration]
    first_half.export(f"{output_path}_1.mp3", format="mp3", bitrate=bitrate)
    
    # Second half
    second_half = audio[half_duration:]
    second_half.export(f"{output_path}_2.mp3", format="mp3", bitrate=bitrate)
    
    # Recombine into a single file
    combined = first_half + second_half
    combined.export(f"{output_path}_combined.mp3", format="mp3", bitrate=bitrate)
    print(f"Split and recompressed {file_path} into {output_path}_combined.mp3")

# Main function to process directory
def process_directory(directory):
    size_limit = 100 * 1024 * 1024  # 100MB in bytes
    
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            file_path = os.path.join(directory, filename)
            file_size = os.path.getsize(file_path)
            
            if file_size > size_limit:
                # Output file name without extension
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(directory, base_name)

                # Recompress and check the size again
                recompressed_path = f"{output_path}_recompressed.mp3"
                recompress_audio(file_path, recompressed_path)
                
                # Check the size of the recompressed file
                new_size = os.path.getsize(recompressed_path)
                if new_size > size_limit:
                    # If still over 100MB, split and recompress
                    split_and_recompress(file_path, output_path)
                else:
                    print(f"Recompressed file is under 100MB: {recompressed_path}")

if __name__ == "__main__":
    # Set your directory path containing mp3 files
    directory_path = "test"
    process_directory(directory_path)
