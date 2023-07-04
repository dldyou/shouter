import whisper as ws
import os

print(os.getcwd())

model = ws.load_model("base")

#이걸 구해야 할건디,,,,
audio = ws.load_audio('C:\\Code\\shouter\\shouter\\shouter\\test\\test2.m4a')
audio = ws.pad_or_trim(audio)

mel = ws.log_mel_spectrogram(audio).to(model.device)

_, probs = model.detect_language(mel)
print(f'Detected language: {max(probs, key=probs.get)}')

options = ws.DecodingOptions(fp16 = False)
result = ws.decode(model, mel, options)

print(result.text)