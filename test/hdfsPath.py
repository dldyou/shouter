import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession

from pyspark.sql.functions import udf
from pyspark.sql.types import BinaryType
from pydub import AudioSegment

def get_path():
    spark = SparkSession.builder.getOrCreate()
    df = spark.read.format("binaryFile").load("hdfs://localhost:50070/data/*.mp3").selectExpr("path").collect()
    list = [row['path'] for row in df]
    return list