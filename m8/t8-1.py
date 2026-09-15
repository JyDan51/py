import mysql.connector
from getpass import getpass

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=getpass("MariaDB password: "),
    database="fligth_game"
)

code = input("Enter ICAO code: ")

cursor = connection.cursor()


sql = "SELECT name, municipality FROM airport WHERE ident = %s"
cursor.execute(sql, (code,))

result = cursor.fetchone()
if result is not None:
    print("Airport:", result[0])
    print("Town:", result[1])
else:
    print("Airport not found")

cursor.close()
connection.close()
