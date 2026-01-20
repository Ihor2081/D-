import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3307,
    database="testdb",
    user="root",
    password="mysql"
)

cursor = connection.cursor()
select Query = "select * from users"
cursor.execute(Query)
result = cursor.fetchall()
print(result)