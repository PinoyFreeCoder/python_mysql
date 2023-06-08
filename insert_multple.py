import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user="root",
    password="123456",
    database="python_mysql"
)

cursor = db.cursor()

sql = "INSERT INTO customers (name, location) VALUES (%s, %s)"
value = [
    ("HRrepublic", "Corner Timog 123"),
    ("ShoesInc", "Manila 124"),
    ("Barbers101", "Makati 255"),
    ("RestoBar", "Laguna 222"),
    ("GuitarMania", "Cebu 323"),
    ("MarkelShoe", "Laguna 321"),
    ("SaveDogs", "Cavite 123"),
    ("SameInc", "Batangas 444"),
    ("Smila Inc", "Batangas 123")
]
cursor.executemany(sql, value)

db.commit()

print(cursor.rowcount, "was inserted.")