import os
from pydub import AudioSegment
import math

sec = 1000
# trim cycle
timing = 20 * sec
# interpolation time
interpolation_timing = 5 * sec

def trim():
    filename = 'audio.mp3'
    standard_path = os.path.dirname(os.path.realpath(__file__)) + '\\'

    audio = AudioSegment.from_mp3(standard_path + filename)

    # trim like 0-25 20-45 40-65
    for i in range(int(math.floor(len(audio) / timing))):
        part_audio = audio[timing * i:timing * (i + 1) + interpolation_timing]
        part_audio.export(standard_path + f'audio{i}.mp3')