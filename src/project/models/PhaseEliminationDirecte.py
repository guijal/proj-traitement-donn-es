from .PhaseTournoi import PhaseTournoi
from .NoeudMatch import NoeudMatch


class PhaseEliminationDirecte(PhaseTournoi):
    """Phase de tournoi à élimination directe (bracket standard).

    Attributes
    ----------
    nb_equipes : int
        Nombre d'équipes (doit être une puissance de 2)
    """

    def __init__(self, nb_equipes: int = 8):
        if not isinstance(nb_equipes, int) or nb_equipes < 2:
            raise TypeError("nb_equipes doit être un int >= 2")
        super().__init__(format="élimination directe")
        self.__nb_equipes = nb_equipes

    def creer_graphe_match(self) -> None:
        """Construit la structure de bracket (noeuds vides, sans matchs)."""
        nb_r1 = self.__nb_equipes // 2
        noeuds_precedents = []

        for _ in range(nb_r1):
            noeud = NoeudMatch(numero_match=len(self.graphe_matchs))
            self.graphe_matchs.append(noeud)
            noeuds_precedents.append(noeud)

        while len(noeuds_precedents) > 1:
            suivants = []
            for i in range(0, len(noeuds_precedents), 2):
                parents = [noeuds_precedents[i], noeuds_precedents[i + 1]]
                noeud = self.ajouter_match_vainqueur_de(parents)
                suivants.append(noeud)
            noeuds_precedents = suivants

    def get_classement(self) -> dict:
        """Retourne le vainqueur de la phase (noeud finale sans enfant)."""
        for noeud in self.graphe_matchs:
            if not noeud.liste_enfants and noeud.match:
                vainqueur = noeud.match.vainqueur()
                if vainqueur:
                    return {1: vainqueur}
        return {}

    def get_noeuds_par_round(self) -> list[list]:
        """Retourne les noeuds groupés par tour (round 1 = racines).

        Returns
        -------
        list[list[NoeudMatch]]
            Chaque sous-liste correspond à un tour
        """
        restants = set(self.graphe_matchs)
        rounds = []

        racines = [n for n in self.graphe_matchs if not n.liste_parents]
        if not racines:
            return []
        rounds.append(racines)
        restants -= set(racines)

        while restants:
            precedent_set = set(rounds[-1])
            suivants = [
                n for n in restants
                if all(p in precedent_set for p in n.liste_parents)
            ]
            if not suivants:
                break
            rounds.append(suivants)
            restants -= set(suivants)

        return rounds
