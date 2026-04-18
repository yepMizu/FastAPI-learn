import psycopg2
from psycopg2.extras import RealDictCursor
import time

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='MyDB',
            user='postgres',
            password='password123',
            cursor_factory=RealDictCursor
        )
        cursor = conn.cursor()
        print("Database connected Successfully")
        break

    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(3)