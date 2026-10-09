import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="practice"
)
cur = conn.cursor()
cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)
conn.close()