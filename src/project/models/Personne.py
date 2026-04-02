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
        self.__id_personne = id_personne
        self.__sex = sex
        self.__nom = nom
        self.__prenom = prenom
        self.__date_naissance = date_naissance
        self.__nationalite = nationalite
        self.__taille = taille
        self.__poids = poids

    def 