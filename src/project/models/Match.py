from .equipe import Equipe
from .arbitre import Arbitre


class Match:
    def __init__(self, id_match: int, heure_debut: tuple[int], heure_fin: tuple[int], jour: tuple[int], lieu: str, ville: str, liste_equipes_participantes: list[Equipe]=, score: dict[Equipe], arbitre: Arbitre):
        self.__id_match = id_match
        self.__heure_debut = heure_debut
        self.__heure_fin = heure_fin
        self.__jour = jour
        self.__ville = ville
        self.__liste_equipes_participantes = liste_equipes_participantes
        self.__score = score
        self.__arbitre = arbitre

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Match):
            return self.__id_match == other.__id_match
        return NotImplemented

    @property.getter
        
    @property.setter


    def ajouter_points(self, equipe: Equipe, nb_points: int):
        self.__score[Equipe] += nb_points

    def ajouter_equipes(self, liste_equipes: list[Equipe]):
        self.__liste_equipes_participantes.append(liste_equipes)

    

    



