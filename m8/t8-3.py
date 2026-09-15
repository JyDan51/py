import mysql.connector
from getpass import getpass
from geopy.distance import geodesic

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=getpass("MariaDB password: "),
    database="fligth_game"
)

code1 = input("Enter first ICAO code: ")
code2 = input("Enter second ICAO code: ")

cursor = connection.cursor()

sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"

cursor.execute(sql, (code1,))
coords1 = cursor.fetchone()

cursor.execute(sql, (code2,))
coords2 = cursor.fetchone()

if coords1 is not None and coords2 is not None:
    distance = geodesic(coords1, coords2).km
    print(f"Distance: {distance:.2f} km")
else:
    print("Airport not found")

cursor.close()
connection.close()