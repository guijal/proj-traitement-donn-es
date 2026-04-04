from ..models.sport import Sport
from ..models.equipe import Equipe
from ..models.competiteur import Competiteur


class Database:
    """Base de données centralisant toutes les instances de l'application.

    On utilise des dictionnaires pour stocker tous les objets.
    Pour chaque classe (Match, Competition, Competiteur...), on créé un dictionnaire associé dans la database
    Structure des dictionnaires : {id: objet, ...}


    """

    def __init__(self) -> None:
        # Registres pour stocker les objets instanciés par leur identifiant unique
        self.sports: dict[int, Sport] = {}
        self.equipes: dict[int, Equipe] = {}
        self.competiteurs: dict[int, Competiteur] = {}

        # On ajoutera les arbitres, les matchs, etc., ici plus tard.

        # Séquences (Auto-incrément) pour générer des IDs internes uniques
        self._seq_sports = 0
        self._seq_equipes = 0
        self._seq_personnes = 0
        self._seq_matchs = 0
        self._seq_competitions = 0
        self._seq_medailles = 0

    def generer_id_sport(self) -> int:
        self._seq_sports += 1
        return self._seq_sports

    def generer_id_equipe(self) -> int:
        self._seq_equipes += 1
        return self._seq_equipes

    def generer_id_personne(self) -> int:
        self._seq_personnes += 1
        return self._seq_personnes
        
    def generer_id_match(self) -> int:
        self._seq_matchs += 1
        return self._seq_matchs

    def generer_id_competition(self) -> int:
        self._seq_competitions += 1
        return self._seq_competitions

    # placer toutes les méthodes de recherche / modification ici
    # Cela correspond à notre actuelle classe GestionnaireApplication
