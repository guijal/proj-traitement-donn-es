from ..models.Equipe import Equipe
from ..models.Sport import Sport
from ..models.Competiteur import Competiteur
from ..models.Match import Match
from ..models.Competition import Competition
from .base_loader import BaseLoader


class BasketballLoader(BaseLoader):
    """Loader spécifique pour les données de basketball.

    Suit la structure d'import générale (c.f. base_loader.py)
    """

    def __init__(self, data_directory: str, db):
        super().__init__(data_directory, db)

    def charger_tout(self) -> None:
        """Orchestre le chargement de toutes les données liées au basketball.

        Pour chaque dossier, créer le load du sport.
        Pour chaque fichier dans le dossier de données, créer une méthode qui instancie les données.
        ! Mettre les chargements dans l'ordre : par ex les équipes doivent être chargées avant les matchs
        """

        # Ici on créé le/les sports en lien avec les csv car il n'y a pas de "sports.csv", il faut les créer un par un selon les données fournies
        self.unique_charger_sport("Basketball", 5, 2)

        self.charger_equipes("basketball/team.csv")
        self.charger_joueurs("basketball/player.csv")
        self.charger_matchs("basketball/game.csv")

    def charger_equipes(self, nom_fichier: str) -> None:
        donnees = self._lire_csv(nom_fichier)
        # donnees est une ligne et chaque elt de la liste est un dictionnaire qui contient {variable:valeur}. Ex {nom:Fiodor}
        for ligne in donnees:
            id_csv = int(ligne["id"])  # à mettre si ya un id_csv

            nouvel_id = self.db.generer_id_equipe()
            self.map_equipes[id_csv] = nouvel_id  # à mettre si y'a un id_csv

            equipe = Equipe(
                id_equipe=nouvel_id,
                nom_officiel=ligne["full_name"],
                nom_abrege=ligne["abbreviation"],
                ville=ligne["city"],
                pays="USA",
                code_pays="US",
                etat=ligne["state"],
                genre="masculin",
                discipline=self.sport,  # On utilise directement l'attribut créé dans __init__
                id_csv=id_csv,
            )
            # Ajout dans la db
            self.db.equipes[nouvel_id] = equipe

            # mettre aussi les ajouts aux classes qui dépendent. par ex
            # à la création dun joueur il faut modifier Equipe

    def charger_joueurs(self, nom_fichier: str) -> None:
        donnees = self._lire_csv(nom_fichier)
        for ligne in donnees:
            id_csv = int(ligne["person_id"])
            nouvel_id = self.db.generer_id_competiteur()
            self.map_personnes[id_csv] = nouvel_id

            competiteur = Competiteur(
                id_personne=nouvel_id,
                prenom=ligne["first_name"],
                nom=ligne["last_name"],
                date_naissance=self._parser_date(ligne["birthdate"]),
                id_csv=id_csv,
                sport_pratique=self.sport,
                numero_maillot=int(ligne["jersey"]),
                poste_principal=ligne["position"],
                taille=self._parser_height(ligne["height"]),
                poids=self._parser_weight(ligne["weight"]),
            )
            # Ajout dans la db
            self.db.competiteurs[nouvel_id] = competiteur

            # ajout du joueur dans l'équipe associée
            id_equipe = self.map_equipes[int(ligne["team_id"])]
            self.db.equipes[id_equipe].liste_joueurs.append(competiteur)

    def charger_matchs(self, nom_fichier: str) -> None:
        donnees = self._lire_csv(nom_fichier)
        for ligne in donnees:
            id_csv = int(ligne["game_id"])
            nouvel_id = self.db.generer_id_match()
            self.map_matchs[id_csv] = nouvel_id

            # équipes en jeu
            equipe_home = self.db.equipes[self.map_equipes[int(ligne["team_id_home"])]]
            equipe_away = self.db.equipes[self.map_equipes[int(ligne["team_id_away"])]]

            # Récupération des colonnes que l'on met dans statistiques_diverses
            colonnes_diverses = {
                "fgm_home",
                "fga_home",
                "fg_pct_home",
                "fg3m_home",
                "fg3a_home",
                "fg3_pct_home",
                "ftm_home",
                "fta_home",
                "ft_pct_home",
                "oreb_home",
                "dreb_home",
                "reb_home",
                "ast_home",
                "stl_home",
                "blk_home",
                "tov_home",
                "pf_home",
                "fgm_away",
                "fga_away",
                "fg_pct_away",
                "fg3m_away",
                "fg3a_away",
                "fg3_pct_away",
                "ftm_away",
                "fta_away",
                "ft_pct_away",
                "oreb_away",
                "dreb_away",
                "reb_away",
                "ast_away",
                "stl_away",
                "blk_away",
                "tov_away",
                "pf_away",
            }
            stats_diverses: dict = {}
            for cle, valeur in ligne.items():
                if cle in colonnes_diverses:
                    # Essayer de convertir en float/int si c'est numérique
                    self._parser_stats_diverses_auto(cle, valeur, stats_diverses)

            match = Match(
                id_match=nouvel_id,
                jour=self._parser_date(ligne["game_date"]),
                id_csv=id_csv,
                liste_equipes_participantes=[equipe_home, equipe_away],
                score={
                    equipe_home: int(ligne["pts_home"]),
                    equipe_away: int(ligne["pts_away"]),
                },
                duree=int(ligne["min"])
                // 5,  # duree dun match dapres les explis du prof (selon les temps additionnel)
            )

            # Ajout dans la db
            self.db.matchs[nouvel_id] = match

    # on peut créer d'autres méthodes qui permettent de calculer d'autres infos à partir des données csv
    # on peut utiliser pandas pour ce faire
    # exemple here : https://foad-moodle.ensai.fr/pluginfile.php/47664/mod_resource/content/2/Exemple%20-%20Joueuses%20de%20tennis.html
