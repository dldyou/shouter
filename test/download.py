import os
from hdfs import InsecureClient
from hdfs import HdfsError

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