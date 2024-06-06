from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pipeline_1.config.ConfigStore import *
from pipeline_1.udfs.UDFs import *

def by_average_rating_asc(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("movie_averageRating").asc())
