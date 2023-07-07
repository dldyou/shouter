import whisper as ws
import os

# print(os.getcwd())
def start(filename):
    path = os.path.dirname(os.path.realpath(__file__)) + '\\' + filename
    
    if (not os.path.isfile(path)):
        return
    
    model = ws.load_model("medium")

    #이걸 구해야 할건디,,,,
    audio = ws.load_audio(path)
    audio = ws.pad_or_trim(audio)

    mel = ws.log_mel_spectrogram(audio).to(model.device)

    _, probs = model.detect_language(mel)
    print(f'Detected language: {max(probs, key=probs.get)}')

    options = ws.DecodingOptions(fp16 = False)
    # result = ws.decode(model, mel, options)
    result = model.transcribe(audio)

    #print(type(result))
    # print(result['segments'])

    for data in result['segments']:
        start_time = data['start']
        end_time = data['end']
        text = data['text']
        print(f'{start_time} ~ {end_time}: {text}')
        
idx = 0
while (True):
    start(f'audio{idx}.mp3')
    idx += 1