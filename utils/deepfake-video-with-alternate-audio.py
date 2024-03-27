from moviepy.editor import VideoFileClip, AudioFileClip
import speech_recognition as sr
from pydub import AudioSegment
import os
from gtts import gTTS

# Initialize speech recognizer
r = sr.Recognizer()

# Step 1: Load the video file
video_clip = VideoFileClip("/Users/vikas/Desktop/input.mp4")

# Access the audio clip from the video
audio_clip = video_clip.audio

# Print audio properties
print(f"Audio Duration: {audio_clip.duration} seconds")
print(f"Audio FPS (frames per second): {audio_clip.fps}")
print(f"Number of Audio Channels: {audio_clip.nchannels}")

# Export the video's audio to a file (temporary WAV file for compatibility)
temp_audio_path = "temp_audio.wav"
audio_clip.write_audiofile(temp_audio_path)

# Use the recognize_google() method to transcribe the audio file
try:
    with sr.AudioFile(temp_audio_path) as source:
        # Record the audio file into an audio data object
        audio_data = r.record(source)
        # Transcribe the audio data to text
        text = r.recognize_google(audio_data)
        print("Transcription: ", text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")



# Clean up the temporary audio file
os.remove(temp_audio_path)

# Step 2: Extract the audio from the video file (optional if you are going to replace it anyway)
# This step is not necessary if you're going to replace the audio,
# but it's useful to know how to extract audio.
# audio_clip = video_clip.audio

# Step 3: Load your new audio file
new_audio_clip = AudioFileClip("/Users/vikas/builderspace/Real-Time-Voice-Cloning/utils/output.wav")



# Step 4: Replace the audio in the video file
# This will replace the audio of the video_clip with new_audio_clip
# Ensure the audio is the same duration as the video; you may need to cut or loop your audio
video_with_new_audio = video_clip.set_audio(new_audio_clip)

# Step 5: Save the video file with the new audio
output_path = "/Users/vikas/Desktop//output_video.mp4"
video_with_new_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Note: Specifying codecs is optional but recommended for compatibility.
