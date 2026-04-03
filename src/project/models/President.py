from datetime import date

from .Personne import Personne


class President(Personne):
    """Classe représentant le président d'une équipe, héritant de Personne.

    Attributes
    ----------
    surnom : str
        Surnom ou alias du président
    nombre_medailles : int
        Nombre de médailles sous sa présidence
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
        if not isinstance(nombre_medailles, int):
            raise TypeError("nombre_medailles doit être un int")

        self.__surnom = surnom
        self.__nombre_medailles = nombre_medailles

    def __str__(self) -> str:
        return f"Président: {self.prenom} {self.nom} ({self.__surnom})"

    def recuperer_info(self) -> str:
        """Retourne un résumé des informations du président.

        Returns
        -------
        str
            Résumé lisible
        """
        return (
            f"{self.prenom} {self.nom} | Président | "
            f"Médailles sous sa présidence: {self.__nombre_medailles}"
        )

    @property
    def surnom(self) -> str:
        """str: Surnom"""
        return self.__surnom

    @surnom.setter
    def surnom(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("surnom doit être un str")
        self.__surnom = valeur

    @property
    def nombre_medailles(self) -> int:
        """int: Nombre de médailles"""
        return self.__nombre_medailles

    @nombre_medailles.setter
    def nombre_medailles(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("nombre_medailles doit être un int")
        self.__nombre_medailles = valeur
