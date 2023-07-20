import findspark
findspark.init() 
from pyspark import SparkConf, SparkContext
import whisper as ws
import upload
import hdfsPath
import merge
import os
from hdfs import InsecureClient
from hdfs import HdfsError

# progress in MAP
###########################################################################

# get title for mp3 file
def get_subtitle(path):
    # get model
    sel_model = "medium"
    model = ws.load_model(sel_model)
    
    # get audio and trim it
    audio = ws.load_audio(path)
    audio = ws.pad_or_trim(audio)

    mel = ws.log_mel_spectrogram(audio).to(model.device)

    _, probs = model.detect_language(mel)
    print(f'Detected language: {max(probs, key=probs.get)}')

    options = ws.DecodingOptions(fp16 = False)
    result = model.transcribe(audio)
    
    # get result
    ret = []
    for data in result['segments']:
        start_time = round(data['start'], 2)
        end_time = round(data['end'], 2)
        text = data['text']
        ret.append([start_time, end_time, text])
        
        print(f'{start_time} ~ {end_time}: {text}')
    
    # return result
    return ret

# download audio from hdfs
def download_audio(filename):
    hdfs_port = '9870'
    hdfs_url = f'http://localhost:{hdfs_port}'    
    filepath = os.path.dirname(os.path.realpath(__file__))

    # upload to hdfs
    hdfs_client = InsecureClient(hdfs_url)
    try:
        hdfs_client.download(f'/data/{filename}', filepath)
        
        #check download status
        if (os.path.isfile(filepath+'\\'+filename)):
            print(f'File download Succesfully ({filename})')
    except HdfsError as e:
        print(str(e))

# Map function
def process_audio_file(hdfs_path):
    global result
    # print current process
    print(f'Processing: {hdfs_path}')
    # get filename and download to local
    filename = hdfs_path.split('/')[-1]
    download_audio(filename)
    # get result
    path = os.path.dirname(os.path.realpath(__file__)) + '\\' + filename
    return get_subtitle(path)

###########################################################################

def main():
    # configuration spark API
    conf = SparkConf().setAppName("Shouter").setMaster("local")
    sctx = SparkContext(conf = conf)
    # file upload to hdfs like audio0.mp3, audio1.mp3, ..., audio{n}.mp3
    upload.file_processing()
    # file read from hdfs 
    audio_files = hdfsPath.get_path()
    # set RDD 
    audio_files_rdd = sctx.parallelize(audio_files)
    # Map (apply subtitle.get_subtitle() for every audio{n}.mp3 files)
    result_rdd = audio_files_rdd.map(process_audio_file)
    # Reduce (collect results)
    results = result_rdd.collect()
    results = merge.merge_audio(results, len(audio_files))
    print(results)
    # transform to subtitle file form
    
    # start download subtitle file
    
if __name__ == '__main__':
    main()