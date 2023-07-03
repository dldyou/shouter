import whisper as ws

model = ws.load_model("base")

#이걸 구해야 할건디,,,,
audio = ws.load_audio("test.m4a")
audio = ws.pad_or_trim(audio)

mel = ws.log_mel_spectrogram(audio).to(model.device)

_, probs = model.detect_language(mel)
print(f'Detected language: {max(probs, key=probs.get)}')

options = ws.DecodingOptions()
result = ws.decode(model, mel, options)

print(result.text)