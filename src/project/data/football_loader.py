# /src/project/data/football_loader.py
from ..models.Equipe import Equipe
from ..models.Sport import Sport
from ..models.Competiteur import Competiteur
from ..models.Match import Match
from ..models.Competition import Competition
from .base_loader import BaseLoader


class FootballLoader(BaseLoader):
    """Loader spécifique pour les données de football.

    Suit la structure d'import générale (c.f. base_loader.py)
    """

    def __init__(self, data_directory: str, db):
        super().__init__(data_directory, db)

    def charger_tout(self) -> None:
        """Orchestre le chargement de toutes les données liées au football."""
        # Ici, vous devez définir les paramètres spécifiques au football
        # Par exemple, 11 joueurs par équipe, 2 équipes par match
        self.unique_charger_sport("Football", 11, 2)

        self.charger_equipes("football_european_leagues/team.csv")
        self.charger_joueurs("football_european_leagues/player.csv")
        self.charger_matchs("football_european_leagues/match.csv")

    def charger_equipes(self, nom_fichier: str) -> None:
        donnees = self._lire_csv(nom_fichier)
        for ligne in donnees:
            id_csv = int(
                ligne["team_api_id"]
            )  # Utilisation de team_api_id pour le mapping
            nouvel_id = self.db.generer_id_equipe()
            self.map_equipes[id_csv] = nouvel_id

            equipe = Equipe(
                id_equipe=nouvel_id,
                nom_officiel=ligne["team_long_name"],
                nom_abrege=ligne["team_short_name"],
                ville="",  # Non disponible dans les colonnes fournies
                pays="",  # Non disponible dans les colonnes fournies
                code_pays="",  # Non disponible dans les colonnes fournies
                etat="",  # Non disponible dans les colonnes fournies
                genre="masculin",  # Par défaut
                discipline=self.sport,  # On utilise directement l'attribut créé dans __init__
                id_csv=id_csv,  # L'id du CSV est l'id de la ligne
            )
            self.db.equipes[nouvel_id] = equipe

    def charger_joueurs(self, nom_fichier: str) -> None:
        donnees = self._lire_csv(nom_fichier)  # player.csv
        for ligne in donnees:
            id_csv = int(
                ligne["player_api_id"]
            )  # Utilisation de player_api_id comme id_csv
            nouvel_id = self.db.generer_id_competiteur()
            self.map_personnes[id_csv] = nouvel_id

            prenom, nom = self._parser_prenom_nom(ligne["player_name"])

            competiteur = Competiteur(
                id_personne=nouvel_id,
                nom=nom,
                prenom=prenom,
                date_naissance=self._parser_date(ligne["birthday"]),
                id_csv=id_csv,
                sport_pratique=self.sport,
                numero_maillot=None,  # Non disponible dans les colonnes fournies
                poste_principal="",  # Non disponible dans les colonnes fournies
                taille=float(ligne["height (cm)"])
                if ligne.get("height (cm)")
                else None,  # Déjà en cm
                poids=float(ligne["weight (kg)"])
                if ligne.get("weight (kg)")
                else None,  # Déjà en kg
                pays="",  # Non disponible dans les colonnes fournies
            )
            self.db.competiteurs[nouvel_id] = competiteur

            # Les joueurs ne sont pas directement liés à une équipe dans ce CSV,
            # donc pas d'ajout à equipe.liste_joueurs ici.

    def charger_matchs(self, nom_fichier: str) -> None:
        donnees = self._lire_csv(nom_fichier)
        for ligne in donnees:  # match.csv
            id_csv = int(
                ligne["match_api_id"]
            )  # Utilisation de match_api_id comme id_csv
            nouvel_id = self.db.generer_id_match()
            self.map_matchs[id_csv] = nouvel_id

            equipe_home = None
            if int(ligne["home_team_api_id"]) in self.map_equipes:
                equipe_home = self.db.equipes[
                    self.map_equipes[int(ligne["home_team_api_id"])]
                ]

            equipe_away = None
            if int(ligne["away_team_api_id"]) in self.map_equipes:
                equipe_away = self.db.equipes[
                    self.map_equipes[int(ligne["away_team_api_id"])]
                ]

            if not equipe_home or not equipe_away:
                print(
                    f"Avertissement: Équipe non trouvée pour le match {id_csv}. Match ignoré."
                )
                continue

            score_home = (
                int(ligne["home_team_goal"]) if ligne.get("home_team_goal") else 0
            )
            score_away = (
                int(ligne["away_team_goal"]) if ligne.get("away_team_goal") else 0
            )

            # --- Ajout des statistiques diverses pour les matchs de football ---
            colonnes_diverses_football = {
                "country_id",
                "league_id",
                "season",
                "stage",
                # Les colonnes home_player_X et away_player_X sont des IDs de joueurs
                # et nécessiteraient une logique de mapping plus complexe pour être
                # stockées comme des objets Competiteur dans le Match.
                # Pour l'instant, nous les ignorons dans les statistiques diverses.
            }

            stats_diverses: dict = {}
            for cle, valeur in ligne.items():
                if cle in colonnes_diverses_football:
                    self._parser_stats_diverses_auto(cle, valeur, stats_diverses)
            # --- Fin de l'ajout des statistiques diverses ---

            match = Match(
                id_match=nouvel_id,
                jour=self._parser_date(ligne["date"]),
                id_csv=id_csv,
                liste_equipes_participantes=[equipe_home, equipe_away],
                score={
                    equipe_home: score_home,
                    equipe_away: score_away,
                },
                duree=None,  # La colonne 'duration' n'est pas présente dans les données fournies
                statistiques_diverses=stats_diverses if stats_diverses else None,
            )
            self.db.matchs[nouvel_id] = match
