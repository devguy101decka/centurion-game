
# run_game_tk.py

import os
import sys
# Ensure Python can find your package under src/
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import tkinter as tk
from tkinter import messagebox
from centurion.engine import GameEngine
from centurion.score import Score

# Full names for ranks and suits
RANK_NAME_FULL = {
    1:  "Ace",   2:  "Two",    3:  "Three",  4:  "Four",
    5:  "Five",  6:  "Six",    7:  "Seven",  8:  "Eight",
    9:  "Nine",  10: "Ten",    11: "Jack",   12: "Queen",
    13: "King"
}
SUIT_NAME_FULL = {
    "SPADES":   "Spades",
    "HEARTS":   "Hearts",
    "CLUBS":    "Clubs",
    "DIAMONDS": "Diamonds",
}

class CardLabel(tk.Label):
    def __init__(self, master, card, **kw):
        rank = RANK_NAME_FULL.get(card.rank, "Joker")
        suit = SUIT_NAME_FULL.get(card.suit.name, "Joker") if card.suit else "Joker"
        text = f"{rank}\nof\n{suit}"
        fg   = "red" if card.suit and card.suit.name in ("HEARTS", "DIAMONDS") else "black"

        super().__init__(
            master,
            text=text,
            bg="white",
            fg=fg,
            width=8,
            height=4,
            borderwidth=2,
            relief="raised",
            **kw
        )

class GameUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Centurion")
        self.engine = GameEngine(counters=21, include_jokers=0)
        self.score  = Score()
        self.engine.start_match()
        self._build_ui()
        self._draw_hand()

    def _build_ui(self):
        self.card_frame = tk.Frame(self)
        self.card_frame.pack(pady=20)
        self.info_label = tk.Label(self, text="")
        self.info_label.pack()
        self.bind("<Button-1>", self._on_click)

    def _draw_hand(self):
        for w in self.card_frame.winfo_children():
            w.destroy()

        p    = self.engine.current_player
        hand = self.engine.players[p]
        self.info_label.config(text=f"Player {p+1} — Total: {self.engine.running_total}")

        for i, card in enumerate(hand):
            lbl = CardLabel(self.card_frame, card)
            lbl.grid(row=0, column=i, padx=5)
            lbl.card_index = i

    def _on_click(self, event):
        w = event.widget
        if not hasattr(w, "card_index"):
            return

        idx = w.card_index
        # play the card
        self.engine.play_turn(self.engine.current_player, idx)

        if self.engine.check_deal_end():
            # figure out who actually played the last card
            scoring_player = 1 - self.engine.current_player

            # Compute points
            played = sum(7 - len(h) for h in self.engine.players)
            self.score.computeBase(played)
            self.score.computePenalty(self.engine.running_total)
            pts = self.score.computeFinal()

            # Show deal-over message for the right player
            messagebox.showinfo(
                "Deal Over",
                f"Player {scoring_player+1} scores {pts} point(s)"
            )

            # Award counters to that player
            if self.engine.award_counters(scoring_player, pts):
                over = tk.Toplevel(self)
                over.title("Game Over")
                tk.Label(
                    over,
                    text="🎮 Game Over 🎉",
                    fg="blue",
                    padx=20, pady=20
                ).pack()
                return
            else:
                messagebox.showinfo(
                    "Next Deal",
                    f"Counters remaining: {self.engine.counter_pool.remainingCounters}"
                )
                self.engine.start_match()

        # redraw the current hand (either next deal or same deal if not ended)
        self._draw_hand()

if __name__ == "__main__":
    app = GameUI()
    app.mainloop()                    font=("Helvetica", 24),
                messagebox.showinfo(
