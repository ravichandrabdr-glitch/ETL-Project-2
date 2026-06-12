from pathlib import Path

from pyspark.sql import SparkSession


project_root = Path(__file__).resolve().parent

spark = SparkSession.builder \
    .appName("Retail_ETL") \
    .getOrCreate()
# customers file
customers = spark.read.csv(
    str(project_root / "data" / "customers.csv"),
    header=True,
    inferSchema=True
)

# orders file
orders = spark.read.csv(
    str(project_root / "data" / "orders.csv"),
    header=True,
    inferSchema=True
)
customers.show()
orders.show()