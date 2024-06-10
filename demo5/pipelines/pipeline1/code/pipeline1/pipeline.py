from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pipeline1.config.ConfigStore import *
from pipeline1.functions import *
from prophecy.utils import *
from pipeline1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_dataset1 = dataset1(spark)
    df_Reformat_1 = Reformat_1(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("pipeline1")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pipeline1")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/pipeline1", config = Config)(pipeline)

if __name__ == "__main__":
    main()
