import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession

def get_path(key):
    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format("binaryFile").load(f'hdfs://localhost:50070/data/{key}/*.mp3').selectExpr("path").collect()
    path = [row['path'] for row in df]
    return path