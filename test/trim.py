import os
from pydub import AudioSegment
import math

sec = 1000
# trim cycle
timing = 20 * sec

# Trim MP3 file 1 / N
def trim():
    global timing, interpolation_timing
    filename = 'audio.mp3'
    standard_path = os.path.dirname(os.path.realpath(__file__)) + '\\'

    audio = AudioSegment.from_mp3(standard_path + filename)

    for i in range(math.ceil(len(audio) / timing)):
        part_audio = audio[timing * i:timing * (i + 1)]
        part_audio.export(standard_path + f'audio{i}.mp3')