"""
étapes pour lancer l'application :

1. Transformer l'ensemble des données csv en instances
2. Lancer l'application via l'interface
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
    
    #test sports
    registre_sports = db.sports
    print("=== Sports chargées ===")
    for sport in registre_sports.values():
        print(f"- {sport}")

    #test joueurs basket
    registre_joueurs = db.competiteurs
    print("=== Joueurs chargées ===")
    for joueur in registre_joueurs.values():
        print(f"- {joueur}")


        for equipe in registre_equipes.values():
            if joueur in equipe.liste_joueurs:
                print("Equipe du joueur :", equipe.nom_officiel)
    

"""


def main():
    # 1. initialisation de la bdd
    db = Database()

    # 2. load des données
    print("Chargement des données en cours, veuillez patienter...")
    loader = CSVLoader(data_directory="data/raw", db=db)
    loader.charger_tout()
    print("Chargement terminé !\n")

    # 3. Activation de l'app
    print("     ===== Bienvenue dans l'application =====     ")
    reponse_admin = (
        input("Voulez-vous activer le mode administrateur ? (o/n) : ").strip().lower()
    )
    mode_admin = reponse_admin == "o" or reponse_admin == "oui"

    if mode_admin:
        print("\n>>> Mode Administrateur activé (Modifications autorisées) <<<")
    else:
        print("\n>>> Mode Visiteur activé (Lecture seule) <<<")

    # 4. Boucle principale de l'interface
    while True:
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

        else:
            print("\nErreur : Choix invalide. Veuillez entrer un chiffre entre 0 et 5.")


if __name__ == "__main__":
    main()
