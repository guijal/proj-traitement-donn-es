import csv
from datetime import datetime
from abc import ABC, abstractmethod
from pathlib import Path

from ..models.Sport import Sport
from ..models.Equipe import Equipe
from ..models.Competiteur import Competiteur
from ..models.Match import Match
from ..models.Competition import Competition

from .database import Database


class BaseLoader(ABC):
    """Classe de base fournissant les outils nécessaires à tous les loaders spécifiques.

    Pour linstant les dossiers fournis correspondent à un sport et à l'intérieur les tables ont des relations.
    C'est pourquoi la structure d'import est la suivante :

    [Cependant cela n'empêche en rien d'importer d'autres structures de données s'il venait à en y avoir.
    Il suffit de créer, comme pour les sports, une sous classe de BaseLoader et d'adapter l'import.
    Si cette structure venait à être commune, on ajoute simplement de nouvelles méthodes dans cette classe pour généraliser le nouveau type d'import.]

    Structure d'import générale :

    - création des tables de mapping pour les relations inter-csv (= intra-sport)
    - création d'un id unique pour le Sport (ou autre plus tard) et ajout du sport "mannuellement"
    - ajout manuel d'autres classe si nécessaire, e.g. Competition
    - Pour chaque fichier csv :
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

    # méthodes de load

    def unique_charger_sport(
        self, nom: str, nb_joueurs_par_equipe: int, nb_equipes: int
    ) -> None:
        """load du sport

        La structure des données étant spéciale. Il faut importer le sport "manuellement" à partir de notre connaissance des bdd
        C'est à ça que sert cette méthode

        Parameters
        ----------
        nom : str
            Nom du sport
        nb_joueurs_par_equipe : int
            Nombre de joueurs par équipe
        nb_equipes : int
            Nombre d'équipes par compétition
        """
        nouvel_id_sport = self.db.generer_id_sport()
        sport_basket = Sport(
            nom=nom,
            numero=nouvel_id_sport,
            nb_joueurs_par_equipe=nb_joueurs_par_equipe,
            nb_equipes=nb_equipes,
        )
        # ajout à la db
        self.db.sports[nouvel_id_sport] = sport_basket

        # on crée un attribut qui stocke le sport (pour le réutiliser après)
        self.sport = sport_basket

    # on peut utiliser les kwargs ici
    def unique_charger_competition(
        self,
        nom: str,
        edition: str | None = None,
        organisateur: str | None = None,
        date_debut: str | None = None,
        date_fin: str | None = None,
    ):
        """Load manuel d'une compétition

        Parameters
        ----------
        nom : str
            Nom de la compétition
        edition : str | None
            Edition de la compétition
        organisateur : str | None
            Organisateur de la compétition
        date_debut : str | None
            Date de début de la compétition
        date_fin : str | None
            Date de fin de la compétition
        """
        nouvel_id_competition = self.db.generer_id_competition()
        competition = Competition(
            id_competition=nouvel_id_competition,
            nom=nom,
            edition=edition,
            organisateur=organisateur,
            date_debut=self._parser_date(date_debut),
            date_fin=self._parser_date(date_fin),
        )
        # ajout à la db
        self.db.competitions[nouvel_id_competition] = competition

        self.competition = competition
        # pour réutilisation

    # - - -  - - - -
    # méthodes utilitaires :

    def _lire_csv(self, nom_fichier: str) -> list[dict]:
        """Méthode pour lire un CSV et retourner une liste de dictionnaires."""
        chemin_complet = Path(self.data_directory) / nom_fichier
        with open(chemin_complet, mode="r", encoding="utf-8") as fichier:
            return list(csv.DictReader(fichier))
        # chaque elt de la liste est un dictionnaire qui contient {variable:valeur}. Ex {nom:Fiodor}

    @staticmethod
    def _parser_date(date_str: str | None):
        if date_str == "" or date_str is None:
            return None
        try:
            return datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S").date()
        except ValueError:
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
        # Conversion de lbs en kg (1 lb = 0.453592 kg)
        return float(weight_str) * 0.453592

    @staticmethod
    def _parser_stats_diverses_auto(colonne: str, valeur: str, dico: dict):
        try:
            if "." in valeur:
                dico[colonne] = float(valeur)
            else:
                dico[colonne] = int(valeur)
        except ValueError:
            # Si ce n'est pas un nombre on laisse en str
            dico[colonne] = valeur

    @staticmethod
    def _parser_prenom_nom(nom_complet: str) -> tuple[str, str]:
        prenom = nom_complet.split(" ")[0]  # ce quil y a avant le premier espace
        nom = " ".join(
            nom_complet.split(" ")[1:]
        )  # ce quil y a après le premier espace
        return prenom, nom
