from .sport import Sport


class Equipe:
    """Classe représentant une équipe sportive.

    Attributes
    ----------
    id_equipe : int
        Identifiant unique
    nom_officiel : str
        Nom officiel
    nom_abrege : str
        Abréviation (ex: PSG)
    ville : str
        Ville
    pays : str
        Pays
    code_pays : str
        Code ISO pays
    genre : str
        Genre : masculin, féminin, mixte
    discipline : Sport
        Sport pratiqué
    annee_fondation : int
        Année de fondation
    nb_medailles : int
        Nombre total de medailles
    president : object | None
        Président de l'équipe
    liste_joueurs : list
        Liste des joueurs
    liste_coachs : list
        Liste des entraîneurs
    """

    GENRES_VALIDES = {"masculin", "féminin", "mixte"}

    def __init__(
        self,
        id_equipe: int,
        nom_officiel: str,
        nom_abrege: str,
        ville: str,
        pays: str,
        code_pays: str,
        genre: str,
        discipline: Sport,
        annee_fondation: int,
        nb_medailles: int = 0,
        president=None,
        liste_joueurs: list | None = None,
        liste_coachs: list | None = None,
    ):
        if not isinstance(id_equipe, int):
            raise TypeError("id_equipe doit être un int")
        if not isinstance(nom_officiel, str):
            raise TypeError("nom_officiel doit être un str")
        if not isinstance(nom_abrege, str):
            raise TypeError("nom_abrege doit être un str")
        if not isinstance(ville, str):
            raise TypeError("ville doit être un str")
        if not isinstance(pays, str):
            raise TypeError("pays doit être un str")
        if not isinstance(code_pays, str):
            raise TypeError("code_pays doit être un str")
        if not isinstance(genre, str):
            raise TypeError("genre doit être un str")
        if genre not in self.GENRES_VALIDES:
            raise ValueError(
                f"genre invalide. Valeurs acceptées : {self.GENRES_VALIDES}"
            )
        if not isinstance(discipline, Sport):
            raise TypeError("discipline doit être un Sport")
        if not isinstance(annee_fondation, int):
            raise TypeError("annee_fondation doit être un int")
        if not isinstance(nb_medailles, int):
            raise TypeError("nb_medailles doit être un int")

        self.__id_equipe = id_equipe
        self.__nom_officiel = nom_officiel
        self.__nom_abrege = nom_abrege
        self.__ville = ville
        self.__pays = pays
        self.__code_pays = code_pays
        self.__genre = genre
        self.__discipline = discipline
        self.__president = president
        self.__liste_joueurs: list = liste_joueurs if liste_joueurs is not None else []
        self.__liste_coachs: list = liste_coachs if liste_coachs is not None else []
        self.__annee_fondation = annee_fondation
        self.__nb_medailles = nb_medailles

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Equipe):
            return self.__id_equipe == other.id_equipe
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__id_equipe)

    def __str__(self) -> str:
        return f"{self.__nom_officiel} ({self.__nom_abrege}) - {self.__ville}, {self.__pays}"

    @property
    def id_equipe(self) -> int:
        """int: Identifiant"""
        return self.__id_equipe

    @id_equipe.setter
    def id_equipe(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("id_equipe doit être un int")
        self.__id_equipe = valeur

    @property
    def nom_officiel(self) -> str:
        """str: Nom officiel"""
        return self.__nom_officiel

    @nom_officiel.setter
    def nom_officiel(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("nom_officiel doit être un str")
        self.__nom_officiel = valeur

    @property
    def nom_abrege(self) -> str:
        """str: Abréviation"""
        return self.__nom_abrege

    @nom_abrege.setter
    def nom_abrege(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("nom_abrege doit être un str")
        self.__nom_abrege = valeur

    @property
    def ville(self) -> str:
        """str: Ville"""
        return self.__ville

    @ville.setter
    def ville(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("ville doit être un str")
        self.__ville = valeur

    @property
    def pays(self) -> str:
        """str: Pays"""
        return self.__pays

    @pays.setter
    def pays(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("pays doit être un str")
        self.__pays = valeur

    @property
    def code_pays(self) -> str:
        """str: Code ISO pays"""
        return self.__code_pays

    @code_pays.setter
    def code_pays(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("code_pays doit être un str")
        self.__code_pays = valeur

    @property
    def genre(self) -> str:
        """str: Genre de l'équipe"""
        return self.__genre

    @genre.setter
    def genre(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("genre doit être un str")
        if valeur not in self.GENRES_VALIDES:
            raise ValueError(
                f"genre invalide. Valeurs acceptées : {self.GENRES_VALIDES}"
            )
        self.__genre = valeur

    @property
    def discipline(self) -> Sport:
        """Sport: Discipline pratiquée"""
        return self.__discipline

    @discipline.setter
    def discipline(self, valeur: Sport):
        if not isinstance(valeur, Sport):
            raise TypeError("discipline doit être un Sport")
        self.__discipline = valeur

    @property
    def president(self):
        """object | None: Président"""
        return self.__president

    @president.setter
    def president(self, valeur):
        self.__president = valeur

    @property
    def liste_joueurs(self) -> list:
        """list: Joueurs"""
        return self.__liste_joueurs

    @property
    def liste_coachs(self) -> list:
        """list: Coachs"""
        return self.__liste_coachs

    @property
    def annee_fondation(self) -> int:
        """int: Année de fondation"""
        return self.__annee_fondation

    @annee_fondation.setter
    def annee_fondation(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("annee_fondation doit être un int")
        self.__annee_fondation = valeur

    @property
    def nb_medailles(self) -> int:
        """int: Nombre de médailles"""
        return self.__nb_medailles

    @nb_medailles.setter
    def nb_medailles(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("nb_medailles doit être un int")
        self.__nb_medailles = valeur

    def ajouter_joueur(self, joueur) -> None:
        """Ajoute un joueur à la liste.

        Parameters
        ----------
        joueur : Competiteur
            Joueur à ajouter
        """
        self.__liste_joueurs.append(joueur)

    def retirer_joueur(self, joueur) -> None:
        """Retire un joueur de la liste.

        Parameters
        ----------
        joueur : Competiteur
            Joueur à retirer

        Raises
        ------
        ValueError
            Si le joueur n'est pas dans l'equipe.
        """
        if joueur not in self.__liste_joueurs:
            raise ValueError("Ce joueur n'est pas dans l'équipe")
        self.__liste_joueurs.remove(joueur)

    def ajouter_coach(self, coach) -> None:
        """Ajoute un entraîneur à la liste.

        Parameters
        ----------
        coach : Coach
            Coach à ajouter
        """
        self.__liste_coachs.append(coach)
