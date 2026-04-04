from .database import Database
from .basketball_loader import BasketballLoader


class CSVLoader:
    """Classe permettant de charger tous les CSV

    Pour chaque jeu de donnée, on créera une sous classe pour importer les données.
    En effet, les fichiers ayant des structures trop différentes il faut s'adapter à chaque fois pour l'import.
    Cependant pour garder une s
    """

    def __init__(self, data_directory: str, db: Database):
        self.data_directory = data_directory
        self.db = db

    def charger_tout(self) -> None:
        """Point d'entrée principal qui charge les fichiers dans le bon ordre."""
        # On délègue le chargement de chaque sport à son loader spécifique
        loader_basket = BasketballLoader(self.data_directory, self.db)
        loader_basket.charger_tout()

        # On ajoutera tous les autres loaders ici
        
        # loader_foot = FootballLoader(self.data_directory, self.db)
        # loader_foot.charger_tout()
