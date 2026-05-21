import os  # import lib os untuk mengakses environment variable
from dotenv import load_dotenv  # import lib dotenv untuk membaca file .env
from pymongo import MongoClient  # import lib MongoClient untuk koneksi ke MongoDB
from pyspark.sql import SparkSession  # import lib SparkSession untuk koneksi ke Spark

load_dotenv()  # membaca file .env dan memuat semua variable ke environment

spark = SparkSession.builder.getOrCreate()  # mengaktifkan spark
df = spark.read.csv('/opt/airflow/data/transform_result_shopping_trends', header=True)  # membaca file csv pada folder transform_result_shopping_trends menggunakan spark

MONGO_URI = os.getenv("MONGO_URI")  # mengambil URI koneksi MongoDB dari file .env
MONGO_DB = os.getenv("MONGO_DB")  # mengambil nama database MongoDB dari file .env
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")  # mengambil nama collection MongoDB dari file .env

# =====================================================================
# PENTING: Buat file bernama ".env" di folder yang sama dengan file ini
# Isi file .env dengan variable berikut:
#
#   MONGO_URI=mongodb+srv://<username>:<password>@<host>.mongodb.net/
#   MONGO_DB=<nama_database>
#   MONGO_COLLECTION=<nama_collection>
#
# Ganti <username>, <password>, <host>, <nama_database>, dan
# <nama_collection> sesuai dengan kredensial MongoDB kamu.
#
# Jangan lupa tambahkan ".env" ke file ".gitignore" agar kredensial
# tidak ikut ter-push ke GitHub.
# =====================================================================

client = MongoClient(MONGO_URI)  # memasukan credential untuk koneksi ke MongoDB yang diambil dari .env
db = client[MONGO_DB]  # nama database yang akan digunakan di MongoDB, diambil dari .env
collection = db[MONGO_COLLECTION]  # nama collection yang akan digunakan di MongoDB, diambil dari .env

data = df.toPandas().to_dict(orient="records")  # mengubah df menjadi format pandas dan diubah menjadi dict/json dan disimpan pada variabel data
collection.insert_many(data)  # memasukan data ke MongoDB