from abc import ABC, abstractmethod

from .noeudMatch import NoeudMatch


class PhaseTournoi(ABC):
    """Classe abstraite représentant une phase d'un tournoi.

    Attributes
    ----------
    graphe_matchs : list[NoeudMatch]
        Noeuds du graphe de matches
    format : str
        Format de la phase (poule,élimination directe...).
    """

    def __init__(
        self,
        format: str,
        graphe_matchs: list | None = None
    ):
        if not isinstance(format, str):
            raise TypeError("format doit être un str")
        self.__graphe_matchs: list = graphe_matchs if graphe_matchs is not None else []
        self.__format = format

    def __str__(self) -> str:
        return f"Phase ({self.__format}) - {len(self.__graphe_matchs)} match(es)"

    @abstractmethod
    def get_classement(self) -> dict:
        """Retourne le classement de cette phase.

        Returns
        -------
        dict
            Classement {place: equipe}.
        """

    @abstractmethod
    def creer_graphe_match(self) -> None:
        """Initialise la structure du graphe de matches"""

    @property
    def graphe_matchs(self) -> list:
        """list[NoeudMatch]: Graphe de matches"""
        return self.__graphe_matchs

    @graphe_matchs.setter
    def graphe_matchs(self, valeur: list):
        if not isinstance(valeur, list):
            raise TypeError("graphe_matchs doit être une list")
        self.__graphe_matchs = valeur

    @property
    def format(self) -> str:
        """str: Format de la phase"""
        return self.__format

    @format.setter
    def format(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("format doit être un str")
        self.__format = valeur

    def ajouter_match_de_base(self, liste_matchs: list) -> None:
        """Ajoute des matches initiaux sans parents au graphe.

        Parameters
        ----------
        liste_matchs : list
            Matches a ajouter comme noeuds racines
        """
        for i, match in enumerate(liste_matchs):
            noeud = NoeudMatch(numero_match=len(self.__graphe_matchs) + i, match=match)
            self.__graphe_matchs.append(noeud)

    def ajouter_match_vainqueur_de(self, liste_noeuds_parents: list) -> NoeudMatch:
        """Crée un match dont les participants sont les vainqueurs des parents.

        Parameters
        ----------
        liste_noeuds_parents : list[NoeudMatch]
            Noeuds dont les vainqueurs s'affrontent

        Returns
        -------
        NoeudMatch
            Nouveau noeud créé
        """
        nouveau = NoeudMatch(numero_match=len(self.__graphe_matchs))
        for parent in liste_noeuds_parents:
            nouveau.ajouter_parent(parent)
            parent.ajouter_enfant(nouveau)
        self.__graphe_matchs.append(nouveau)
        return nouveau

    def ajouter_match_perdants_de(self, liste_noeuds_parents: list) -> NoeudMatch:
        """Crée un match dont les participants sont les perdants des parents.

        Parameters
        ----------
        liste_noeuds_parents : list[NoeudMatch]
            Noeuds dont les perdants s'affrontent

        Returns
        -------
        NoeudMatch
            Nouveau noeud créé
        """
        nouveau = NoeudMatch(numero_match=len(self.__graphe_matchs))
        for parent in liste_noeuds_parents:
            nouveau.ajouter_parent(parent)
            parent.ajouter_enfant(nouveau)
        self.__graphe_matchs.append(nouveau)
        return nouveau
