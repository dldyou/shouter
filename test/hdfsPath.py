import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession

from pyspark.sql.functions import udf
from pyspark.sql.types import BinaryType
from pydub import AudioSegment

# Define a UDF to read audio file
@udf(returnType=BinaryType())
def read_audio_file(path):
    audio = AudioSegment.from_file(path)
    return audio.export(format="mp3").read()

def get_path():
    spark = SparkSession.builder.getOrCreate()

    df = spark.read.format("binaryFile").load("/data/audio0.mp3")
    # .selectExpr("path", "read_audio_file(content) as audio_data")
