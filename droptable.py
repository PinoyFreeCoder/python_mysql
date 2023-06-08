import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="123456",
    database="python_mysql"
)

cursor = db.cursor()

sql = "DROP TABLE customers"

cursor.execute(sql)