import kagglehub
import os

DATASET_ROOT_DIR = "/opt/airflow/data/"

path = kagglehub.dataset_download("iamsouravbanerjee/customer-shopping-trends-dataset") # link dari kaggle yang ingin di download
print("Path to dataset files:", path)
if not os.path.exists(DATASET_ROOT_DIR):
    os.makedirs(DATASET_ROOT_DIR)
os.system("cp -r {}/* {}".format(path, DATASET_ROOT_DIR))
print("Path to dataset files:", path)
# memasukan file csv yang sudah didownload dari kaggle ke folder data di folder airflow.