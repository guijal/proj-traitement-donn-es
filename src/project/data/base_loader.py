import csv
from datetime import datetime
from abc import ABC, abstractmethod
from pathlib import Path

from .database import Database


class BaseLoader(ABC):
    """Classe de base fournissant les outils nécessaires à tous les loaders spécifiques.

    Pour linstant les dossiers fournis correspondent à un sport et à l'intérieur les tables ont des relations.
    C'est pourquoi la structure d'import est la suivante :

    Cependant cela n'empêche en rien d'importer d'autres structures de données s'il venait à en y avoir.
    Il suffit de créer, comme pour les sports, une sous classe de BaseLoader et d'adapter l'import.
    Si cette structure venait à être commune, on ajoute simplement de nouvelles méthodes dans cette classe pour généraliser le nouveau type d'import.

    Structure d'import générale :

    - création des tables de mapping pour les relations inter-csv (= intra-sport)
    - création d'un id unique pour le Sport (ou autre plus tard)
    - import ligne par ligne en faisant correspondre les données aux classes (données brutes)
    - modification des objets existants suite à la création du nouvel objet. Ex en créant un joueur on l'ajoute à son équipe. ("données relationnelles")

    """

    def __init__(self, data_directory: str, db: Database):
        """Initialise le loader.

        Chaque loader accède à son dossier de données brut et remplit la bdd

        Attributes
        ----------
        data_directory : str
            Chemin du dossier de données brut
        db : Database
            Instance de la base de données partagée par tous les loaders

        """
        self.data_directory = data_directory
        self.db = db

        # Tables de mapping : {id_du_csv: id_unique_database}
        # on crée l'ensemble des tables puis elles seront utilisées au besoin

        self.map_equipes: dict[int, int] = {}
        self.map_personnes: dict[int, int] = {}
        self.map_matchs: dict[int, int] = {}
        self.map_competitions: dict[int, int] = {}
        self.map_medailles: dict[int, int] = {}

    @abstractmethod
    def charger_tout(self) -> None:
        """Chaque sous-classe devra implémenter l'orchestration de ses propres fichiers."""
        pass

    # méthodes utilitaires :

    def _lire_csv(self, nom_fichier: str) -> list[dict]:
        """Méthode pour lire un CSV et retourner une liste de dictionnaires."""
        chemin_complet = Path(self.data_directory) / nom_fichier
        with open(chemin_complet, mode="r", encoding="utf-8") as fichier:
            return list(csv.DictReader(fichier))
        # chaque elt de la liste est un dictionnaire qui contient {variable:valeur}. Ex {nom:Fiodor}

    @staticmethod
    def _parser_date(date_str: str):
        if date_str == "": 
            return None
        return datetime.strptime(date_str, "%Y-%m-%d").date()

    @staticmethod
    def _parser_height(height_str: str):
        if height_str == "":
            return None
        try:
            pieds, pouces = height_str.split("-")
            # 1 pied = 30.48 cm, 1 pouce = 2.54 cm
            return float(pieds) * 30.48 + float(pouces) * 2.54
        except ValueError:
            # Fallback si la taille n'est pas au format "x-y" (ex: déjà un nombre)
            return float(height_str)

    @staticmethod
    def _parser_weight(weight_str: str):
        if weight_str == "" or weight_str is None:
            return None
        try:
            # Conversion de lbs en kg (1 lb = 0.453592 kg)
            return float(weight_str) * 0.453592
        except ValueError:
            return float(weight_str)
