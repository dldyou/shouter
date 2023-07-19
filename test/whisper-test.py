import whisper as ws
import trim
import extract
import upload
import os
import torch

# result of tasks
result = []
# count of files
cnt = 0
# final result (return this)
final_result = []

# get model
sel_model = "medium"
model = ws.load_model(sel_model)
# print(os.getcwd())
def start(path):
    global model
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

def task():
    global cnt, result
    while (True): 
        filename = f'audio{cnt}.mp3'
        path = os.path.dirname(os.path.realpath(__file__)) + '\\' + filename
        # file does not exist -> break loop
        if (not os.path.isfile(path)):
            break
        
        print(f'audio{cnt}.mp3 file detected')
        result.append(start(path))
        cnt += 1
        
def merge():
    global cnt, result, final_result
    for i in range(cnt):
        start_time = result[i][-1][0]
        if (trim.timing - start_time <= 0.2):
            final_result.append(result[i][:-1])
        else:
            final_result.append(result[i])
    
    # print result
    for data in final_result:
        print(data)



        
def main():
    upload.file_processing()
    task()
    merge()
            
if __name__ == '__main__':
    main()