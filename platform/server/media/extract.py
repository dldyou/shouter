import os
import moviepy.editor as mp

# Extract MP3 file at MP4 file
def extract(key):
    video = f'{key}.mp4'
    audio = f'{key}.mp3'
    standard_path = os.path.dirname(os.path.realpath(__file__)) + '\\'

    clip = mp.VideoFileClip(standard_path + video)
    clip.audio.write_audiofile(standard_path + audio)
