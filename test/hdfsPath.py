import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession

def get_path():
    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format("binaryFile").load("hdfs://localhost:19000/data/*.mp3").selectExpr("path").collect()
    path = [row['path'] for row in df]
    return path