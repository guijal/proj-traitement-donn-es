from datetime import date

class Medaille:
    def __init__(self, id_medaille: int, type_medaille: str, date: date):
        self.__id_medaille = id_medaille
        self.__type_medaille = type_medaille
        self.__date = date

    def get_id_medaille(self):
        return self.__id_medaille

    def get_type_medaille(self):
        return self.__type_medaille

    def get_date(self):
        return self.__date