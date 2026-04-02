class Sport:
    """
    Classe Sport

    Attributes
    ----------
    nom: str
        Nom du sport
    numero: int
        Numero du sport
    nb_joueurs_par_equipe: int
        Nombre de joueurs par equipe
    nb_equipes: int
        Nombre d'equipes

    Method
    ------

    """

    def __init__(
        self, nom: str, numero: int, nb_joueurs_par_equipe: int, nb_equipes: int
    ):
        self.__nom = nom
        self.__numero = numero
        self.__nb_joueurs_par_equipe = nb_joueurs_par_equipe
        self.__nb_equipes = nb_equipes

    def __str__(self):
        return f"""
        Nom du sport: {self.__nom}

        Numero du sport: {self.__numero} 
        Nombre de joueurs par equipe: {self.__nb_joueurs_par_equipe}
        Nombre d'equipes: {self.__nb_equipes}
        """

    #test 3

    # getter 
    @property
    def nom(self):
        return self.__nom

    @property
    def numero(self):
        return self.__numero

    @property
    def joueurs_par_equipe(self):
        return self.__nb_joueurs_par_equipe

    @property
    def equipes(self):
        return self.__nb_equipes
    
    # setter
    def set_nom(self, nom: str):
        self.__nom = nom

    def set_numero(self, numero: int):
        self.__numero = numero   

    def set_nb_joueurs_par_equipe(self, nb_joueurs_par_equipe: int):
        self.__nb_joueurs_par_equipe = nb_joueurs_par_equipe

    def set_nb_equipes(self, nb_equipes: int):
        self.__nb_equipes = nb_equipes

    
           

