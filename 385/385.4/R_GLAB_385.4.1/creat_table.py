# To connect to MySQL, we need mysql-connector-python
import mysql.connector as mydbconnection # using an alias for clarity
from mysql.connector import Error # Error function for special MySQL errors

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
        # creates a cursor object that allows SQL actions to the MySQL server engine
        cursor = conn.cursor()
        # create a SQL query we want to run
        query = ''' 
            CREATE TABLE laptop (
                ID int(11) NOT   NULL,
                Name varchar(250) NOT NULL,
                Price float NOT NULL,
                Purchase_date date NOT NULL
            )
        '''
    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection Closed')



if __name__ == "__main__":
    connect()