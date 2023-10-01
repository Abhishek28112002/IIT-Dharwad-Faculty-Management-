import psycopg2
import os
from dotenv import load_dotenv

try:
    load_dotenv()
    db_info = {
       "user": os.getenv("db_user"),
       "host": os.getenv("db_host"),
       "database": os.getenv("database"),
       "password": os.getenv("db_passowrd"),
    }

    connection = psycopg2.connect(**db_info)
    cursor = connection.cursor()
    query = "select * from Specialization"
    cursor.execute(query)
    result=cursor.fetchall()
    print(result)
    connection.commit()
    cursor.close()
    connection.close()
except Exception as e:
    print(f"An error occurred: {e}")
