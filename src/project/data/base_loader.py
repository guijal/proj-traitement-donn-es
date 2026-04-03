import csv
from datetime import datetime
from abc import ABC, abstractmethod
from pathlib import Path

from .database import Database


class BaseLoader(ABC):
    """Classe de base fournissant les outils nécessaires à tous les loaders spécifiques."""

    def __init__(self, data_directory: str, db: Database):
        self.data_directory = data_directory
        self.db = db

    @abstractmethod
    def charger_tout(self) -> None:
        """Chaque sous-classe devra implémenter l'orchestration de ses propres fichiers."""
        pass

    def _lire_csv(self, nom_fichier: str) -> list[dict]:
        """Méthode utilitaire pour lire un CSV et retourner une liste de dictionnaires."""
        chemin_complet = Path(self.data_directory) / nom_fichier
        with open(chemin_complet, mode="r", encoding="utf-8") as fichier:
            return list(csv.DictReader(fichier))

    @staticmethod
    def _parser_date(date_str: str):
        if not date_str:
            return None
        return datetime.strptime(date_str, "%Y-%m-%d").date()
