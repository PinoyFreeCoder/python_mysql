import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="123456",
    database="python_mysql"
)

cursor = db.cursor()

sql = "INSERT INTO customers (name, location) VALUES (%s, %s)"
value = ("HRrepublic", "Manila 123")
cursor.execute(sql, value)

db.commit()

print(cursor.rowcount, "record inserted.")