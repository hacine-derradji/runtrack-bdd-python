import mysql.connector

connexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Scarface13",
  database="laplateforme"
)

mycursor = connexion.cursor()

mycursor.execute("SELECT nom, capacite FROM salles")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
