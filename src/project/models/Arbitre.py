from datetime import date

from .personne import Personne
from .sport import Sport


class Arbitre(Personne):
    """
    Classe représentant un arbitre, héritant de Personne.

    Attributes
    ----------
    sport_arbitre : Sport
        Sport arbitré par cet arbitre
    """

    def __init__(
        self,
        id_personne: int,
        nom: str,
        prenom: str,
        sport_arbitre: Sport,
        sex: str | None = None,
        date_naissance: date | None = None,
        nationalite: str | None = None,
        pays: str | None = None,
        taille: float | None = None,
        poids: float | None = None,
    ):
        super().__init__(
            id_personne=id_personne,
            nom=nom,
            prenom=prenom,
            sex=sex,
            date_naissance=date_naissance,
            nationalite=nationalite,
            pays=pays,
            taille=taille,
            poids=poids,
        )
        if not isinstance(sport_arbitre, Sport):
            raise TypeError("sport_arbitre doit être un Sport")
        self.__sport_arbitre = sport_arbitre

    def __str__(self) -> str:
        return f"Arbitre: {self.prenom} {self.nom} - {self.__sport_arbitre.nom}"

    @property
    def sport_arbitre(self):
        """Sport: Sport arbitre."""
        return self.__sport_arbitre

    @sport_arbitre.setter
    def sport_arbitre(self, nouveau_sport: Sport):
        if not isinstance(nouveau_sport, Sport):
            raise TypeError("sport_arbitre doit être un Sport")
        self.__sport_arbitre = nouveau_sport
