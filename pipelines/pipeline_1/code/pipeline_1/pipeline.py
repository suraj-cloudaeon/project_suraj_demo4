from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline_1.config.ConfigStore import *
from pipeline_1.udfs.UDFs import *
from prophecy.utils import *
from pipeline_1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dataset1 = dataset1(spark)
    df_by_average_rating_asc_2 = by_average_rating_asc_2(spark, df_dataset1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pipeline_1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipeline_1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipeline_1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
