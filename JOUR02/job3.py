import mysql.connector

# se connecter à la base de données
connexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Scarface13",
  database="laplateforme"
)

mycursor = connexion.cursor()

mycursor.execute("INSERT INTO etage (nom, numero, superficie) VALUES ('RDC', 0, 500), ('R+1', 1, 500)")
mycursor.execute("INSERT INTO salles (nom, id_etage, capacite) VALUES ('Lounge', 1, 100), ('Studio son', 1, 5), ('Broadcasting', 2, 50), ('Bocal peda', 2, 4), ('Coworking', 2, 80), ('Studio Video', 2, 5)")

connexion.commit()

print(mycursor.rowcount, "lignes insérées.")
