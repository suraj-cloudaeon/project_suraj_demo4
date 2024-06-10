from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline1.config.ConfigStore import *
from pipeline1.functions import *

def dataset1(spark: SparkSession) -> DataFrame:
    return spark.read\
        .option("header", True)\
        .option("sep", ",")\
        .csv("dbfs:/FileStore/tables/suraj/movie_statistic_dataset.csv")
