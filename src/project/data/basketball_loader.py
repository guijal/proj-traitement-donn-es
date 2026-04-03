from ..models.equipe import Equipe
from ..models.sport import Sport
from .base_loader import BaseLoader


class BasketballLoader(BaseLoader):
    """Loader spécifique pour les données de basketball."""

    def __init__(self, data_directory: str, db):
        # Initialise la classe parente (BaseLoader) pour récupérer db et data_directory
        super().__init__(data_directory, db)

        # Création dynamique du sport "Basketball" puisqu'il n'y a plus de sports.csv global
        self.id_sport = 1
        if self.id_sport not in self.db.sports:
            sport_basket = Sport(
                nom="Basketball",
                numero=self.id_sport,
                nb_joueurs_par_equipe=5,
                nb_equipes=0,  # Peut être recalculé plus tard
            )
            self.db.sports[self.id_sport] = sport_basket

        self.sport = self.db.sports[self.id_sport]

    def charger_tout(self) -> None:
        """Orchestre le chargement de toutes les données liées au basketball."""
        self.charger_equipes("basketball/team.csv")
        # À l'avenir, tu pourras ajouter :
        # self.charger_matchs("basketball/match.csv")
        # self.charger_games("basketball/game.csv")

    def charger_equipes(self, nom_fichier: str) -> None:
        donnees = self._lire_csv(nom_fichier)

        for ligne in donnees:
            id_equipe = int(ligne["id"])
            equipe = Equipe(
                id_equipe=id_equipe,
                nom_officiel=ligne["full_name"],
                nom_abrege=ligne["abbreviation"],
                ville=ligne["city"],
                pays="USA",
                code_pays=ligne["state"],
                genre="masculin",
                discipline=self.sport,  # On utilise directement l'attribut créé dans __init__
                annee_fondation=1900,
                nb_medailles=0,
            )
            # Ajout au registre global partagé du CSVLoader principal
            self.db.equipes[id_equipe] = equipe
            # mettre ici les ajout aux classes qui dépendent par ex
            # à la création dun joueur il faut modifier Equipe
