from ..models.sport import Sport
from ..models.equipe import Equipe
from ..models.competiteur import Competiteur


class Database:
    """Base de données en mémoire centralisant toutes les instances de l'application."""

    def __init__(self) -> None:
        # Registres pour stocker les objets instanciés par leur identifiant unique
        self.sports: dict[int, Sport] = {}
        self.equipes: dict[int, Equipe] = {}
        self.competiteurs: dict[int, Competiteur] = {}

        # On ajoutera les arbitres, les matchs, etc., ici plus tard.
