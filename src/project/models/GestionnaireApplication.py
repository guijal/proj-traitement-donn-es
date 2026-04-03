from .Competition import Competition
from .Sport import Sport


class GestionnaireApplication:
    """Gestionnaire central de l'application de résultats sportifs.

    Attributes
    ----------
    liste_competitions : list[Competition]
        Toutes les compétitions enregistrées.
    """

    def __init__(
        self,
        liste_competitions: list | None = None
    ):
        self.__liste_competitions: list = (
            liste_competitions if liste_competitions is not None else []
        )

    def __str__(self) -> str:
        return (
            f"GestionnaireApplication - "
            f"{len(self.__liste_competitions)} compétition(s) enregistrée(s)"
        )

    @property
    def liste_competitions(self) -> list:
        """list[Competition]: Compétitions enregistrées"""
        return self.__liste_competitions

    def ajouter_competition(self, competition: Competition) -> None:
        """Ajoute une compétition à l'application.

        Parameters
        ----------
        competition : Competition
            Compétition à ajouter

        Raises
        ------
        TypeError
            Si l'argument n'est pas une Competition
        ValueError
            Si la competition est déjà enregistrée
        """
        if not isinstance(competition, Competition):
            raise TypeError("competition doit être une Competition")
        if competition in self.__liste_competitions:
            raise ValueError("Cette  competition est déjà enregistrée")
        self.__liste_competitions.append(competition)

    def supprimer_competition(self, competition: Competition) -> None:
        """Supprime une compétition.

        Parameters
        ----------
        competition : Competition
            Compétition à supprimer

        Raises
        ------
        ValueError
            Si la compétition n'est pas dans la liste
        """
        if competition not in self.__liste_competitions:
            raise ValueError("Cette compétition n'est pas enregistrée")
        self.__liste_competitions.remove(competition)

    def get_competitions_par_sport(self, sport: Sport) -> list:
        """Retourne les compétitions d'un sport donné.

        Parameters
        ----------
        sport : Sport
            Sport à filtrer

        Returns
        -------
        list[Competition]
            Compétitions correspondant au sport
        """
        if not isinstance(sport, Sport):
            raise TypeError("sport doit être un Sport")
        return [
            c
            for c in self.__liste_competitions
            if any(t.sport == sport for t in c.liste_tournois)
        ]

    def resumer_competitions(self) -> str:
        """Retourne un résumé de toutes les compétitions.

        Returns
        -------
        str
            Résumé lisible de chaque compétition
        """
        if not self.__liste_competitions:
            return "Aucune compétition enregistrée"
        return "\n".join(c.recuperer_info() for c in self.__liste_competitions)
