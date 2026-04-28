"""Données de démonstration NBA Playoffs pour la visualisation bracket."""

from datetime import date

from src.project.models.Sport import Sport
from src.project.models.Equipe import Equipe
from src.project.models.Match import Match
from src.project.models.PhaseEliminationDirecte import PhaseEliminationDirecte


COULEURS_EQUIPES: dict[str, str] = {
    "ORL": "#0077c0",
    "DET": "#c8102e",
    "MIA": "#98002e",
    "CLE": "#6f263d",
    "POR": "#e03a3e",
    "SAS": "#8a8d8f",
    "DEN": "#0e2240",
    "MIN": "#236192",
    "LAL": "#552583",
    "OKC": "#007ac1",
    "HOU": "#ce1141",
    "GSW": "#1d428a",
    "BOS": "#007a33",
    "NYK": "#f58426",
}


def creer_playoffs_demo() -> PhaseEliminationDirecte:
    """Construit un bracket de playoffs NBA-style avec données simulées.

    Returns
    -------
    PhaseEliminationDirecte
        Phase avec 8 équipes et scores de séries partiellement joués
    """
    basketball = Sport(nom="Basketball", numero=1, nb_joueurs_par_equipe=5, nb_equipes=8)

    equipes_data = [
        (1, "Orlando Magic", "ORL", "Orlando"),
        (2, "Detroit Pistons", "DET", "Detroit"),
        (3, "Miami Heat", "MIA", "Miami"),
        (4, "Cleveland Cavaliers", "CLE", "Cleveland"),
        (5, "Portland Trail Blazers", "POR", "Portland"),
        (6, "San Antonio Spurs", "SAS", "San Antonio"),
        (7, "Denver Nuggets", "DEN", "Denver"),
        (8, "Minnesota Timberwolves", "MIN", "Minnesota"),
    ]

    equipes = [
        Equipe(
            id_equipe=id_e,
            nom_officiel=nom,
            nom_abrege=abrege,
            ville=ville,
            discipline=basketball,
            genre="masculin",
        )
        for id_e, nom, abrege, ville in equipes_data
    ]

    phase = PhaseEliminationDirecte(nb_equipes=8)
    phase.creer_graphe_match()

    # Scores de séries (best-of-7) : (victoires_eq1, victoires_eq2)
    series_r1 = [
        (equipes[0], equipes[1], 3, 1),   # ORL leads 3-1
        (equipes[2], equipes[3], 2, 2),   # MIA tied 2-2
        (equipes[4], equipes[5], 1, 3),   # SAS leads 3-1
        (equipes[6], equipes[7], 2, 3),   # MIN leads 3-2
    ]

    racines = [n for n in phase.graphe_matchs if not n.liste_parents]
    for i, (eq1, eq2, v1, v2) in enumerate(series_r1):
        match = Match(id_match=i + 1, jour=date(2025, 4, 20))
        match.ajouter_equipe(eq1)
        match.ajouter_equipe(eq2)
        match.ajouter_points(eq1, v1)
        match.ajouter_points(eq2, v2)
        racines[i].match = match

    return phase
