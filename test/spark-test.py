import findspark
findspark.init()

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

data = spark.read.csv("hdfs://localhost:19000/data/data.csv", header="true")

data.show(5)