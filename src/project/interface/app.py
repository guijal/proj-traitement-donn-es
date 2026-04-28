"""Fenêtre principale de l'application sports analytics (tkinter)."""

import tkinter as tk
from tkinter import ttk, font as tkfont

from src.project.interface.bracket_view import BracketView, BG_APP, COLOR_HEADER, COLOR_HEADER_TEXT
from src.project.interface.demo_data import creer_playoffs_demo
from src.project.models.PhaseEliminationDirecte import PhaseEliminationDirecte


ONGLETS = ["BRACKET", "MATCHS", "ÉQUIPES"]
APP_TITLE = "Sports Analytics"
APP_GEOMETRY = "960x680"


class AppSport(tk.Tk):
    """Fenêtre principale avec barre de navigation et onglets.

    Parameters
    ----------
    phase : PhaseEliminationDirecte | None
        Phase à afficher. Si None, charge les données de démo.
    """

    def __init__(self, phase: PhaseEliminationDirecte | None = None):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(APP_GEOMETRY)
        self.configure(bg=COLOR_HEADER)
        self.minsize(720, 500)

        self._phase = phase or creer_playoffs_demo()
        self._onglet_actif = tk.StringVar(value=ONGLETS[0])

        self._construire_ui()

    # ── Construction UI ────────────────────────────────────────────────────────

    def _construire_ui(self) -> None:
        self._creer_header()
        self._creer_contenu()
        self._afficher_onglet(ONGLETS[0])

    def _creer_header(self) -> None:
        header = tk.Frame(self, bg=COLOR_HEADER, height=54)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        # Titre / logo
        fnt_titre = tkfont.Font(family="Arial", size=15, weight="bold")
        tk.Label(
            header, text="🏆  Sports Analytics",
            bg=COLOR_HEADER, fg=COLOR_HEADER_TEXT,
            font=fnt_titre, padx=18
        ).pack(side="left", pady=10)

        # Boutons onglets
        self._boutons_nav: dict[str, tk.Label] = {}
        nav_frame = tk.Frame(header, bg=COLOR_HEADER)
        nav_frame.pack(side="left", padx=20)

        fnt_nav = tkfont.Font(family="Arial", size=11, weight="bold")
        for onglet in ONGLETS:
            btn = tk.Label(
                nav_frame, text=onglet,
                bg=COLOR_HEADER, fg="#a8bcd8",
                font=fnt_nav, padx=16, pady=14, cursor="hand2"
            )
            btn.pack(side="left")
            btn.bind("<Button-1>", lambda e, o=onglet: self._afficher_onglet(o))
            btn.bind("<Enter>", lambda e, b=btn: b.configure(fg="#ffffff"))
            btn.bind("<Leave>", lambda e, b=btn, o=onglet: b.configure(
                fg="#ffffff" if o == self._onglet_actif.get() else "#a8bcd8"
            ))
            self._boutons_nav[onglet] = btn

        # Soulignement de l'onglet actif
        self._indicateur = tk.Frame(header, bg="#f5c518", height=3)
        self._indicateur.place(x=0, y=0, width=0)  # positionné dynamiquement

    def _creer_contenu(self) -> None:
        self._zone_contenu = tk.Frame(self, bg=BG_APP)
        self._zone_contenu.pack(fill="both", expand=True)

        # Bracket view (préchargé)
        self._bracket_view = BracketView(self._zone_contenu, self._phase)

        # Vue placeholder matchs
        self._vue_matchs = self._creer_vue_placeholder(
            "Matchs", "Liste des matchs à venir ici."
        )

        # Vue placeholder équipes
        self._vue_equipes = self._creer_vue_placeholder(
            "Équipes", "Liste des équipes à venir ici."
        )

        self._vues = {
            "BRACKET": self._bracket_view,
            "MATCHS": self._vue_matchs,
            "ÉQUIPES": self._vue_equipes,
        }

    @staticmethod
    def _creer_vue_placeholder(titre: str, message: str) -> tk.Frame:
        frame = tk.Frame(bg=BG_APP)
        fnt = tkfont.Font(family="Arial", size=13)
        tk.Label(
            frame, text=f"{titre}\n\n{message}",
            bg=BG_APP, fg="#607080", font=fnt, justify="center"
        ).pack(expand=True)
        return frame

    # ── Navigation ─────────────────────────────────────────────────────────────

    def _afficher_onglet(self, nom: str) -> None:
        # Cacher la vue courante
        for vue in self._vues.values():
            vue.pack_forget()

        # Afficher la nouvelle vue
        self._vues[nom].pack(in_=self._zone_contenu, fill="both", expand=True)
        self._onglet_actif.set(nom)

        # Mettre à jour les couleurs des boutons
        for o, btn in self._boutons_nav.items():
            btn.configure(fg="#ffffff" if o == nom else "#a8bcd8")

        # Déplacer l'indicateur sous le bouton actif
        self._deplacer_indicateur(nom)

    def _deplacer_indicateur(self, nom: str) -> None:
        btn = self._boutons_nav.get(nom)
        if btn is None:
            return
        self.update_idletasks()
        x = btn.winfo_x() + btn.master.winfo_x()
        w = btn.winfo_width()
        self._indicateur.place(x=x, y=51, width=w, height=3)


def lancer_app(phase: PhaseEliminationDirecte | None = None) -> None:
    """Point d'entrée pour lancer l'application graphique.

    Parameters
    ----------
    phase : PhaseEliminationDirecte | None
        Phase à afficher. Si None, utilise les données de démo.
    """
    app = AppSport(phase=phase)
    app.mainloop()
