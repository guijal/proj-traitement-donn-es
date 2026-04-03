from datetime import date


class Medaille:
    """Classe représentant une médaille sportive.

    Attributes
    ----------
    id_medaille : int
        Identifiant unique
    type_medaille : str
        Type : or, argent ou bronze
    date : date
        Date de remise de la médaille
    """

    TYPES_VALIDES = {"or", "argent", "bronze"}

    def __init__(self, id_medaille: int, type_medaille: str, date_remise: date):
        if not isinstance(id_medaille, int):
            raise TypeError("id_medaille doit être un int")
        if not isinstance(type_medaille, str):
            raise TypeError("type_medaille doit être un str")
        if type_medaille not in self.TYPES_VALIDES:
            raise ValueError(
                f"type_medaille invalide. Valeurs accept2es : {self.TYPES_VALIDES}"
            )
        if not isinstance(date_remise, date):
            raise TypeError("date_remise doit être un datetime.date")
        self.__id_medaille = id_medaille
        self.__type_medaille = type_medaille
        self.__date = date_remise

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Medaille):
            return self.__id_medaille == other.id_medaille
        return NotImplemented

    def __hash__(self) -> int:
        return hash(self.__id_medaille)

    def __str__(self) -> str:
        return f"Médaille {self.__type_medaille} - {self.__date}"

    @property
    def id_medaille(self) -> int:
        """int: Identifiant"""
        return self.__id_medaille

    @id_medaille.setter
    def id_medaille(self, valeur: int):
        if not isinstance(valeur, int):
            raise TypeError("id_medaille doit être un int")
        self.__id_medaille = valeur

    @property
    def type_medaille(self) -> str:
        """str: Type de medaille"""
        return self.__type_medaille

    @type_medaille.setter
    def type_medaille(self, valeur: str):
        if valeur not in self.TYPES_VALIDES:
            raise ValueError(
                f"type_medaille invalide. Valeurs acceptées : {self.TYPES_VALIDES}"
            )
        self.__type_medaille = valeur

    @property
    def date(self) -> date:
        """date: Date de remise de la médaille"""
        return self.__date

    @date.setter
    def date(self, valeur: date):
        if not isinstance(valeur, date):
            raise TypeError("date doit être un datetime.date")
        self.__date = valeur
