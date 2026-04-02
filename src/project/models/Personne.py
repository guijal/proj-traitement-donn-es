from abc import ABC, abstractmethod


class Personne(ABC):
    """

    Simule une personne

    Attributes
    -----------
    id_personne
        int
    sex
        str
    nom
        str
    prenom
        str
    date_naissance
        tuple[int]
    nationalite
        str
    taille
        int (en cm)
    poids
        int  (en kg)
    statut
        dict[tuple[int], str]
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
    ):
        if not (
            isinstance(id_personne, int)
            and isinstance(sex, str)
            and isinstance(nom, str)
            and isinstance(prenom, str)
            and isinstance(date_naissance, tuple)
            and isinstance(nationalite, str)
            and isinstance(taille, int)
            and isinstance(poids, int)
        ):
            raise TypeError("mauvais type")

        self.__id_personne = id_personne
        self.__sex = sex
        self.__nom = nom
        self.__prenom = prenom
        self.__date_naissance = date_naissance
        self.__nationalite = nationalite
        self.__taille = taille
        self.__poids = poids
        self.__statut = dict()

    def __eq__(self, value):
        return self.id_personne == value.id_personne

    @property
    def id_personne(self):
        return self.__id_personne

    @id_personne.setter
    def id_personne(self, nouveau_id: int):
        assert isinstance(nouveau_id, int)
        self.__id_personne = nouveau_id

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, nouveau_sex: str):
        assert isinstance(nouveau_sex, str)
        self.__sex = nouveau_sex

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, nouveau_nom: str):
        assert isinstance(nouveau_nom, str)
        self.__nom = nouveau_nom

    @property
    def prenom(self):
        return self.__prenom

    @prenom.setter
    def prenom(self, nouveau_prenom: str):
        assert isinstance(nouveau_prenom, str)
        self.__prenom = nouveau_prenom

    @property
    def date_naissance(self):
        return self.__date_naissance

    @date_naissance.setter
    def date_naissance(self, nouvelle_date: tuple[int]):
        assert isinstance(nouvelle_date, tuple)
        self.__date_naissance = nouvelle_date

    @property
    def nationalite(self):
        return self.__nationalite

    @nationalite.setter
    def nationalite(self, nouvelle_nationalite: str):
        assert isinstance(nouvelle_nationalite, str)
        self.__nationalite = nouvelle_nationalite

    @property
    def taille(self):
        return self.__taille

    @taille.setter
    def taille(self, nouvelle_taille: int):
        assert isinstance(nouvelle_taille, int)
        self.__taille = nouvelle_taille

    @property
    def poids(self):
        return self.__poids

    @poids.setter
    def poids(self, nouveau_poids: int):
        assert isinstance(nouveau_poids, int)
        self.__poids = nouveau_poids

    @property
    def statut(self):
        return self.__statut

    def ajouter_statut(self, date: tuple[int], description: str):
        if not (isinstance(date, tuple) and isinstance(description, str)):
            raise TypeError(
                "Les arguments 'date' et 'description' doivent être respectivement un tuple et une chaîne de caractères."
            )
        self.__statut[date] = description
