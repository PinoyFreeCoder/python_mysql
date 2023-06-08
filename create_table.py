import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="123456",
    database="python_mysql"
)

cursor = db.cursor()
 

cursor.execute("CREATE table customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), location VARCHAR(255))")