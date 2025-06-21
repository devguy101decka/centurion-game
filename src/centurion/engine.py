from centurion.deck import Deck
from centurion.card import Card
from typing import List

class GameEngine:
    def __init__(self, counters: int = 21, include_jokers: int = 2):
        self.deck = Deck(include_jokers)
        # Two players, each with their own hand list
        self.players: List[List[Card]] = [[], []]
        self.counters = counters

    def start_match(self) -> None:
        """Shuffle and deal 7 cards to each player."""
        self.deck.shuffle()
        # Clear any existing hands
        self.players = [[], []]
        # Deal exactly 7 cards each
        for _ in range(7):
            self.players[0].append(self.deck.deal())
            self.players[1].append(self.deck.deal())
