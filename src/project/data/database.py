from ..models.sport import Sport
from ..models.equipe import Equipe
from ..models.competiteur import Competiteur


class Database:
    """Base de données centralisant toutes les instances de l'application.

    On utilise des dictionnaires pour stocker tous les objets.
    Pour chaque classe (Match, Competition, Competiteur...), on créé un dictionnaire associé dans la database
    Structure des dictionnaires : {id: objet}
    L'id est une clé primaire qui est incrémentée par l'attribut protégé _auto_increment_id_XXX (passer par un incrément permet de gérer les problèmes en cas de suppression (si on prend le len par ex)))


    """

    def __init__(self) -> None:
        # Dictionnaires pour stocker les objets instanciés par leur id unique (c'est une clé primaire quoi)
        self.sports: dict[int, Sport] = {}
        self.equipes: dict[int, Equipe] = {}
        self.competiteurs: dict[int, Competiteur] = {}

        # On ajoutera les arbitres, les matchs, ou toute autre classe considérée comme "donnée" ici.
        # Puis on leur attribut un id unique

        # Auto-incrément pour générer les id uniques
        self._auto_increment_id_sport = 0
        self._auto_increment_id_equipe = 0
        self._auto_increment_id_personne = 0
        self._auto_increment_id_match = 0
        self._auto_increment_id_competition = 0
        self._auto_increment_id_medaille = 0

    # Pour chaque id on créer une méthode qui génère le bon id (on modifie par directement l'attribut protégé)
    def generer_id_sport(self) -> int:
        self._auto_increment_id_sport += 1
        return self._auto_increment_id_sport

    def generer_id_equipe(self) -> int:
        self._auto_increment_id_equipe += 1
        return self._auto_increment_id_equipe

    def generer_id_personne(self) -> int:
        self._auto_increment_id_personne += 1
        return self._auto_increment_id_personne

    def generer_id_match(self) -> int:
        self._auto_increment_id_match += 1
        return self._auto_increment_id_match

    def generer_id_competition(self) -> int:
        self._auto_increment_id_competition += 1
        return self._auto_increment_id_competition

#  - - - - - - - - - - 
    #
    # placer toutes les méthodes de recherche / modification ici
    # Cela correspond à notre actuelle classe GestionnaireApplication
