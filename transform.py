import pyspark
from pyspark.sql.functions import col # import col untuk manipulasi data
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate() #untuk mengaktifkan spark dalam penggunaan manipulasi data

df = spark.read.csv('/opt/airflow/data/shopping_trends.csv', header=True, inferSchema=True) # membaca file shopping_trends.csv menggunakan spark
df = df.withColumn("Customer ID", col("Customer ID").cast("string")) # mengubah tipe data kolom Customer ID menjadi string
df = df.replace("Yes", "True", subset=["Subscription Status"]) # mengganti nilai "Yes" menjadi "True" pada kolom Subscription Status
df = df.replace("Yes", "True", subset=["Discount Applied"]) # mengganti nilai "Yes" menjadi "True" pada kolom Discount Applied
df = df.replace("Yes", "True", subset=["Promo Code Used"]) # mengganti nilai "Yes" menjadi "True" pada kolom Promo Code Used
df = df.replace("No", "False", subset=["Subscription Status"]) # mengganti nilai "No" menjadi "False" pada kolom Subscription Status
df = df.replace("No", "False", subset=["Discount Applied"]) # mengganti nilai "No" menjadi "False" pada kolom Discount Applied
df = df.replace("No", "False", subset=["Promo Code Used"]) # mengganti nilai "No" menjadi "False" pada kolom Promo Code Used
df = df.withColumn("Subscription Status", col("Subscription Status").cast("boolean")) # mengubah tipe data kolom Subscription Status menjadi boolean
df = df.withColumn("Discount Applied", col("Discount Applied").cast("boolean")) # mengubah tipe data kolom Discount Applied menjadi boolean
df = df.withColumn("Promo Code Used", col("Promo Code Used").cast("boolean")) # mengubah tipe data kolom Promo Code Used menjadi boolean
df = df.withColumn("Review Rating", col("Review Rating").cast("float")) # mengubah tipe data kolom Review Rating menjadi float
df.write.mode("overwrite").option("header", "true").csv("/opt/airflow/data/transform_result_shopping_trends") # menyimpan hasil cleaning dan transform data ke dalam folder transform_result_shopping_trends dengan format csv.