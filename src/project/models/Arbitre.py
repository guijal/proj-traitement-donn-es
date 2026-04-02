from .Personne import Personne
from .Sport import Sport


class Arbitre(Personne):
    """
    Simule un arbitre, héritant de Personne.
    """

    def __init__(
        self,
        id_personne: int,
        sex: str,
        nom: str,
        prenom: str,
        date_naissance: tuple[int],
        nationalite: str,
        taille: int,
        poids: int,
        sport_arbitre: Sport,
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
        )
        self.__sport_arbitre = sport_arbitre

    @property
    def sport_arbitre(self):
        return self.__sport_arbitre

    @sport_arbitre.setter
    def sport_arbitre(self, nouveau_sport: Sport):
        assert isinstance(nouveau_sport, Sport)
        self.__sport_arbitre = nouveau_sport

    def __str__(self):
        return f"Arbitre: {self.prenom} {self.nom} ({self.nationalite})"
