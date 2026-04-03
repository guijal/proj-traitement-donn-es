from abc import ABC, abstractmethod

from .sport import Sport
from .medaille import Medaille


class Tournoi(ABC):
    """Classe abstraite représentant un tournoi sportif.

    Attributes
    ----------
    sport : Sport
        Sport du tournoi
    categorie : str
        Catégorie (ex: seniors, U21)
    medaille_or : Medaille | None
        Médaille d'or attribuée
    medaille_argent : Medaille | None
        Médaille d'argent attribuée
    medaille_bronze : Medaille | None
        Médaille de bronze attribuée
    liste_phases : list
        Phases du tournoi dans l'ordre
    """

    def __init__(
        self,
        sport: Sport,
        categorie: str,
        medaille_or=None,
        medaille_argent=None,
        medaille_bronze=None,
    ):
        if not isinstance(sport, Sport):
            raise TypeError("sport doit être un Sport")
        if not isinstance(categorie, str):
            raise TypeError("categorie doit être un str")
        self.__sport = sport
        self.__categorie = categorie
        self.__medaille_or = medaille_or
        self.__medaille_argent = medaille_argent
        self.__medaille_bronze = medaille_bronze
        self.__liste_phases: list = []

    def __str__(self) -> str:
        return f"Tournoi {self.__sport.nom} - {self.__categorie}"

    @abstractmethod
    def get_classement(self) -> dict:
        """Retourne le classement final du tournoi.

        Returns
        -------
        dict
            Classement {place: equipe}.
        """

    @abstractmethod
    def ajouter_phase(self, phase) -> None:
        """Ajoute une phase au tournoi.

        Parameters
        ----------
        phase : PhaseTournoi
            Phase à ajouter
        """

    @property
    def sport(self) -> Sport:
        """Sport: Sport du tournoi"""
        return self.__sport

    @sport.setter
    def sport(self, valeur: Sport):
        if not isinstance(valeur, Sport):
            raise TypeError("sport doit être un Sport")
        self.__sport = valeur

    @property
    def categorie(self) -> str:
        """str: Categorie"""
        return self.__categorie

    @categorie.setter
    def categorie(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("categorie doit être un str")
        self.__categorie = valeur

    @property
    def medaille_or(self) -> Medaille | None:
        """Medaille | None: Médaille d'or"""
        return self.__medaille_or

    @medaille_or.setter
    def medaille_or(self, valeur):
        self.__medaille_or = valeur

    @property
    def medaille_argent(self) -> Medaille | None:
        """Medaille | None: Médaille d'argent"""
        return self.__medaille_argent

    @medaille_argent.setter
    def medaille_argent(self, valeur):
        self.__medaille_argent = valeur

    @property
    def medaille_bronze(self) -> Medaille | None:
        """Medaille | None: Médaille de bronze"""
        return self.__medaille_bronze

    @medaille_bronze.setter
    def medaille_bronze(self, valeur):
        self.__medaille_bronze = valeur

    @property
    def liste_phases(self) -> list:
        """list: Phases du tournoi"""
        return self.__liste_phases
