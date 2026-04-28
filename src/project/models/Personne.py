from abc import ABC
from datetime import date


class Personne(ABC):
    """Classe abstraite représentant une personne.

    Attributes
    -----------
    id_personne : int
        Identifiant unique
    sex : str
        Sexe
    nom : str
        Nom de famille
    prenom : str
        Prenom
    date_naissance : date
        Date de naissance
    nationalite : str
        Code nationalité (ex: FRA)
    pays : str | None
        Pays de la personne
    taille : float | None
        Taille en cm
    poids : float | None
        Poids en kg
    statut : dict[date, str]
        Historique des statuts
    """

    def __init__(
        self,
        id_personne: int,
        nom: str,
        prenom: str,
        sex: str | None = None,
        date_naissance: date | None = None,
        nationalite: str | None = None,
        pays: str | None = None,
        taille: float | None = None,
        poids: float | None = None,
        id_csv: int | None = None,
    ):
        if not isinstance(id_personne, int):
            raise TypeError("id_personne doit être un int")
        if sex is not None and not isinstance(sex, str):
            raise TypeError("sex doit être un str")
        if not isinstance(nom, str):
            raise TypeError("nom doit être un str")
        if not isinstance(prenom, str):
            raise TypeError("prenom doit être un str")
        if date_naissance is not None and not isinstance(date_naissance, date):
            raise TypeError("date_naissance doit être un datetime.date")
        if nationalite is not None and not isinstance(nationalite, str):
            raise TypeError("nationalite doit être un str")
        if pays is not None and not isinstance(pays, str):
            raise TypeError("pays doit être un str")
        if taille is not None and not isinstance(taille, float):
            raise TypeError("taille doit être un float")
        if poids is not None and not isinstance(poids, float):
            raise TypeError("poids doit être un float")

        self.__id_personne = id_personne
        self.__sex = sex
        self.__nom = nom
        self.__prenom = prenom
        self.__date_naissance = date_naissance
        self.__nationalite = nationalite
        self.__pays = pays
        self.__taille = float(taille) if taille is not None else None
        self.__poids = float(poids) if poids is not None else None
        self.__statut: dict = {}
        self.__id_csv = id_csv

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Personne):
            return self.__id_personne == other.id_personne
        return NotImplemented

    def __str__(self) -> str:
        return f"{self.__prenom} {self.__nom} ({self.__nationalite})"

    @property
    def id_personne(self) -> int:
        """int: Identifiant unique"""
        return self.__id_personne

    @id_personne.setter
    def id_personne(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("id_personne doit etre un int.")
        self.__id_personne = valeur

    @property
    def sex(self) -> str | None:
        """str | None: Sexe"""
        return self.__sex

    @sex.setter
    def sex(self, valeur: str | None):
        if valeur is not None and not isinstance(valeur, str):
            raise TypeError("sex doit etre un str")
        self.__sex = valeur

    @property
    def nom(self) -> str:
        """str: Nom de famille"""
        return self.__nom

    @nom.setter
    def nom(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("nom doit etre un str")
        self.__nom = valeur

    @property
    def prenom(self) -> str:
        """str: Prenom"""
        return self.__prenom

    @prenom.setter
    def prenom(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("prenom doit etre un str")
        self.__prenom = valeur

    @property
    def date_naissance(self) -> date | None:
        """date | None: Date de naissance"""
        return self.__date_naissance

    @date_naissance.setter
    def date_naissance(self, valeur: date | None):
        if valeur is not None and not isinstance(valeur, date):
            raise TypeError("date_naissance doit être un datetime.date")
        self.__date_naissance = valeur

    @property
    def nationalite(self) -> str | None:
        """str | None: Code nationalité"""
        return self.__nationalite

    @nationalite.setter
    def nationalite(self, valeur: str | None):
        if valeur is not None and not isinstance(valeur, str):
            raise TypeError("nationalite doit être un str")
        self.__nationalite = valeur

    @property
    def pays(self) -> str | None:
        """str | None: Pays de la personne"""
        return self.__pays

    @pays.setter
    def pays(self, valeur: str | None):
        if valeur is not None and not isinstance(valeur, str):
            raise TypeError("pays doit être un str")
        self.__pays = valeur

    @property
    def taille(self) -> float | None:
        """float | None: Taille en cm"""
        return self.__taille

    @taille.setter
    def taille(self, valeur: float | None):
        if valeur is not None and not isinstance(valeur, (int, float)):
            raise TypeError("taille doit être un int ou float")
        self.__taille = float(valeur) if valeur is not None else None

    @property
    def poids(self) -> float | None:
        """float | None: Poids en kg"""
        return self.__poids

    @poids.setter
    def poids(self, valeur: float | None):
        if valeur is not None and not isinstance(valeur, (int, float)):
            raise TypeError("poids doit être un int ou float.")
        self.__poids = float(valeur) if valeur is not None else None

    @property
    def statut(self) -> dict:
        """dict[date, str]: Historique des statuts"""
        return self.__statut

    def ajouter_statut(self, d: date, description: str) -> None:
        """Ajoute une entrée dans l'historique des statuts.

        Parameters
        ----------
        d : date
            Date du changement de statut
        description : str
            Nouveau statut : actif, blessé, suspendu, retraité

        Raises
        ------
        TypeError
            Si les types ne correspondent pas
        ValueError
            Si la description n'est pas un statut valide
        """
        statuts_valides = {"actif", "blessé", "suspendu", "retraité"}
        if not isinstance(d, date):
            raise TypeError("d doit être un datetime.date")
        if not isinstance(description, str):
            raise TypeError("description doit être un str")
        if description not in statuts_valides:
            raise ValueError(f"Statut invalide. Valeurs acceptées : {statuts_valides}")
        self.__statut[d] = description

    @property
    def id_csv(self) -> int | None:
        return self.__id_csv

    @id_csv.setter
    def id_csv(self, valeur: int | None):
        self.__id_csv = valeur
