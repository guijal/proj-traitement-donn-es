from .database import Database
from .basketball_converter import BasketballConverter
from .badminton_converter import BadmintonConverter
from .football_converter import FootballConverter


class CSVConverter:
    """Classe permettant de charger tous les CSV

    Pour chaque jeu de donnée, on créera une sous classe à partir de la classe BaseConverter pour importer les données.
    En effet, les fichiers ayant des structures trop différentes il faut s'adapter à chaque fois pour l'import.
    Cependant on garde une structure d'import de base. c.d. base_converter.py et l'ensemble des méthodes associées

    """

    def __init__(self, data_directory: str, db: Database):
        self.data_directory = data_directory
        self.db = db

    def charger_tout(self) -> None:
        """On charge toutes les données

        Pour chaque "dossier de données", on instancie le converter spécifique puis on charge les données.
        """
        # On délègue le chargement de chaque sport à son converter spécifique
        converter_basket = BasketballConverter(self.data_directory, self.db)
        converter_basket.charger_tout()

        converter_badminton = BadmintonConverter(self.data_directory, self.db)
        converter_badminton.charger_tout()

        # On ajoutera tous les autres converters ici

        converter_foot = FootballConverter(self.data_directory, self.db)
        converter_foot.charger_tout()
