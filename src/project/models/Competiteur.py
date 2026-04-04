from datetime import date

from .personne import Personne
from .sport import Sport


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
        nom: str,
        prenom: str,
        sport_pratique: Sport,
        sex: str | None = None,
        date_naissance: date | None = None,
        nationalite: str | None = None,
        taille: float | None = None,
        poids: float | None = None,
        surnom: str | None = None,
        numero_maillot: int | None = None,
        poste_principal: str | None = None,
        nombre_medailles: int = 0,
        id_csv: int | None = None,
    ):
        super().__init__(
            id_personne=id_personne,
            nom=nom,
            prenom=prenom,
            sex=sex,
            date_naissance=date_naissance,
            nationalite=nationalite,
            taille=taille,
            poids=poids,
            id_csv=id_csv,
        )
        if surnom is not None and not isinstance(surnom, str):
            raise TypeError("surnom doit être un str")
        if not isinstance(sport_pratique, Sport):
            raise TypeError("sport_pratique doit être un Sport")
        if numero_maillot is not None and not isinstance(numero_maillot, int):
            raise TypeError("numero_maillot doit être un int")
        if poste_principal is not None and not isinstance(poste_principal, str):
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
    def surnom(self) -> str | None:
        """str | None: Surnom ou pseudo"""
        return self.__surnom

    @surnom.setter
    def surnom(self, valeur: str | None):
        if valeur is not None and not isinstance(valeur, str):
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
    def numero_maillot(self) -> int | None:
        """int | None: Numéro de maillot"""
        return self.__numero_maillot

    @numero_maillot.setter
    def numero_maillot(self, valeur: int | None):
        if valeur is not None and not isinstance(valeur, int):
            raise TypeError("numero_maillot doit être un int")
        self.__numero_maillot = valeur

    @property
    def poste_principal(self) -> str | None:
        """str | None: Poste ou rôle principal"""
        return self.__poste_principal

    @poste_principal.setter
    def poste_principal(self, valeur: str | None):
        if valeur is not None and not isinstance(valeur, str):
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
