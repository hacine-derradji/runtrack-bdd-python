import mysql.connector

connexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Scarface13",
  database="laplateforme"
)

mycursor = connexion.cursor()

mycursor.execute("CREATE TABLE etage (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), numero INT, superficie INT)")
mycursor.execute ("CREATE TABLE salles(id INT PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(255), id_etage INT, capacite INT)")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)





