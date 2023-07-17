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