# Create a DAG that:
# 1. Uses a BashOperator to echo a word and create a new file that contains that word as text
# 2. Uses a PythonOperator to get that word from the file and print it to the Airflow log