from .database import Database
from .base_loader import BaseLoader
from ..models.Equipe import Equipe
from ..models.Sport import Sport
from ..models.Competiteur import Competiteur
from ..models.Match import Match
from ..models.Competition import Competition


class CSVLoader(BaseLoader):
    """Classe permettant de charger tous les CSV

    Pour chaque jeu de donnée, on créera une sous classe à partir de la classe BaseLoader pour importer les données.
    En effet, les fichiers ayant des structures trop différentes il faut s'adapter à chaque fois pour l'import.
    Cependant on garde une structure d'import de base. c.d. base_loader.py et l'ensemble des méthodes associées

    """

    def __init__(self, db: Database):
        self.data_directory = "data/db/"
        self.db = db

    def charger_tout(self) -> None:
        """On charge toutes les données

        Pour chaque "dossier de données", on instancie le loader spécifique puis on charge les données.
        """

        sports = self._lire_csv(nom_fichier="sports.csv")
        for sport in sports:
            self.db.sports[sport["id"]] = Sport(
                nom=sport["_Sport__nom"],
                numero=int(sport["id"]),
                nb_joueurs_par_equipe=int(sport["_Sport__nb_joueurs_par_equipe"]),
                nb_equipes=int(sport["_Sport__nb_equipes"]),
            )

        competiteurs = self._lire_csv(nom_fichier="competiteurs.csv")
        for competiteur in competiteurs:
            comp = Competiteur(
                id_personne=int(competiteur["id"]),
                nom=competiteur["_Personne__nom"],
                prenom=competiteur["_Personne__prenom"],
                sport_pratique=self.db.sports[
                    competiteur["_Competiteur__sport_pratique"]
                ],
                pays=competiteur["_Personne__pays"],
            )
            self.db.competiteurs[competiteur["id"]] = competiteur
