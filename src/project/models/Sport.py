class Sport:
    """Classe représentant un sport.

    Attributes
    ----------
    nom: str
        Nom du sport
    numero: int
        Identifiant numérique du sport
    nb_joueurs_par_equipe: int
        Nombre de joueurs par équipe
    nb_equipes: int
        Nombre d'équipes
    """

    def __init__(
        self,
        nom: str,
        numero: int,
        nb_joueurs_par_equipe: int,
        nb_equipes: int,
    ):
        if not isinstance(nom, str):
            raise TypeError("nom doit être un str")
        if not isinstance(numero, int):
            raise TypeError("numero doit être un int")
        if not isinstance(nb_joueurs_par_equipe, int):
            raise TypeError("nb_joueurs_par_equipe doit être un int")
        if not isinstance(nb_equipes, int):
            raise TypeError("nb_equipes doit être un int")

        self.__nom = nom
        self.__numero = numero
        self.__nb_joueurs_par_equipe = nb_joueurs_par_equipe
        self.__nb_equipes = nb_equipes

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Sport):
            return self.__numero == other.numero
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__numero)

    def __str__(self):
        return (
            f"Sport: {self.__nom} (n°{self.__numero}) - "
            f"{self.__nb_equipes} équipes de {self.__nb_joueurs_par_equipe} joueurs"
        )

    @property
    def nom(self) -> str:
        """str: Nom du sport"""
        return self.__nom

    @nom.setter
    def nom(self, valeur: str):
        if not isinstance(valeur, str):
            raise TypeError("nom doit être un str")
        self.__nom = valeur

    @property
    def numero(self) -> int:
        """int: Identifiant numerique du sport"""
        return self.__numero

    @numero.setter
    def numero(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("numero doit être un int")
        self.__numero = valeur

    @property
    def nb_joueurs_par_equipe(self) -> int:
        """int: Nombre de joueurs par équipe"""
        return self.__nb_joueurs_par_equipe

    @nb_joueurs_par_equipe.setter
    def nb_joueurs_par_equipe(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("nb_joueurs_par_equipe doit être un int")
        self.__nb_joueurs_par_equipe = valeur

    @property
    def nb_equipes(self) -> int:
        """int: Nombre d'équipes"""
        return self.__nb_equipes

    @nb_equipes.setter
    def nb_equipes(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("nb_equipes doit être un int")
        self.__nb_equipes = valeur
