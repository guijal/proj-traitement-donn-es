from ..models.equipe import Equipe
from ..models.sport import Sport
from ..models.competiteur import Competiteur
from ..models.match import Match
from ..models.competition import Competition
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
            id_csv = int(ligne["id"]) # à mettre si ya un id_csv

            nouvel_id = self.db.generer_id_equipe()
            self.map_equipes[id_csv] = nouvel_id #à mettre si y'a un id_csv

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
            nouvel_id = self.db.generer_id_personne()
            self.map_personnes[id_csv] = nouvel_id

            competiteur = Competiteur(
                id_personne=nouvel_id,
                nom=ligne["first_name"],
                prenom=ligne["last_name"],
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

            #équipes en jeu
            equipe_home = self.db.equipes[self.map_equipes[int(ligne["team_id_home"])]]
            equipe_away = self.db.equipes[self.map_equipes[int(ligne["team_id_away"])]]
            match = Match(
                id_match=nouvel_id,
                jour=self._parser_date(ligne["game_date"]),
                id_csv=id_csv,
                liste_equipes_participantes=[equipe_home, equipe_away],
                score={equipe_home: ligne["pts_home"], equipe_away: ligne["pts_away"]},
                duree=int(ligne["min"])//5 #duree dun match dapres les explis du prof (selon les temps additionnel)
            )
            # Ajout dans la db
            self.db.matchs[nouvel_id] = match

            




    # on peut créer d'autres méthodes qui permettent de calculer d'autres infos à partir des données csv
    # on peut utiliser pandas pour ce faire
    # exemple here : https://foad-moodle.ensai.fr/pluginfile.php/47664/mod_resource/content/2/Exemple%20-%20Joueuses%20de%20tennis.html
