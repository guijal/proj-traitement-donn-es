from ..models.equipe import Equipe
from ..models.sport import Sport
from .base_loader import BaseLoader


class BasketballLoader(BaseLoader):
    """Loader spécifique pour les données de basketball.
    
    Suit la structure d'import générale (c.d. base_loader.py)
    """

    def __init__(self, data_directory: str, db):
        # Initialise la classe parente (BaseLoader) pour récupérer db et data_directory
        super().__init__(data_directory, db)

        # Dans cette partie on créé le/les sports en lien avec les csv car il n'y a pas de "sports.csv", il faut les créer un par un selon les données fournies
        # Création  sport "Basketball"
        self.id_csv_sport = 1
        if self.id_csv_sport not in self.map_sports:
            nouvel_id_sport = self.db.generer_id_sport()
            self.map_sports[self.id_csv_sport] = nouvel_id_sport
            sport_basket = Sport(
                nom="Basketball",
                numero=nouvel_id_sport,
                nb_joueurs_par_equipe=5,
                nb_equipes=0,  # dv
                id_csv=self.id_csv_sport,
            )
            self.db.sports[nouvel_id_sport] = sport_basket

        self.sport = self.db.sports[self.map_sports[self.id_csv_sport]]

    def charger_tout(self) -> None:
        """Orchestre le chargement de toutes les données liées au basketball."""
        self.charger_equipes("basketball/team.csv")
        # À l'avenir, tu pourras ajouter :
        # self.charger_matchs("basketball/match.csv")
        # self.charger_games("basketball/game.csv")

    def charger_equipes(self, nom_fichier: str) -> None:
        donnees = self._lire_csv(nom_fichier)

        for ligne in donnees:
            id_csv = int(ligne["id"])
            
            nouvel_id = self.db.generer_id_equipe()
            self.map_equipes[id_csv] = nouvel_id

            equipe = Equipe(
                id_equipe=nouvel_id,
                nom_officiel=ligne["full_name"],
                nom_abrege=ligne["abbreviation"],
                ville=ligne["city"],
                pays="USA",
                code_pays=ligne["state"],
                genre="masculin",
                discipline=self.sport,  # On utilise directement l'attribut créé dans __init__
                annee_fondation=1900,
                nb_medailles=0,
                id_csv=id_csv,
            )
            # Ajout au registre global partagé du CSVLoader principal
            self.db.equipes[nouvel_id] = equipe

            # mettre ici les ajout aux classes qui dépendent par ex
            # à la création dun joueur il faut modifier Equipe
