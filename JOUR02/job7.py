import mysql.connector

connexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Scarface13",
)
mycursor = connexion.cursor()

mycursor.execute("CREATE DATABASE employes")

connexion = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Scarface13",
  database="employes"
)

mycursor = connexion.cursor()
mycursor.execute("CREATE TABLE employees (id INT AUTO_INCREMENT PRIMARY KEY, nom VARCHAR(255), prenom VARCHAR(255), salaire FLOAT, id_service INT)")
