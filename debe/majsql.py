import mysql.connector

mydb = mysql.connector.connect(
  host="10.4.0.238",
  user="tnt",
  password="tnt",
  database="tnt"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.close()
