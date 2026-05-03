from src.project.data.csv_converter import CSVConverter
from src.project.data.csv_writer import sauvegarder_donnees_csv
from src.project.data.database import Database

# 1. initialisation de la bdd
db = Database()

# 2. load des données
print("Chargement des données en cours, veuillez patienter...")
converter = CSVConverter(data_directory="data/raw", db=db)
converter.charger_tout()
print("Chargement terminé !\n")

print("Sauvegarde des données en cours, veuillez patienter...")
sauvegarder_donnees_csv(data_directory="data/db", db=db)
print("Sauvegarde terminée !\n")
