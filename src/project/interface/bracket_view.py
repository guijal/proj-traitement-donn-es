"""Widget tkinter de visualisation bracket (élimination directe)."""

import tkinter as tk
from tkinter import font as tkfont

from src.project.models.PhaseEliminationDirecte import PhaseEliminationDirecte
from src.project.models.NoeudMatch import NoeudMatch
from src.project.interface.demo_data import COULEURS_EQUIPES

# ── Dimensions d'une carte match ──────────────────────────────────────────────
CARD_W = 210
CARD_H = 82          # 2 lignes équipes + 14px label statut
ROW_H = 34           # hauteur d'une ligne équipe
STATUS_H = CARD_H - 2 * ROW_H   # hauteur de la ligne statut
STRIP_W = 8          # largeur de la bande colorée par équipe

# ── Espacement entre les tours ─────────────────────────────────────────────────
H_GAP = 70           # gap horizontal entre colonnes de rounds
SLOT_H = CARD_H + 90 # hauteur d'un slot en round 1

# ── Couleurs globales ──────────────────────────────────────────────────────────
BG_APP = "#f0f2f5"
BG_CARD = "#ffffff"
BG_TBD = "#dde0e4"
COLOR_WINNER_BG = "#e8f5e9"
COLOR_WINNER_TEXT = "#1b5e20"
COLOR_LOSER_TEXT = "#9e9e9e"
COLOR_BORDER = "#cfd4db"
COLOR_CONNECTOR = "#9aa3af"
COLOR_HEADER = "#1a3a6b"
COLOR_HEADER_TEXT = "#ffffff"
COLOR_STATUS = "#607080"
PADDING = 40


class BracketView(tk.Frame):
    """Frame contenant un Canvas scrollable avec le bracket de tournoi.

    Parameters
    ----------
    parent : tk.Widget
        Widget parent tkinter
    phase : PhaseEliminationDirecte
        Phase à afficher
    """

    def __init__(self, parent: tk.Widget, phase: PhaseEliminationDirecte):
        super().__init__(parent, bg=BG_APP)
        self._phase = phase
        self._positions: dict[NoeudMatch, tuple[int, int]] = {}
        self._rounds: list[list[NoeudMatch]] = []

        self._build_ui()
        self._render()

    # ── Construction UI ────────────────────────────────────────────────────────

    def _build_ui(self) -> None:
        self.canvas = tk.Canvas(self, bg=BG_APP, highlightthickness=0)
        scroll_x = tk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        scroll_y = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-4>", self._on_mousewheel)
        self.canvas.bind("<Button-5>", self._on_mousewheel)

    def _on_mousewheel(self, event: tk.Event) -> None:
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")
        else:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    # ── Rendu principal ────────────────────────────────────────────────────────

    def _render(self) -> None:
        self.canvas.delete("all")

        self._rounds = self._phase.get_noeuds_par_round()
        if not self._rounds:
            self.canvas.create_text(200, 100, text="Aucun match à afficher", font=("Arial", 14))
            return

        self._positions = self._calculer_positions()
        self._dessiner_entetes_rounds()
        self._dessiner_connecteurs()
        self._dessiner_cartes()
        self._ajuster_scrollregion()

    def _calculer_positions(self) -> dict[NoeudMatch, tuple[int, int]]:
        positions: dict[NoeudMatch, tuple[int, int]] = {}
        header_h = 36  # espace pour les labels de round en haut

        for i, noeud in enumerate(self._rounds[0]):
            x = PADDING
            y = header_h + PADDING + i * SLOT_H
            positions[noeud] = (x, y)

        for r in range(1, len(self._rounds)):
            for noeud in self._rounds[r]:
                parents = noeud.liste_parents
                parent_centers_y = [positions[p][1] + CARD_H / 2 for p in parents if p in positions]
                y_center = sum(parent_centers_y) / len(parent_centers_y)
                x = PADDING + r * (CARD_W + H_GAP)
                y = y_center - CARD_H / 2
                positions[noeud] = (x, y)

        return positions

    def _dessiner_entetes_rounds(self) -> None:
        labels = ["1er Tour", "Demi-finales", "Finale", "Champion"]
        fnt = tkfont.Font(family="Arial", size=10, weight="bold")
        for r, noeuds in enumerate(self._rounds):
            x = PADDING + r * (CARD_W + H_GAP) + CARD_W // 2
            self.canvas.create_text(
                x, 18, text=labels[r] if r < len(labels) else f"Round {r+1}",
                font=fnt, fill=COLOR_HEADER, anchor="center"
            )

    def _dessiner_connecteurs(self) -> None:
        for r in range(1, len(self._rounds)):
            for noeud in self._rounds[r]:
                if noeud not in self._positions:
                    continue
                cx, cy = self._positions[noeud]
                child_center_y = cy + CARD_H / 2

                for parent in noeud.liste_parents:
                    if parent not in self._positions:
                        continue
                    px, py = self._positions[parent]
                    parent_center_y = py + CARD_H / 2
                    mid_x = px + CARD_W + H_GAP / 2

                    # Ligne horizontale depuis parent
                    self.canvas.create_line(
                        px + CARD_W, parent_center_y,
                        mid_x, parent_center_y,
                        fill=COLOR_CONNECTOR, width=2
                    )
                    # Ligne verticale vers l'enfant
                    self.canvas.create_line(
                        mid_x, parent_center_y,
                        mid_x, child_center_y,
                        fill=COLOR_CONNECTOR, width=2
                    )
                    # Ligne horizontale vers l'enfant
                    self.canvas.create_line(
                        mid_x, child_center_y,
                        cx, child_center_y,
                        fill=COLOR_CONNECTOR, width=2
                    )

    def _dessiner_cartes(self) -> None:
        for noeud, (x, y) in self._positions.items():
            self._dessiner_carte(noeud, x, y)

    # ── Dessin d'une carte ─────────────────────────────────────────────────────

    def _dessiner_carte(self, noeud: NoeudMatch, x: int, y: int) -> None:
        if noeud.match is None or not noeud.match.liste_equipes_participantes:
            self._dessiner_carte_tbd(x, y)
            return

        match = noeud.match
        equipes = match.liste_equipes_participantes[:2]
        vainqueur = match.vainqueur() if match.score else None

        # Fond de carte
        self.canvas.create_rectangle(
            x, y, x + CARD_W, y + CARD_H,
            fill=BG_CARD, outline=COLOR_BORDER, width=1
        )

        for i, equipe in enumerate(equipes):
            row_y = y + i * ROW_H
            is_winner = equipe == vainqueur and any(v > 0 for v in match.score.values())

            # Bande colorée à gauche
            couleur = COULEURS_EQUIPES.get(equipe.nom_abrege or "", "#8899aa")
            self.canvas.create_rectangle(
                x, row_y, x + STRIP_W, row_y + ROW_H,
                fill=couleur, outline=""
            )

            # Fond de ligne (léger vert pour le gagnant)
            if is_winner:
                self.canvas.create_rectangle(
                    x + STRIP_W, row_y, x + CARD_W, row_y + ROW_H,
                    fill=COLOR_WINNER_BG, outline=""
                )

            # Séparateur horizontal entre les deux équipes
            if i == 1:
                self.canvas.create_line(
                    x, row_y, x + CARD_W, row_y,
                    fill=COLOR_BORDER, width=1
                )

            # Nom abrégé
            text_color = COLOR_WINNER_TEXT if is_winner else "#2c3e50"
            weight = "bold" if is_winner else "normal"
            fnt = tkfont.Font(family="Arial", size=11, weight=weight)
            self.canvas.create_text(
                x + STRIP_W + 8, row_y + ROW_H // 2,
                text=equipe.nom_abrege or equipe.nom_officiel,
                anchor="w", fill=text_color, font=fnt
            )

            # Score de série
            score = match.score.get(equipe, 0)
            self.canvas.create_text(
                x + CARD_W - 10, row_y + ROW_H // 2,
                text=str(score),
                anchor="e", fill=text_color, font=fnt
            )

        # Ligne de statut (sous les deux équipes)
        status_y = y + 2 * ROW_H
        self.canvas.create_rectangle(
            x, status_y, x + CARD_W, y + CARD_H,
            fill="#f7f8fa", outline=COLOR_BORDER, width=1
        )
        self.canvas.create_text(
            x + CARD_W // 2, status_y + STATUS_H // 2,
            text=self._get_status(match),
            anchor="center", fill=COLOR_STATUS,
            font=tkfont.Font(family="Arial", size=8)
        )

        # Bordure extérieure de la carte
        self.canvas.create_rectangle(
            x, y, x + CARD_W, y + CARD_H,
            fill="", outline=COLOR_BORDER, width=1
        )

    def _dessiner_carte_tbd(self, x: int, y: int) -> None:
        self.canvas.create_rectangle(
            x, y, x + CARD_W, y + CARD_H,
            fill=BG_TBD, outline=COLOR_BORDER, width=1, dash=(4, 3)
        )
        fnt = tkfont.Font(family="Arial", size=11)
        self.canvas.create_text(
            x + CARD_W // 2, y + CARD_H // 2,
            text="À déterminer", anchor="center",
            fill="#8a96a3", font=fnt
        )

    # ── Utilitaires ───────────────────────────────────────────────────────────

    @staticmethod
    def _get_status(match) -> str:
        if not match.score or not match.liste_equipes_participantes:
            return "À venir"
        equipes = match.liste_equipes_participantes[:2]
        s = [match.score.get(e, 0) for e in equipes]
        MAX_WINS = 4
        if s[0] == MAX_WINS:
            return f"{equipes[0].nom_abrege} wins {s[0]}-{s[1]}"
        if s[1] == MAX_WINS:
            return f"{equipes[1].nom_abrege} wins {s[1]}-{s[0]}"
        if s[0] > s[1]:
            return f"{equipes[0].nom_abrege} leads {s[0]}-{s[1]}"
        if s[1] > s[0]:
            return f"{equipes[1].nom_abrege} leads {s[1]}-{s[0]}"
        return f"Series tied {s[0]}-{s[1]}"

    def _ajuster_scrollregion(self) -> None:
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def charger_phase(self, phase: PhaseEliminationDirecte) -> None:
        """Recharge le bracket avec une nouvelle phase."""
        self._phase = phase
        self._render()
