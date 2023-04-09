import mysql.connector

connexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Scarface13",
  database="laplateforme"
)

mycursor = connexion.cursor()

mycursor.execute("SELECT SUM(capacite) FROM salles")


myresult = mycursor.fetchone()

print("La capacité de toutes les salles est de :", myresult[0])
