from contextlib import contextmanager

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as f
from app import DOWNLOAD_PATH


@contextmanager
def spark_session() -> SparkSession:
    spark = SparkSession.builder.appName(f"enem-export-data").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    yield spark
    spark.stop()


def read(spark: SparkSession, path: str, year: str) -> DataFrame:
    print(f"Reading file: {path}") 
    df = spark.read.csv(
        path,
        header=True,
        inferSchema=True,
        sep=";"
    )
    if "TP_VERSAO_DIGITAL" in df.columns:
        df = df.drop("TP_VERSAO_DIGITAL")

    df = df.withColumn("year", f.lit(year))
    return df.select(
        *[f.col(col).alias(col.lower()) for col in df.columns]
    )


def write(df: DataFrame, table: str) -> None:
    print(f"Writing table: {table}") 
    df.write \
        .format("jdbc") \
        .mode("append") \
        .option("url", "jdbc:postgresql://db:5432/enem_db") \
        .option("driver", "org.postgresql.Driver") \
        .option("dbtable", table) \
        .option("user", "admin") \
        .option("password", "admin") \
        .save()


def run(**kwargs) -> None:
    with spark_session() as spark:
        for year in range(kwargs["from"], kwargs["to"] + 1):
            base_path = f"{DOWNLOAD_PATH}/microdados_enem_{year}/DADOS"
            test_items = read(spark, f"{base_path}/ITENS_PROVA_{year}.csv", year)
            data = read(spark, f"{base_path}/MICRODADOS_ENEM_{year}.csv", year)
            write(test_items, "test_items")
            write(data, "microdata")
        
        
