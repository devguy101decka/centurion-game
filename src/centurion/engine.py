from centurion.deck import Deck
from centurion.card import Card
from centurion.counterpool import CounterPool
from typing import List

class GameEngine:
    def __init__(self, counters: int = 21, include_jokers: int = 2):
        self.include_jokers = include_jokers
        self.counter_pool   = CounterPool(counters)

        # US3 fields
        self.running_total  = 0
        self.current_player = 0

        # first deck & deal
        self.start_match()

    def start_match(self) -> None:
        """Reset everything for a new deal, then shuffle and deal 7 cards each."""
        # fresh deck
        self.deck = Deck(self.include_jokers)
        self.deck.shuffle()

        # reset hands and running total / turn
        self.players        = [[], []]
        self.running_total  = 0
        self.current_player = 0

        # deal 7 cards to each player
        for _ in range(7):
            self.players[0].append(self.deck.deal())
            self.players[1].append(self.deck.deal())
