from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline1.config.ConfigStore import *
from pipeline1.functions import *

def dataset1(spark: SparkSession) -> DataFrame:
    return spark.read\
        .schema(
          StructType([
            StructField("movie_title", StringType(), True), StructField("production_date", StringType(), True), StructField("genres", StringType(), True), StructField("runtime_minutes", StringType(), True), StructField("director_name", StringType(), True), StructField("director_professions", StringType(), True), StructField("director_birthYear", StringType(), True), StructField("director_deathYear", StringType(), True), StructField("movie_averageRating", StringType(), True), StructField("movie_numerOfVotes", StringType(), True), StructField("approval_Index", StringType(), True), StructField("Production budget $", StringType(), True), StructField("Domestic gross $", StringType(), True), StructField("Worldwide gross $", StringType(), True)
        ])
        )\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/tables/suraj/movie_statistic_dataset.csv")
