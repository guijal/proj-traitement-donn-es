from ..data.csv_converter import CSVConverter
from ..data.csv_writer import sauvegarder_donnees_csv
from ..data.database import Database


def chargement_raw_data():
    # 1. initialisation d'une bdd
    db = Database()

    # 2. load des données sous forme d'objets 
    print(" ⚙️   Chargement des données depuis les fichiers bruts en cours, veuillez patienter...")
    converter = CSVConverter(data_directory="data/raw", db=db)
    converter.charger_tout()
    print(" ✅   Chargement terminé !\n")

    # 3. Export en fichier csv
    print(" ⚙️   Sauvegarde des données en cours, veuillez patienter...")
    sauvegarder_donnees_csv(data_directory="data/db", db=db)
    print(" ✅   Sauvegarde terminée !\n")
