import subtitle as st
import download
# result of task
result = []
def process_audio_file(hdfs_path):
    global result
    # print current process
    print(f'Processing: {hdfs_path}')
    # get filename and download to local
    filename = hdfs_path.split('/')[-1]
    download.download_audio(filename)
    # get result
    result.append(st.get_subtitle(filename))