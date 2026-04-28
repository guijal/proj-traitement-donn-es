from .database import Database
from .basketball_loader import BasketballLoader
from .badminton_loader import BadmintonLoader
    


class CSVLoader:
    """Classe permettant de charger tous les CSV

    Pour chaque jeu de donnée, on créera une sous classe à partir de la classe BaseLoader pour importer les données.
    En effet, les fichiers ayant des structures trop différentes il faut s'adapter à chaque fois pour l'import.
    Cependant on garde une structure d'import de base. c.d. base_loader.py et l'ensemble des méthodes associées
 
    """

    def __init__(self, data_directory: str, db: Database):
        self.data_directory = data_directory
        self.db = db

    def charger_tout(self) -> None:
        """On charge toutes les données
        
        Pour chaque "dossier de données", on instancie le loader spécifique puis on charge les données.
        """
        # On délègue le chargement de chaque sport à son loader spécifique
        loader_basket = BasketballLoader(self.data_directory, self.db)
        loader_basket.charger_tout()

        loader_badminton = BadmintonLoader(self.data_directory, self.db)
        loader_badminton.charger_tout()


        # On ajoutera tous les autres loaders ici

        # loader_foot = FootballLoader(self.data_directory, self.db)
        # loader_foot.charger_tout()
