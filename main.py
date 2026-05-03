"""
étapes pour lancer l'application :

0. importer la structure depuis github

1. Vérifications :
1.1.  Avoir l'ensemble des fichiers csv bruts dans le dossier data/raw
1.2. créer un dossier db dans data s'il n'y est pas (normalement il est importé de puis github)

2. Lancer le fichier main
2.1 UNIQUEMENT POUR LE PREMIER CHARGEMENT : Transformer l'ensemble des données csv brutes en instances
2.2 Lancer l'application via l'interface
"""

from src.project.data.csv_loader import CSVLoader
from src.project.data.database import Database
import src.project.utils.utils_interface as utils_interface


"""
Créer une fonction main a plusieurs avantages :

- avoir des variables locales
- exécuter le code uniquement si on run depuis le bon fichier i.e. main.py
avec la ligne " if __name__ == "__main__": "
- pouvoir changer de runner facilement en important la fonction main dans un autre fichier

"""


""" TESTSSSS

    # test afficher les données pour team de basket
    registre_equipes = db.equipes
    print("=== Équipes chargées ===")
    # .values() permet de récupérer la liste des objets (sans leurs IDs)
    for equipe in registre_equipes.values():
        # L'affichage de l'équipe utilise implicitement la méthode __str__ définie dans ta classe Equipe
        print(f"- {equipe} | Sport: {equipe.discipline.nom}")
        print("liste des joueurs :")
        for joueur in equipe.liste_joueurs:
            print(f"  - {joueur}")

"""


def main():

    print("\n" + "=" * 35)
    print(" ⚙️   Démarrage du programme...\n")
    # 0. Pour le premier import à partir des données brutes :

    reponse_import_raw_data = input(" ⚠️   Attention cette action peut écraser certaines données existantes.\n Souhaitez-vous importer les données brutes ? (o/n) : ")
    print()
    if reponse_import_raw_data.strip().lower() == "o":
        from src.project.data.creation_db_base import chargement_raw_data
        chargement_raw_data()
        print("Les données ont été réinitialisées depuis les csv bruts.")
    else:
        print("Les données n'ont pas été réinitialisées depuis les csv bruts.")

    # 1. initialisation de la bdd
    db = Database()

    # 2. load des données
    print()
    print(" ⚙️   Chargement des données existantes en cours, veuillez patienter...")
    loader = CSVLoader(db=db)
    loader.charger_tout()
    print(" ✅   Chargement terminé !\n")

    # 3. Activation de l'app
    print()
    print("    ===== Bienvenue dans l'application =====     ")
    reponse_admin = ""
    while reponse_admin not in ["o", "n"]:
        reponse_admin = (
            input("Voulez-vous activer le mode administrateur ? (o/n) : ")
            .strip()
            .lower()
        )
    mode_admin = reponse_admin == "o"

    if mode_admin:
        print("\n>>> Mode Administrateur activé (Modifications autorisées) <<<")
    else:
        print("\n>>> Mode Visiteur activé (Lecture seule) <<<")

    # 4. Boucle principale de l'interface
    while True:
        # ici toutes les actions utilisateurs
        print("\n" + "=" * 35)
        print("         MENU PRINCIPAL")
        print("=" * 35)
        print("1. Afficher les sports")
        print("2. Afficher les équipes")
        print("3. Afficher les joueurs")
        print("4. Afficher les matchs")
        print("5. Afficher les compétitions")
        print("0. Quitter l'application")
        print("=" * 35)

        choix = input("Votre choix : ").strip()

        if choix == "1":
            utils_interface.afficher_echantillon_hasard("Liste des Sports", db.sports)

        elif choix == "2":
            utils_interface.afficher_echantillon_hasard("Liste des Équipes", db.equipes)

        elif choix == "3":
            utils_interface.afficher_echantillon_hasard(
                "Liste des Joueurs", db.competiteurs
            )

        elif choix == "4":
            utils_interface.afficher_echantillon_hasard("Liste des Matchs", db.matchs)

        elif choix == "5":
            utils_interface.afficher_echantillon_hasard(
                "Liste des Compétitions", db.competitions
            )

        elif choix == "0":
            print("\nFermeture de l'application. À bientôt :D")
            break

        # La toutes les actions du mode admin :

        # ici autre :
        else:
            print("\nErreur : Choix invalide. Veuillez entrer un chiffre entre 0 et 5.")


if __name__ == "__main__":
    main()
