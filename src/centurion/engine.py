from centurion.deck import Deck
from centurion.card import Card
from typing import List

class GameEngine:
    def __init__(self, counters: int = 21, include_jokers: int = 2):
        self.deck = Deck(include_jokers)
        self.players: List[List[Card]] = [[], []]
        self.counters = counters

        # NEW for US3:
        self.running_total: int = 0
        self.current_player: int = 0

    def start_match(self) -> None:
        self.deck.shuffle()
        self.players = [[], []]
        for _ in range(7):
            self.players[0].append(self.deck.deal())
            self.players[1].append(self.deck.deal())

    def play_turn(self, player_index: int, card_index: int) -> int:
        """
        Player plays the card at card_index from their hand,
        updates running_total, switches current_player, returns new total.
        """
        card = self.players[player_index].pop(card_index)
        self.running_total += card.value()
        self.current_player = 1 - player_index
        return self.running_total
