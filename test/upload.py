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

def file_processing():
    # trim file
    extract.extract()
    trim.trim()
    
    #defines
    filename = 'audio0.mp3'
    filepath = os.path.dirname(os.path.realpath(__file__)) + '/' + filename
    hdfs_port = '9870'
    hdfs_url = f'http://localhost:{hdfs_port}'    

    # upload to hdfs
    # spark = SparkSession.builder.getOrCreate()
    hdfs_client = InsecureClient(hdfs_url)
    hdfs_client.upload("/data/", filepath, overwrite=True)

    #check upload status
    upload_stat = hdfs_client.status(f'/data/{filename}')
    print(upload_stat)

file_processing()
