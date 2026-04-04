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
        sex: str,
        nom: str,
        prenom: str,
        date_naissance: date,
        nationalite: str,
        taille: int,
        poids: int,
        sport_arbitre: Sport,
        id_csv: int | None = None,
    ):
        super().__init__(
            id_personne,
            sex,
            nom,
            prenom,
            date_naissance,
            nationalite,
            taille,
            poids,
            id_csv,
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
