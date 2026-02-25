import mysql.connector
import time

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            return mysql.connector.connect(
                host="db",          
                user="root",         
                password="root",   
                database="chat_db"
            )
        except mysql.connector.Error:
            print("Database not ready yet, waiting 3 seconds...")
            time.sleep(3)
            retries -= 1
    raise Exception("Could not connect to database after multiple retries")

def init_db():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                room VARCHAR(50) NOT NULL,
                username VARCHAR(50) NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        cursor.close()
        conn.close()
        print("Database initialized successfully!")
    except mysql.connector.Error as err:
        print(f"Error: Could not initialize database - {err}")
