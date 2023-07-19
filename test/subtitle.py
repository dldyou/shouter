import whisper as ws

def get_subtitle(path):
    # get model
    sel_model = "medium"
    model = ws.load_model(sel_model)
    
    # 오디오 불러오기 및 trim 진행
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
    
    ret = []
    for data in result['segments']:
        start_time = round(data['start'], 2)
        end_time = round(data['end'], 2)
        text = data['text']
        ret.append([start_time, end_time, text])
        
        print(f'{start_time} ~ {end_time}: {text}')
        
    return ret