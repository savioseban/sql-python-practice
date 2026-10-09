import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="practice"
)
df = pd.read_sql("SELECT * FROM students", conn)
df.to_csv("students.csv", index=False)
conn.close()
print("Saved students.csv")