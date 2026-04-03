from datetime import date

from .personne import Personne
from .sport import Sport


class Coach(Personne):
    """Classe representant un entraîneur, héritant de Personne.

    Attributes
    ----------
    surnom : str
        Surnom ou pseudo de l'entraîneur
    sport_pratique : Sport
        Sport encadré
    nombre_medailles : int
        Nombre de médailles en tant qu'entraîneur
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
        poids: float,
        surnom: str,
        sport_pratique: Sport,
        nombre_medailles: int,
    ):
        super().__init__(
            id_personne, sex, nom, prenom, date_naissance, nationalite, taille, poids
        )
        if not isinstance(surnom, str):
            raise TypeError("surnom doit être un str")
        if not isinstance(sport_pratique, Sport):
            raise TypeError("sport_pratique doit être un Sport")
        if not isinstance(nombre_medailles, int):
            raise TypeError("nombre_medailles doit être un int.")

        self.__surnom = surnom
        self.__sport_pratique = sport_pratique
        self.__nombre_medailles = nombre_medailles

    def __str__(self) -> str:
        return (
            f"Coach: {self.prenom} {self.nom}"
            f" ({self.__surnom}) - {self.__sport_pratique.nom}"
        )

    def recuperer_info(self) -> str:
        """Retourne un résumé des informations du coach.

        Returns
        -------
        str
            résumé lisible
        """
        return (
            f"{self.prenom} {self.nom} | Coach {self.__sport_pratique.nom} | "
            f"Médailles: {self.__nombre_medailles}"
        )

    @property
    def surnom(self) -> str:
        """str: Surnom"""
        return self.__surnom

    @surnom.setter
    def surnom(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("surnom doit etre un str")
        self.__surnom = valeur

    @property
    def sport_pratique(self) -> Sport:
        """Sport: Sport encadré"""
        return self.__sport_pratique

    @sport_pratique.setter
    def sport_pratique(self, valeur: Sport):
        if not isinstance(valeur, Sport):
            raise TypeError("sport_pratique doit être un Sport")
        self.__sport_pratique = valeur

    @property
    def nombre_medailles(self) -> int:
        """int: Nombre de médailles"""
        return self.__nombre_medailles

    @nombre_medailles.setter
    def nombre_medailles(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("nombre_medailles doit être un int")
        self.__nombre_medailles = valeur
