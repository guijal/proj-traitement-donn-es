from .database import Database
import csv
import pandas as pd


def enregister_list(data_directory: str, dico: dict):
    # On crée une liste de dictionnaires en fusionnant l'ID et les attributs
    liste_donnees = []
    for idx, objet in dico.items():
        dico_ligne = {"id": idx}  # On commence par l'ID
        dico_ligne.update(objet.__dict__)  # On ajoute tous les attributs de la classe
        liste_donnees.append(dico_ligne)

    # Création du DataFrame
    df = pd.DataFrame(liste_donnees)

    # Enregistrement du DataFrame dans un fichier CSV

    df.to_csv(data_directory + ".csv", index=False, encoding="utf-8")


def enregister_list_equipe(data_directory: str, dico: dict):
    # On crée une liste de dictionnaires en fusionnant l'ID et les attributs
    liste_donnees = []
    for idx, objet in dico.items():
        dico_ligne = {"id": idx}  # On commence par l'ID
        dico_ligne.update(objet.__dict__)  # On ajoute tous les attributs de la classe
        dico_ligne["_Equipe__discipline"] = dico[idx].discipline.numero
        l = []
        for joueur in dico[idx].liste_joueurs:
            l.append(joueur.id_personne)
        dico_ligne["_Equipe__liste_joueurs"] = l
        l2 = []
        for coach in dico[idx].liste_coachs:
            l2.append(coach.id_personne)
        dico_ligne["_Equipe__liste_coachs"] = l2

        liste_donnees.append(dico_ligne)

    # Création du DataFrame
    df = pd.DataFrame(liste_donnees)

    # Enregistrement du DataFrame dans un fichier CSV

    df.to_csv(data_directory + ".csv", index=False, encoding="utf-8")


def enregister_list_matchs(data_directory: str, dico: dict):
    # On crée une liste de dictionnaires en fusionnant l'ID et les attributs
    liste_donnees = []
    for idx, objet in dico.items():
        dico_ligne = {"id": idx}  # On commence par l'ID
        dico_ligne.update(objet.__dict__)  # On ajoute tous les attributs de la classe
        l = []
        for equipe in dico[idx].liste_equipes_participantes:
            l.append(equipe.id_equipe)
        dico_ligne["_Match__liste_equipes_participantes"] = l

        if dico[idx].arbitre is not None:
            dico_ligne["_Match__arbitre"] = dico[idx].arbitre.id_personne

        l_score = []
        for equipe, score in dico[idx].score.items():
            l_score.append((equipe.id_equipe, score))
        dico_ligne["_Match__score"] = l_score

        liste_donnees.append(dico_ligne)

    # Création du DataFrame
    df = pd.DataFrame(liste_donnees)

    # Enregistrement du DataFrame dans un fichier CSV

    df.to_csv(data_directory + ".csv", index=False, encoding="utf-8")


def enregister_list_competiteurs(data_directory: str, dico: dict):
    # On crée une liste de dictionnaires en fusionnant l'ID et les attributs
    liste_donnees = []
    for idx, objet in dico.items():
        dico_ligne = {"id": idx}  # On commence par l'ID
        dico_ligne.update(objet.__dict__)  # On ajoute tous les attributs de la classe

        dico_ligne["_Competiteur__sport_pratique"] = dico[idx].sport_pratique.numero

        liste_donnees.append(dico_ligne)

    # Création du DataFrame
    df = pd.DataFrame(liste_donnees)

    # Enregistrement du DataFrame dans un fichier CSV

    df.to_csv(data_directory + ".csv", index=False, encoding="utf-8")


def sauvegarder_donnees_csv(data_directory: str, db):
    """
    Sauvegarde les données de la base de données dans des fichiers CSV.
    """
    enregister_list(data_directory + "/sports", db.sports)
    enregister_list_equipe(data_directory + "/equipes", db.equipes)
    enregister_list_competiteurs(data_directory + "/competiteurs", db.competiteurs)
    enregister_list_matchs(data_directory + "/matchs", db.matchs)
    enregister_list(data_directory + "/competitions", db.competitions)
    enregister_list(data_directory + "/arbitres", db.arbitres)
    enregister_list(data_directory + "/coachs", db.coachs)
    enregister_list(data_directory + "/medailles", db.medailles)
    enregister_list(data_directory + "/tournois", db.tournois)
