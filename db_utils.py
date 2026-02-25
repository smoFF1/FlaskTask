import mysql.connector
from mysql.connector import pooling

db_pool = pooling.MySQLConnectionPool(
    pool_name="chatpool",
    pool_size=5,
    host="localhost",      # in Docker compose: use service name like "db"
    user="chatuser",
    password="chatpass",
    database="chatdb",
)

def get_conn():
    return db_pool.get_connection()