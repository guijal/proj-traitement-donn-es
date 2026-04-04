"""
étapes pour lancer l'application :

1. Transformer l'ensemble des données csv en instances
2. Lancer l'application via l'interface
"""

from src.project.data.csv_loader import CSVLoader
from src.project.data.database import Database

"""
Créer une fonction main a plusieurs avantages :

- avoir des variables locales
- exécuter le code uniquement si on run depuis le bon fichier i.e. main.py
avec la ligne " if __name__ == "__main__": "
- pouvoir changer de runner facilement en important la fonction main dans un autre fichier

"""


def main():
    # 1. Initialisation de la base de données en mémoire
    db = Database()

    # 2. Initialisation de l'instance de chargement puis injection de la base de données
    loader = CSVLoader(data_directory="data/raw", db=db)
    loader.charger_tout()

    # test afficher les données pour team de basket
    registre_equipes = db.equipes
    print("=== Équipes chargées ===")
    # .values() permet de récupérer la liste des objets (sans leurs IDs)
    for equipe in registre_equipes.values():
        # L'affichage de l'équipe utilise implicitement la méthode __str__ définie dans ta classe Equipe
        print(f"- {equipe} | Sport: {equipe.discipline.nom}")


if __name__ == "__main__":
    main()
