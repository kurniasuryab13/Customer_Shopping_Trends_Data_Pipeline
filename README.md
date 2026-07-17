# 📊 Data Pipeline of Customer Shopping Trends 

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![Google Looker Studio](https://img.shields.io/badge/Google%20Looker%20Studio-4285F4?style=for-the-badge&logo=googlelookerstudio&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

Proyek ini berfokus dalam membuat pipeline data end-to-end dengan data Customer Shopping Trends yang mengekstraksi data pada Kaggle, transformasi menggunakan PySpark, pemuatan (loading) ke MongoDB, serta otomatisasi menggunakan Apache Airflow. Tahap pra-otomatisasi meliputi exploratory data analysis (EDA) dan validasi data menggunakan Great Expectations.

---

# 📑 Daftar Isi

1. [Link Dataset](#-Link-Dataset)
2. [Gambaran Project](#-gambaran-project)
3. [Metode Yang Digunakan](#️-Metode-Yang-Digunakan)
4. [List File](#-list-file)
5. [Cara Menjalankannya](#-Cara-Menjalankannya)
6. [Libraries](#-libraries)
7. [Author](#-author)

---

# 🔗 Link Dataset

- [Customer Shopping Trends Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset)

---

# 📌 Gambaran Project

Proyek ini membuat pipeline ETL (Extract, Transform, Load) otomatis untuk data Customer Shopping Trends. Pipeline ini melakukan:

- Extract —> mengambil data dari Kaggle
- Transform —> mentransformasi data menggunakan PySpark
- Load —> memuat data hasil transformasi ke MongoDB

Seluruh proses ini diorkestrasi (dijadwalkan dan dikelola) menggunakan Apache Airflow yang dijalankan di atas Docker.
Sebelum tahap otomasi, ada langkah pra-proses yang mencakup EDA (Exploratory Data Analysis), eksplorasi data untuk memahami pola, distribusi, dan anomali, serta Data validation menggunakan Great Expectations, untuk memastikan kualitas dan konsistensi data sebelum masuk ke pipeline otomatis.

## 1. Extract
Dataset diunduh dari Kaggle menggunakan library `kagglehub`, kemudian disalin ke folder `/opt/airflow/data/` agar dapat diakses oleh Airflow dalam proses selanjutnya.

## 2. Transform
Data hasil extract dibaca menggunakan PySpark, kemudian dilakukan proses transformasi seperti mengubah tipe data kolom, mengganti nilai `Yes/No` menjadi `True/False` pada kolom boolean, dan menyimpan hasil transformasi kembali ke folder Airflow dalam format CSV.

## 3. Load
Data hasil transformasi dibaca kembali menggunakan PySpark, dikonversi ke format dictionary, lalu dimasukkan ke MongoDB. Kredensial koneksi MongoDB (URI, nama database, dan nama collection) disimpan secara aman di file `.env` agar tidak ter-expose ke GitHub.

## 4. DAG (Airflow Automation)
Ketiga proses di atas (extract, transform, load) diotomasi menggunakan Apache Airflow DAG. DAG dijadwalkan berjalan setiap hari Sabtu pada jam 09:10–09:30 WIB, dengan urutan eksekusi: `extract → transform → load`. Apabila terjadi error, DAG akan melakukan retry 1 kali setelah 60 menit.

## 5. EDA & Great Expectations
Sebelum pipeline diotomasi, dilakukan eksplorasi data sederhana, data cleaning, dan data processing menggunakan Pandas di Jupyter Notebook. Selanjutnya dilakukan validasi data menggunakan Great Expectations untuk memastikan kualitas data sebelum masuk ke pipeline.

---

# ⚒️ Metode Yang Digunakan

- Exploratory Data Analysis (EDA)
- Data Transformation with PySpark
- ETL Pipeline Automation with Apache Airflow
- Data Validation with Great Expectations
- Database Management with MongoDB
- Containerization with Docker

---

# 📁 List File

| File | Deskripsi |
|------|-----------|
| `extract.py` | Script untuk mengunduh dataset dari Kaggle dan menyimpan ke folder Airflow |
| `transform.py` | Script transformasi data menggunakan PySpark |
| `load.py` | Script untuk memuat data ke MongoDB menggunakan kredensial dari `.env` |
| `DAG.py` | Script DAG Airflow untuk otomasi pipeline ETL |
| `ETL and GX.ipynb` | Notebook EDA, data cleaning, dan validasi dengan Great Expectations |
| `data_raw` | Dataset mentah hasil download dari Kaggle |
| `data_cleaned` | Dataset hasil proses cleaning |
| `DAG_SS.png` | Screenshot tampilan DAG di Airflow |
| `mongodb_SS.png` | Screenshot data yang berhasil masuk ke MongoDB |

---

# 💻 Cara Menjalankannya

## 1. Clone repository ini

```bash
git clone https://github.com/kurniasuryab13/Customer_Shopping_Trends_Data_Pipeline.git
cd Customer_Shopping_Trends_Data_Pipeline
```

## 2. Buat file `.env` di folder yang sama dengan `load.py`

```env
MONGO_URI=mongodb+srv://<username>:<password>@<host>.mongodb.net/
MONGO_DB=<nama_database>
MONGO_COLLECTION=<nama_collection>
```

> Ganti `<username>`, `<password>`, `<host>`, `<nama_database>`, dan `<nama_collection>` sesuai kredensial MongoDB kamu.  
> Jangan lupa tambahkan `.env` ke `.gitignore` agar kredensial tidak ter-push ke GitHub.

## 3. Jalankan Apache Airflow dengan Docker

```bash
docker-compose up
```

## 4. Buka Airflow di browser

```
http://localhost:8080
```

## 5. Jalankan DAG

- Enable DAG **P2M3_Automation_Pipeline** di Airflow dashboard
- Klik tombol **Trigger DAG** untuk menjalankan pipeline secara manual

---

# 📚 Libraries

- PySpark
- Pandas
- NumPy
- Matplotlib
- Seaborn
- PyMongo
- python-dotenv
- kagglehub
- Apache Airflow
- Great Expectations

---

# ✍️ Author

## Kurnia Surya

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/kurniasuryab/)
