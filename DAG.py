import datetime as dt #import library datetime 
from datetime import timedelta #import timedelta dari library datetime

from airflow import DAG #import DAG dari library airflow
from airflow.operators.bash_operator import BashOperator #import BashOperator dari library airflow.operators.bash_operator


default_args = {
    'owner': 'kurnia', # memasukan nama owner untuk DAG
    'start_date': dt.datetime(2026, 4, 20), # memasukan tanggal dimulainya DAG
    'retries': 1, # apabila terjadi error, maka DAG akan mengulang 1 kali
    'retry_delay': dt.timedelta(minutes=60), # apabila terjadi error, maka DAG akan mengulang setelah 60 menit
}


with DAG('P2M3_Automation_Pipeline', # nama dari DAG
         default_args=default_args,
         schedule_interval='10-30/10 9 * * 6', # menentukan interval jadwal DAG, yaitu setiap 10 menit dimulai pada jam 09.10 - 09.30 setiap hari sabtu.
         catchup=False,
         ) as dag:

    python_extract = BashOperator(task_id='python_extract', bash_command='sudo -u airflow python /opt/airflow/scripts/extract.py')
    python_transform = BashOperator(task_id='python_transform', bash_command='sudo -u airflow python /opt/airflow/scripts/transform.py')
    python_load = BashOperator(task_id='python_load', bash_command='sudo -u airflow python /opt/airflow/scripts/load.py')
# syntax untuk mengeksekusi task menggunakan BashOperator.    

python_extract >> python_transform >> python_load # menentukan urutan eksekusi task, yaitu python_extract akan dieksekusi terlebih dahulu, kemudian diikuti oleh python_transform, dan terakhir python_load.