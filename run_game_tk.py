# run_game_tk.py.4                                                                                      run_game_tk.py                                                                                      Modified
        if hasattr(w, "card_index"):
            self.engine.play_turn(self.engine.current_player, w.card_index)
            if self.engine.check_deal_end():
                played = sum(7 - len(h) for h in self.engine.players)
                self.score.computeBase(played)
                self.score.computePenalty(self.engine.running_total)
                pts = self.score.computeFinal()
                winner = self.engine.current_player + 1
                messagebox.showinfo("Deal Over", f"Playe



import os, sys
# make sure Python can find your packagfrom centurion.score im
RANK_NAME = {1:"A", 11:"J",12:"Q"
class CardLabel(tk.Label)
    def __init__(self, mster, card, **kw):
        symbol = card.suit.name[0] if card.suit else "JK"
        rank   = RANK_NAME.get(card.rank, str(card.rank))
        bg      = "white"
        fg      = "red" if card.suit and card.suit.name in ("HEARTS","DIAMONDS") else "black"
        super().__init__(master, text=f"{rank}{symbol}", bg=bg, fg=fg,
                         width=4, height=2, borderwidth=2, relief="raised")

class GameUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Centurion")
        self.engine = GameEngine(counters=21, include_jokers=0)
        self.score  = Score()
        self.engine.start_match()
        self._build()
        self._draw_hand()

    def _build(self):
        self.frame = tk.Frame(self)
        self.frame.pack(pady=20)
        self.info  = tk.Label(self)
        self.info.pack()
        self.bind("<Button-1>", self._on_click)

    def _draw_hand(self):
        for w in self.frame.winfo_children():
            w.destroy()
        p    = self.engine.current_player
        hand = self.engine.players[p]
        self.info.config(text=f"Player {p+1} — Total: {self.engine.running_total}")
        for i, c in enumerate(hand):
            lbl = CardLabel(self.frame, c)
            lbl.grid(row=0, column=i, padx=5)
            lbl.card_index = i

    def _on_click(self, evt):
        w = evt.widget
        if hasattr(w, "card_index"):
            self.engine.play_turn(self.engine.current_player, w.card_index)
            if self.engine.check_deal_end():
                played = sum(7 - len(h) for h in self.engine.players)
                self.score.computeBase(played)
                self.score.computePenalty(self.engine.running_total)
                pts = self.score.computeFinal()
                winner = self.engine.current_player + 1
                messagebox.showinfo("Deal Over", f"Playe
