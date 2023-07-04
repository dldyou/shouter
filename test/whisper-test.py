import whisper as ws
import os

# print(os.getcwd())
filename = 'test2.m4a'
path = os.path.dirname(os.path.realpath(__file__)) + '\\' + filename

model = ws.load_model("base")

#이걸 구해야 할건디,,,,
audio = ws.load_audio(path)
audio = ws.pad_or_trim(audio)

mel = ws.log_mel_spectrogram(audio).to(model.device)

_, probs = model.detect_language(mel)
print(f'Detected language: {max(probs, key=probs.get)}')

options = ws.DecodingOptions(fp16 = False)
result = ws.decode(model, mel, options)

print(result.text)