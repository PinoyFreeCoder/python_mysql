import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="123456",
    database="python_mysql"
)

cursor = db.cursor()

sql = "SELECT * FROM customers"

cursor.execute(sql)

result = cursor.fetchall()

for x in result:
    print(x)