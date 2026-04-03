from datetime import date

from .Personne import Personne
from .Sport import Sport


class Competiteur(Personne):
    """Classe representant un compétiteur, héritant de Personne.

    Attributes
    ----------
    surnom : str
        Surnom ou pseudo du compétiteur
    sport_pratique : Sport
        Sport pratiqué
    numero_maillot : int
        Numéro de maillot
    poste_principal : str
        Poste ou rôle principal dans l'équipe
    nombre_medailles : int
        Nombre total de médailles remportées
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
        numero_maillot: int,
        poste_principal: str,
        nombre_medailles: int,
    ):
        super().__init__(
            id_personne,
            sex,
            nom,
            prenom,
            date_naissance,
            nationalite,
            taille,
            poids
        )
        if not isinstance(surnom, str):
            raise TypeError("surnom doit être un str")
        if not isinstance(sport_pratique, Sport):
            raise TypeError("sport_pratique doit être un Sport")
        if not isinstance(numero_maillot, int):
            raise TypeError("numero_maillot doit être un int")
        if not isinstance(poste_principal, str):
            raise TypeError("poste_principal doit être un str")
        if not isinstance(nombre_medailles, int):
            raise TypeError("nombre_medailles doit être un int")

        self.__surnom = surnom
        self.__sport_pratique = sport_pratique
        self.__numero_maillot = numero_maillot
        self.__poste_principal = poste_principal
        self.__nombre_medailles = nombre_medailles

    def __str__(self) -> str:
        return (
            f"Compétiteur: {self.prenom} {self.nom}"
            f" ({self.__surnom}) - {self.__sport_pratique.nom}"
        )

    def recuperer_info(self) -> str:
        """Retourne un résumé des informations du compétiteur.

        Returns
        -------
        str
            Résumé lisible
        """
        return (
            f"{self.prenom} {self.nom} | {self.__sport_pratique.nom} | "
            f"Poste: {self.__poste_principal} | "
            f"Médailles: {self.__nombre_medailles}"
        )

    @property
    def surnom(self) -> str:
        """str: Surnom ou pseudo"""
        return self.__surnom

    @surnom.setter
    def surnom(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("surnom doit être un str")
        self.__surnom = valeur

    @property
    def sport_pratique(self) -> Sport:
        """Sport: Sport pratiqué"""
        return self.__sport_pratique

    @sport_pratique.setter
    def sport_pratique(self, valeur: Sport):
        if not isinstance(valeur, Sport):
            raise TypeError("sport_pratique doit être un Sport")
        self.__sport_pratique = valeur

    @property
    def numero_maillot(self) -> int:
        """int: Numéro de maillot"""
        return self.__numero_maillot

    @numero_maillot.setter
    def numero_maillot(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("numero_maillot doit être un int")
        self.__numero_maillot = valeur

    @property
    def poste_principal(self) -> str:
        """str: Poste ou rôle principal"""
        return self.__poste_principal

    @poste_principal.setter
    def poste_principal(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("poste_principal doit être un str")
        self.__poste_principal = valeur

    @property
    def nombre_medailles(self) -> int:
        """int: Nombre de médailles"""
        return self.__nombre_medailles

    @nombre_medailles.setter
    def nombre_medailles(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("nombre_medailles doit être un int")
        self.__nombre_medailles = valeur
