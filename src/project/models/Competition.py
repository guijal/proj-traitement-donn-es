from datetime import date

from .Tournoi import Tournoi
from .Sport import Sport


class Competition:
    """Classe représentant une compétition sportive regroupant des tournois.

    Attributes
    ----------
    id_competition : int
        Identifiant unique
    nom : str
        Nom de la compétition
    edition : str
        Edition (ex: 2023-2024)
    organisateur : str
        Nom de l'organisateur
    date_debut : date
        Date de début
    date_fin : date
        Date de fin
    liste_tournois : list[Tournoi]
        Tournois composant la compétition
    """

    def __init__(
        self,
        id_competition: int,
        nom: str | None = None,
        edition: str | None = None,
        organisateur: str | None = None,
        date_debut: date | None = None,
        date_fin: date | None = None,
        liste_tournois: list | None = None,
        id_csv: int | None = None,
    ):
        if not isinstance(id_competition, int):
            raise TypeError("id_competition doit être un int")
        if nom is not None and not isinstance(nom, str):
            raise TypeError("nom doit être un str")
        if edition is not None and not isinstance(edition, str):
            raise TypeError("edition doit être un str")
        if organisateur is not None and not isinstance(organisateur, str):
            raise TypeError("organisateur doit être un str")
        if date_debut is not None and not isinstance(date_debut, date):
            raise TypeError("date_debut doit être un datetime.date")
        if date_fin is not None and not isinstance(date_fin, date):
            raise TypeError("date_fin doit être un datetime.date")
        if date_fin is not None and date_debut is not None and date_fin < date_debut:
            raise ValueError("date_fin doit être posterieure a date_debut")
        self.__id_competition = id_competition
        self.__nom = nom
        self.__edition = edition
        self.__organisateur = organisateur
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__liste_tournois: list = (
            liste_tournois if liste_tournois is not None else []
        )
        self.__id_csv = id_csv

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Competition):
            return self.__id_competition == other.id_competition
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__id_competition)

    def __str__(self) -> str:
        return (
            f"{self.__nom} - Edition {self.__edition} "
            f"({self.__date_debut} -> {self.__date_fin})"
        )

    @property
    def id_competition(self) -> int:
        """int: Identifiant"""
        return self.__id_competition

    @id_competition.setter
    def id_competition(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("id_competition doit être un int")
        self.__id_competition = valeur

    @property
    def nom(self) -> str | None:
        """str | None: Nom de la compétition"""
        return self.__nom

    @nom.setter
    def nom(self, valeur: str | None):
        if valeur is not None and not isinstance(valeur, str):
            raise TypeError("nom doit être un str")
        self.__nom = valeur

    @property
    def edition(self) -> str | None:
        """str | None: Edition"""
        return self.__edition

    @edition.setter
    def edition(self, valeur: str | None):
        if valeur is not None and not isinstance(valeur, str):
            raise TypeError("edition doit être un str")
        self.__edition = valeur

    @property
    def organisateur(self) -> str | None:
        """str | None: Organisateur"""
        return self.__organisateur

    @organisateur.setter
    def organisateur(self, valeur: str | None):
        if valeur is not None and not isinstance(valeur, str):
            raise TypeError("organisateur doit être un str")
        self.__organisateur = valeur

    @property
    def date_debut(self) -> date | None:
        """date | None: Date de début"""
        return self.__date_debut

    @date_debut.setter
    def date_debut(self, valeur: date | None):
        if valeur is not None and not isinstance(valeur, date):
            raise TypeError("date_debut doit être un datetime.date")
        self.__date_debut = valeur

    @property
    def date_fin(self) -> date | None:
        """date | None: Date de fin"""
        return self.__date_fin

    @date_fin.setter
    def date_fin(self, valeur: date | None):
        if valeur is not None and not isinstance(valeur, date):
            raise TypeError("date_fin doit être un datetime.date")
        self.__date_fin = valeur

    @property
    def liste_tournois(self) -> list:
        """list[Tournoi]: Tournois de la compétition"""
        return self.__liste_tournois

    def ajouter_tournoi(self, tournoi: Tournoi) -> None:
        """Ajoute un tournoi à la compétition.

        Parameters
        ----------
        tournoi : Tournoi
            Tournoi à ajouter

        Raises
        ------
        TypeError
            Si l'argument n'est pas un Tournoi
        ValueError
            Si le tournoi est déjà dans la compétition
        """
        if not isinstance(tournoi, Tournoi):
            raise TypeError("tournoi doit être un Tournoi")
        if tournoi in self.__liste_tournois:
            raise ValueError("Ce tournoi est déjà dans la compétition")
        self.__liste_tournois.append(tournoi)

    def get_tournois_par_sport(self, sport: Sport) -> list:
        """Retourne les tournois d'un sport donné

        Parameters
        ----------
        sport : Sport
            Sport à filtrer

        Returns
        -------
        list[Tournoi]
            Tournois correspondant au sport
        """
        if not isinstance(sport, Sport):
            raise TypeError("sport doit être un Sport")
        return [t for t in self.__liste_tournois if t.sport == sport]

    def recuperer_info(self) -> str:
        """Retourne un résumé de la compétition

        Returns
        -------
        str
            Résumé lisible
        """
        return (
            f"{self.__nom} | Edition: {self.__edition} | "
            f"Organisateur: {self.__organisateur} | "
            f"{len(self.__liste_tournois)} tournoi(s) | "
            f"{self.__date_debut} -> {self.__date_fin}"
        )
