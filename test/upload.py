import extract
import trim
import pyspark
from pyspark.sql import SparkSession
import findspark

def file_processing():
    # trim file
    extract.extract()
    trim.trim()
    
    # upload to hdfs
    spark = SparkSession.builder.getOrCreate()

    audio_data = spark.sparkContext.binaryFiles('./audio0.mp3').first()[1]
    dataframe = spark.createDataFrame(["hdfs://localhost:19000/data/audio0.mp3", audio_data], ["path", "data"])
    
    dataframe.write.mode("overwrite").format("binaryFile").option("path", "hdfs://localhost:19000/data/audio0.mp3").save()

    

