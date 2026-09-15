import mysql.connector
from getpass import getpass

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password=getpass("MariaDB password: "),
    database="fligth_game"
)

code = input("Enter country code: ")

cursor = connection.cursor()

sql = """
SELECT type, COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
ORDER BY type
"""

cursor.execute(sql, (code,))

result = cursor.fetchall()

for row in result:
    print(row[0], ":", row[1])

cursor.close()
connection.close()