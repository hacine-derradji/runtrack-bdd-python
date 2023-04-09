import mysql.connector

# se connecter à la base de données
connexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Scarface13",
  database="laplateforme"
)

mycursor = connexion.cursor()
mycursor.execute("SELECT SUM(superficie) FROM etage")


myresult = mycursor.fetchone()

print("La superficie de La Plateforme est de", myresult[0], "m2")
