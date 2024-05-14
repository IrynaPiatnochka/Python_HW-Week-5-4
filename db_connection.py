import mysql.connector 
from mysql.connector import Error

def connect_db():
    db_name = "library_sys" 
    user = "root" 
    # password = "Lifeisinmyhands88" 
    host = "127.0.0.1" 

    
    try:
        conn = mysql.connector.connect(
            database=db_name,
            user=user,
            # password=password,
            host=host
        )

        if conn.is_connected():
            print("Connected to MySQL Database")
            return conn 

    except Error as e:
        print(f"Error: {e}")
        return None






