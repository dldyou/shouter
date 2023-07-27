import findspark
findspark.init()

import hdfs
import extract
import trim
import pyspark
import os
from pyspark import SparkFiles
from pyspark.sql import SparkSession
from hdfs import InsecureClient

def file_processing(key):
    # trim file
    extract.extract(key)
    trim.trim(key)
    
    #defines
    hdfs_port = '9870'
    hdfs_url = f'http://localhost:{hdfs_port}'    

    # upload to hdfs
    # spark = SparkSession.builder.getOrCreate()
    hdfs_client = InsecureClient(hdfs_url)

    cnt = 0
    while (True): 
        filename = f'{key}{cnt}.mp3'
        path = os.path.dirname(os.path.realpath(__file__)) + '\\' + filename
        
        # file does not exist -> break loop
        if (not os.path.isfile(path)):
            break
        
        filepath = os.path.dirname(os.path.realpath(__file__)) + '/' + filename
        hdfs_client.makedirs(f'/data/{key}')
        hdfs_client.upload(f'/data/{key}/', filepath, overwrite=True)
        
        #check upload status
        upload_stat = hdfs_client.status(f'/data/{key}/{filename}')
        print(upload_stat)
        
        cnt += 1
