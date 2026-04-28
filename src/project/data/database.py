from ..models.Sport import Sport
from ..models.Equipe import Equipe
from ..models.Competiteur import Competiteur
from ..models.Match import Match
from ..models.Competition import Competition
from ..models.Arbitre import Arbitre
from ..models.Coach import Coach
from ..models.Medaille import Medaille
from ..models.Tournoi import Tournoi


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
        self.matchs: dict[int, Match] = {}
        self.competitions: dict[int, Competition] = {}
        self.arbitres: dict[int, Arbitre] = {}
        self.coachs: dict[int, Coach] = {}
        self.medailles: dict[int, Medaille] = {}
        self.tournois: dict[int, Tournoi] = {}

        # On ajoutera les arbitres, les matchs, ou toute autre classe considérée comme "donnée" ici.
        # Puis on leur attribut un id unique

        # Auto-incrément pour générer les id uniques
        self._auto_increment_id_sport = 0
        self._auto_increment_id_equipe = 0
        self._auto_increment_id_competiteur = 0
        self._auto_increment_id_match = 0
        self._auto_increment_id_competition = 0
        self._auto_increment_id_medaille = 0
        self._auto_increment_id_arbitre = 0
        self._auto_increment_id_coach = 0
        self._auto_increment_id_tournoi = 0

    # Pour chaque id on créer une méthode qui génère le bon id (on modifie par directement l'attribut protégé)
    def generer_id_sport(self) -> int:
        self._auto_increment_id_sport += 1
        return self._auto_increment_id_sport

    def generer_id_equipe(self) -> int:
        self._auto_increment_id_equipe += 1
        return self._auto_increment_id_equipe

    def generer_id_competiteur(self) -> int:
        self._auto_increment_id_competiteur += 1
        return self._auto_increment_id_competiteur

    def generer_id_match(self) -> int:
        self._auto_increment_id_match += 1
        return self._auto_increment_id_match

    def generer_id_competition(self) -> int:
        self._auto_increment_id_competition += 1
        return self._auto_increment_id_competition

    def generer_id_arbitre(self) -> int:
        self._auto_increment_id_arbitre += 1
        return self._auto_increment_id_arbitre

    def generer_id_coach(self) -> int:
        self._auto_increment_id_coach += 1
        return self._auto_increment_id_coach

    def generer_id_medaille(self) -> int:
        self._auto_increment_id_medaille += 1
        return self._auto_increment_id_medaille

    def generer_id_tournoi(self) -> int:
        self._auto_increment_id_tournoi += 1
        return self._auto_increment_id_tournoi


#  - - - - - - - - - -
#
# placer toutes les méthodes de recherche / modification ici
# Cela correspond à notre actuelle classe GestionnaireApplication mais restreinte ( pas la gestion admin )
