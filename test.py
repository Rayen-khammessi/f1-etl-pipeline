import mysql.connector

try:
    conn = mysql.connector.connect(
        user='rayen',
        password='pass',
        host='127.0.0.1',
        database='f1etl'
    )
    print("✅ MySQL connection successful!")
    conn.close()
except Exception as e:
    print("❌ Error:", e)
