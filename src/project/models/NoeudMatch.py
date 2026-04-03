from __future__ import annotations
# permet de gérer l'appel récursif du type NoeudMatch dans les annotations


class NoeudMatch:
    """Noeud du graphe de matches d'une phase de tournoi.

    Attributes
    ----------
    match : object | None
        Match associé à ce noeud
    numero_match : int
        Numéro d'ordre dans la phase
    liste_parents : list[NoeudMatch]
        Noeuds parents (matches précédents)
    liste_enfants : list[NoeudMatch]
        Noeuds enfants (matches suivants)
    """

    def __init__(
        self,
        numero_match: int,
        match=None,
        liste_parents: list | None = None,
        liste_enfants: list | None = None,
    ):
        if not isinstance(numero_match, int):
            raise TypeError("numero_match doit être un int")
        self.__match = match
        self.__numero_match = numero_match
        self.__liste_parents: list = liste_parents if liste_parents is not None else []
        self.__liste_enfants: list = liste_enfants if liste_enfants is not None else []

    def __hash__(self) -> int:
        return hash(self.__numero_match)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, NoeudMatch):
            return self.__numero_match == other.numero_match
        return NotImplemented

    def __str__(self) -> str:
        match_str = str(self.__match) if self.__match else "Match non défini"
        return f"NoeudMatch n°{self.__numero_match} - {match_str}"

    @property
    def match(self):
        """object | None: Match associé"""
        return self.__match

    @match.setter
    def match(self, valeur):
        self.__match = valeur

    @property
    def numero_match(self) -> int:
        """int: Numéro du match"""
        return self.__numero_match

    @numero_match.setter
    def numero_match(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("numero_match doit être un int")
        self.__numero_match = valeur

    @property
    def liste_parents(self) -> list:
        """list[NoeudMatch]: Noeuds parents"""
        return self.__liste_parents

    @property
    def liste_enfants(self) -> list:
        """list[NoeudMatch]: Noeuds enfants"""
        return self.__liste_enfants

    def ajouter_parent(self, noeud: NoeudMatch) -> None:
        """Ajoute un noeud parent.

        Parameters
        ----------
        noeud : NoeudMatch
            Noeud parent à ajouter
        """
        if not isinstance(noeud, NoeudMatch):
            raise TypeError("noeud doit être un NoeudMatch")
        if noeud not in self.__liste_parents:
            self.__liste_parents.append(noeud)

    def supprimer_parent(self, noeud: NoeudMatch) -> None:
        """Supprime un noeud parent.

        Parameters
        ----------
        noeud : NoeudMatch
            Noeud parent à supprimer

        Raises
        ------
        ValueError
            Si le noeud n'est pas dans la liste des parents
        """
        if noeud not in self.__liste_parents:
            raise ValueError("Ce noeud n'est pas dans la liste des parents")
        self.__liste_parents.remove(noeud)

    def ajouter_enfant(self, noeud: NoeudMatch) -> None:
        """Ajoute un noeud enfant.

        Parameters
        ----------
        noeud : NoeudMatch
            Noeud enfant à ajouter
        """
        if not isinstance(noeud, NoeudMatch):
            raise TypeError("noeud doit être un NoeudMatch")
        if noeud not in self.__liste_enfants:
            self.__liste_enfants.append(noeud)

    def supprimer_enfant(self, noeud: NoeudMatch) -> None:
        """Supprime un noeud enfant.

        Parameters
        ----------
        noeud : NoeudMatch
            Noeud enfant à supprimer

        Raises
        ------
        ValueError
            Si le noeud n'est pas dans la liste des enfants
        """
        if noeud not in self.__liste_enfants:
            raise ValueError("Ce noeud n'est pas dans la liste des enfants")
        self.__liste_enfants.remove(noeud)
