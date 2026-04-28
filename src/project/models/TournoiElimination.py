from .Tournoi import Tournoi
from .PhaseTournoi import PhaseTournoi
from .Sport import Sport


class TournoiElimination(Tournoi):
    """Tournoi à élimination directe."""

    def get_classement(self) -> dict:
        if not self.liste_phases:
            return {}
        return self.liste_phases[-1].get_classement()

    def ajouter_phase(self, phase: PhaseTournoi) -> None:
        if not isinstance(phase, PhaseTournoi):
            raise TypeError("phase doit être une PhaseTournoi")
        self.liste_phases.append(phase)
