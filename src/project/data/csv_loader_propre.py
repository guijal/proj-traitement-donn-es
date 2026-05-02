import ast
from datetime import datetime
from .database import Database
from .base_loader import BaseLoader
from ..models.Equipe import Equipe
from ..models.Sport import Sport
from ..models.Competiteur import Competiteur
from ..models.Match import Match
from ..models.Competition import Competition
from ..models.Arbitre import Arbitre
from ..models.Coach import Coach


class CSVLoader(BaseLoader):
    """Classe permettant de charger tous les CSV

    Pour chaque jeu de donnée, on créera une sous classe à partir de la classe BaseLoader pour importer les données.
    En effet, les fichiers ayant des structures trop différentes il faut s'adapter à chaque fois pour l'import.
    Cependant on garde une structure d'import de base. c.d. base_loader.py et l'ensemble des méthodes associées

    """

    def __init__(self, db: Database):
        self.data_directory = "data/db/"
        self.db = db

    def charger_tout(self) -> None:
        """On charge toutes les données

        Pour chaque "dossier de données", on instancie le loader spécifique puis on charge les données.
        """

        # 1. Sports (Pas de dépendances)
        for row in self._lire_csv("sports.csv"):
            id_s = int(row["id"])
            self.db.sports[id_s] = Sport(
                nom=row["_Sport__nom"],
                numero=id_s,
                nb_joueurs_par_equipe=int(row["_Sport__nb_joueurs_par_equipe"]),
                nb_equipes=int(row["_Sport__nb_equipes"]),
            )

        # 2. Arbitres et Coachs (Dépendent de rien, héritent de Personne)
        for row in self._lire_csv("arbitres.csv"):
            id_a = int(row["id"])
            self.db.arbitres[id_a] = Arbitre(
                id_personne=id_a,
                sport_arbitre=self.db.sports[int(row["_Arbitre__sport_arbitre"])],
                nom=row["_Personne__nom"],
                prenom=row["_Personne__prenom"],
                pays=row.get("_Personne__pays"),
            )

        for row in self._lire_csv("coachs.csv"):
            id_c = int(row["id"])
            self.db.coachs[id_c] = Coach(
                id_personne=id_c,
                sport_pratique=self.db.sports[int(row["_Coach__sport_pratique"])],
                nombre_medailles=int(row["_Coach__nombre_medailles"]),
                surnom=row["_Coach__surnom"],
                nom=row["_Personne__nom"],
                prenom=row["_Personne__prenom"],
                pays=row.get("_Personne__pays"),
            )

        # 3. Compétiteurs (Dépendent des Sports)
        for row in self._lire_csv("competiteurs.csv"):
            id_p = int(row["id"])
            id_sport = int(row["_Competiteur__sport_pratique"])

            competiteur = Competiteur(
                id_personne=id_p,
                nom=row["_Personne__nom"],
                prenom=row["_Personne__prenom"],
                sport_pratique=self.db.sports[id_sport],
                pays=row.get("_Personne__pays"),
                date_naissance=self._parser_date(row.get("_Personne__date_naissance")),
                taille=float(row["_Competiteur__taille"])
                if row.get("_Competiteur__taille")
                else None,
                poids=float(row["_Competiteur__poids"])
                if row.get("_Competiteur__poids")
                else None,
                numero_maillot=int(float(row["_Competiteur__numero_maillot"]))
                if row.get("_Competiteur__numero_maillot")
                else None,
                poste_principal=row.get("_Competiteur__poste_principal"),
            )
            self.db.competiteurs[id_p] = competiteur

        # 4. Équipes (Dépendent des Sports, Compétiteurs et Coachs)
        for row in self._lire_csv("equipes.csv"):
            id_e = int(row["id"])
            id_sport = int(row["_Equipe__discipline"])

            equipe = Equipe(
                id_equipe=id_e,
                nom_officiel=row["_Equipe__nom_officiel"],
                nom_abrege=row["_Equipe__nom_abrege"],
                ville=row.get("_Equipe__ville"),
                pays=row.get("_Equipe__pays"),
                discipline=self.db.sports[id_sport],
                genre=row.get("_Equipe__genre", "masculin"),
            )

            # Reconstruction des relations listes (IDs -> Objets)
            if row.get("_Equipe__liste_joueurs"):
                ids_joueurs = ast.literal_eval(row["_Equipe__liste_joueurs"])
                for id_j in ids_joueurs:
                    equipe.liste_joueurs.append(self.db.competiteurs[id_j])

            if row.get("_Equipe__liste_coachs"):
                ids_coachs = ast.literal_eval(row["_Equipe__liste_coachs"])
                for id_c in ids_coachs:
                    equipe.liste_coachs.append(self.db.coachs[id_c])

            self.db.equipes[id_e] = equipe

        # 5. Matchs (Dépendent des Équipes et Arbitres)
        for row in self._lire_csv("matchs.csv"):
            id_m = int(row["id"])

            # Equipes participantes
            ids_equipes = ast.literal_eval(row["_Match__liste_equipes_participantes"])
            liste_equipes = [self.db.equipes[eid] for eid in ids_equipes]

            # Score (Stocké en liste de tuples par le writer)
            score_raw = ast.literal_eval(row["_Match__score"])
            score_dict = {self.db.equipes[eid]: s for eid, s in score_raw}

            # Arbitre
            id_arb = row.get("_Match__arbitre")
            arbitre_obj = (
                self.db.arbitres[int(id_arb)]
                if id_arb and id_arb != "" and id_arb != "None"
                else None
            )

            match = Match(
                id_match=id_m,
                jour=self._parser_date(row.get("_Match__jour")),
                liste_equipes_participantes=liste_equipes,
                score=score_dict,
                arbitre=arbitre_obj,
                ville=row.get("_Match__ville"),
                lieu=row.get("_Match__lieu"),
                duree=int(float(row["_Match__duree"]))
                if row.get("_Match__duree")
                else None,
            )
            # Statistiques diverses (dictionnaire)
            if row.get("_Match__statistiques_diverses"):
                match.statistiques_diverses.update(
                    ast.literal_eval(row["_Match__statistiques_diverses"])
                )

            self.db.matchs[id_m] = match

        # 6. Compétitions
        for row in self._lire_csv("competitions.csv"):
            id_comp = int(row["id"])
            competition = Competition(
                id_competition=id_comp,
                nom=row["_Competition__nom"],
                edition=row.get("_Competition__edition"),
                organisateur=row.get("_Competition__organisateur"),
                date_debut=self._parser_date(row.get("_Competition__date_debut")),
                date_fin=self._parser_date(row.get("_Competition__date_fin")),
            )
            self.db.competitions[id_comp] = competition
