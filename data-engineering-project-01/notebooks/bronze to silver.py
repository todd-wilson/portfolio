# Databricks notebook source
# MAGIC %md
# MAGIC Format dates for all tables.

# COMMAND ----------

from pyspark.sql.functions import  from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls("/mnt/bronze/SalesLT/"):
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

table_name

# COMMAND ----------

for i in table_name:
    path = '/mnt/bronze/SalesLT/' + i + '/' + i + '.parquet'
    print(path)
    df = spark.read.format('parquet').load(path)
    column = df.columns

    for col in column:
        if "Date" in col or "date" in col:
            df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))

    output_path = '/mnt/silver/SalesLT/' + i + '/'
    df.write.format('delta').mode("overwrite").save(output_path)
