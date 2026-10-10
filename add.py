from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("add").getOrCreate()

a = 1
b = 2
c = a+b
print(c)

spark.stop()


