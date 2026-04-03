from datetime import date, time

from .equipe import Equipe
from .arbitre import Arbitre


class Match:
    """Classe représentant un match entre équipes.

    Attributes
    ----------
    id_match : int
        Identifiant unique
    jour : date
        Date du match
    lieu : str
        Lieu du match
    ville : str
        Ville du match
    liste_equipes_participantes : list[Equipe]
        Equipes participantes
    score : dict[Equipe, int]
        Score par équipe
    heure_debut : time | None
        Heure de début du match
    heure_fin : time | None
        Heure de fin. du match
    arbitre : Arbitre | None
        Arbitre du match
    """
    def __init__(
        self,
        id_match: int,
        jour: date,
        lieu: str,
        ville: str,
        liste_equipes_participantes: list | None = None,
        score: dict | None = None,
        heure_debut: time | None = None,
        heure_fin: time | None = None,
        arbitre=None,
    ):
        if not isinstance(id_match, int):
            raise TypeError("id_match doit être un int")
        if not isinstance(jour, date):
            raise TypeError("jour doit être un datetime.date")
        if not isinstance(lieu, str):
            raise TypeError("lieu doit être un str")
        if not isinstance(ville, str):
            raise TypeError("ville doit être un str")
        self.__id_match = id_match
        self.__heure_debut = heure_debut
        self.__heure_fin = heure_fin
        self.__jour = jour
        self.__ville = ville
        self.__liste_equipes_participantes: list = (
            liste_equipes_participantes if liste_equipes_participantes is not None else []
        )
        self.__score: dict = score if score is not None else {}
        self.__arbitre = arbitre

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Match):
            return self.__id_match == other.__id_match
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__id_match)

    def __str__(self) -> str:
        equipes = " vs ".join(e.nom_abrege for e in self.__liste_equipes_participantes)
        return f"Match n{self.__id_match} - {equipes} le {self.__jour} à {self.__ville}"

    @property
    def id_match(self) -> int:
        """int: Identifiant du match"""
        return self.__id_match

    @id_match.setter
    def id_match(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("id_match doit être un int")
        self.__id_match = valeur

    @property
    def jour(self) -> date:
        """date: Date du match"""
        return self.__jour

    @jour.setter
    def jour(self, valeur: date):
        if not isinstance(valeur, date):
            raise TypeError("jour doit être un datetime.date")
        self.__jour = valeur

    @property
    def lieu(self) -> str:
        """str: Lieu du match"""
        return self.__lieu

    @lieu.setter
    def lieu(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("lieu doit être un str")
        self.__lieu = valeur

    @property
    def ville(self) -> str:
        """str: Ville du match"""
        return self.__ville

    @ville.setter
    def ville(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("ville doit être un str")
        self.__ville = valeur

    @property
    def heure_debut(self):
        """time | None: Heure de début du match"""
        return self.__heure_debut

    @heure_debut.setter
    def heure_debut(self, valeur):
        self.__heure_debut = valeur

    @property
    def heure_fin(self):
        """time | None: Heure de fin du match"""
        return self.__heure_fin

    @heure_fin.setter
    def heure_fin(self, valeur):
        self.__heure_fin = valeur

    @property
    def liste_equipes_participantes(self) -> list:
        """list[Equipe]: Equipes participantes"""
        return self.__liste_equipes_participantes

    @property
    def score(self) -> dict:
        """dict[Equipe, int]: Score par équipe"""
        return self.__score

    @property
    def arbitre(self) -> Arbitre | None:
        """Arbitre | None: Arbitre du match"""
        return self.__arbitre

    @arbitre.setter
    def arbitre(self, valeur):
        self.__arbitre = valeur

    def ajouter_equipe(self, equipe: Equipe) -> None:
        """Ajoute une équipe au match.

        Parameters
        ----------
        equipe : Equipe
            Equipe à ajouter.

        Raises
        ------
        TypeError
            Si l'argument n'est pas une Equipe
        ValueError
            Si l'équipe est déjà dans le match
        """
        if not isinstance(equipe, Equipe):
            raise TypeError("equipe doit être une Equipe")
        if equipe in self.__liste_equipes_participantes:
            raise ValueError("Cette equipe participe déjà au match")
        self.__liste_equipes_participantes.append(equipe)
        self.__score[equipe] = 0

    def ajouter_points(self, equipe: Equipe, nb_points: int) -> None:
        """Ajoute des points au score d'une équipe.

        Parameters
        ----------
        equipe : Equipe
            Equipe à créditer
        nb_points : int
            Nombre de points à ajouter

        Raises
        ------
        TypeError
            Si les types sont incorrects
        ValueError
            Si l'équipe ne participe pas au match
        """
        if not isinstance(equipe, Equipe):
            raise TypeError("equipe doit être une Equipe")
        if not isinstance(nb_points, int):
            raise TypeError("nb_points doit être un int")
        if equipe not in self.__score:
            raise ValueError("Cette équipe ne participe pas au match")
        self.__score[equipe] += nb_points

    def deplacer_match(self, nouvelle_date: date) -> None:
        """Déplace le match à une nouvelle date.

        Parameters
        ----------
        nouvelle_date : date
            Nouvelle date du match
        """
        if not isinstance(nouvelle_date, date):
            raise TypeError("nouvelle_date doit être un datetime.date")
        self.__jour = nouvelle_date

    def vainqueur(self):
        """Retourne l'équipe vainqueure (score le plus élevé).

        Returns
        -------
        Equipe | None
            Equipe vainqueure, ou None si aucun score
        """
        if not self.__score:
            return None
        return max(self.__score, key=lambda e: self.__score[e])

    def perdants(self) -> list:
        """Retourne toutes les équipes sauf le vainqueur.

        Returns
        -------
        list[Equipe]
            Liste des équipes perdantes
        """
        gagnant = self.vainqueur()
        return [e for e in self.__liste_equipes_participantes if e != gagnant]

    def resultats(self) -> str:
        """Retourne une répresentation lisible du score.

        Returns
        -------
        str
            Score formaté
        """
        if not self.__score:
            return "Aucun score enregistré"
        return " | ".join(f"{e.nom_abrege}: {pts}" for e, pts in self.__score.items())

    def classement(self) -> list:
        """Retourne les équipes classées par score décroissant.

        Returns
        -------
        list[tuple[Equipe, int]]
            Liste triée par score décroissant
        """
        return sorted(self.__score.items(), key=lambda x: x[1], reverse=True)
