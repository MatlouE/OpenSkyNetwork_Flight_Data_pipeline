import psycopg2
import os
import time

def test_connection():
    # Use the environment variables we'll define in docker-compose
    dbname = os.getenv("DB_NAME")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASS")
    host = os.getenv("DB_HOST")

    print(f"Attempting to connect to {host}...")
    
    # Simple retry loop
    for i in range(5):
        try:
            conn = psycopg2.connect(
                dbname=dbname, user=user, password=password, host=host
            )
            print("✅ CONNECTION SUCCESSFUL!")
            conn.close()
            return
        except Exception as e:
            print(f"Attempt {i+1}: Database not ready yet... ({e})")
            time.sleep(2)

if __name__ == "__main__":
    test_connection()