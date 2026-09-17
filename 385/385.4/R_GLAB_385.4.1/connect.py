# To connect to MySQL, we need mysql-connector-python
import mysql.connector as mydbconnection # using an alias for clarity
from mysql.connector import Error # Error function for special MySQL errors
from dotenv import 

def connect():
    conn = None

    try:
        conn = mydbconnection.connect(
            database='classicmodels',
            user='root',
            password='password' # password for mysql server
        )

        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')



if __name__ == "__main__":
    connect()