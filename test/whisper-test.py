import whisper as ws
import trim
import extract
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
    boundary_index = 0
    for i in range(cnt):
        if (i == cnt - 1):
            final_result.append(result[i][boundary_index:])
        else:
            final_result.append(result[i][boundary_index:sz - 1])
        # get size
        sz = len(result[i])
        # check last sentence
        last_sentence = result[i][sz - 1]
        start_time, end_time, text = last_sentence
        
        # find boundary
        for idx, sentence in enumerate(result[i + 1]):
            # if start time is same
            if (start_time - trim.timing == sentence[0]):
                boundary_index = idx
                print(f'boundary at {sentence[0]} ~ {sentence[1]}: {sentence[2]}')
                break
    
    # print result
    for data in final_result:
        print(data)

def checkGPU(model):
    # model capabilities
    model_capability = {'tiny': 0.9, 'base': 0.9, 'small': 1.9, 'medium': 4.9, 'large': 9.9}
    
    device_count = torch.cuda.device_count()
    capability = 0
    
    # get highest capability
    for i in range(device_count):
        device = torch.device(f'cuda:{i}')
        print(f'Device {i}: {torch.cuda.get_device_name(device)}')
        if (capability < torch.cuda.get_device_properties(device).total_memory / 1024**3):
            capability = torch.cuda.get_device_properties(device).total_memory / 1024**3
    
    # check GPU is available
    if (model_capability[model] > capability):
        print("Can\'t find available device")
        os.environ["CUDA_VISIBLE_DEVICES"] = ""    

        
def main():
    # checkGPU(sel_model)
    extract.extract()
    trim.trim()
    task()
    merge()
            
if __name__ == '__main__':
    main()