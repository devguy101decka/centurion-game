from centurion.deck import Deck
from centurion.card import Card
from centurion.counterpool import CounterPool   # ← don’t forget this import
from typing import List

class GameEngine:
    def __init__(self, counters: int = 21, include_jokers: int = 2):
        self.deck = Deck(include_jokers)
        self.players: List[List[Card]] = [[], []]
        self.counter_pool = CounterPool(counters)

        # US3 fields
        self.running_total: int = 0
        self.current_player: int = 0

    def start_match(self) -> None:
        """Shuffle and deal 7 cards each to begin the match."""
        self.deck.shuffle()
        self.players = [[], []]
        for _ in range(7):
            self.players[0].append(self.deck.deal())
            self.players[1].append(self.deck.deal())

    def play_turn(self, player_index: int, card_index: int) -> int:
        """
        Player plays the card at card_index from their hand,
        updates running_total, switches current_player, and returns new total.
        """
        card = self.players[player_index].pop(card_index)
        self.running_total += card.value()
        self.current_player = 1 - player_index
        return self.running_total

    def check_deal_end(self) -> bool:
        """
        Returns True if the deal is over:
          - running_total == 100
          - running_total > 100 and is a multiple of 10
          - both players have no cards left
        Otherwise False.
        """
        if self.running_total == 100:
            return True
        if self.running_total > 100 and self.running_total % 10 == 0:
            return True
        if all(len(hand) == 0 for hand in self.players):
            return True
        return False

    def award_counters(self, player_index: int, points: int) -> bool:
        """
        Player takes 'points' counters. Returns True if pool is now empty.
        """
        taken = self.counter_pool.take(points)
        return self.counter_pool.remainingCounters == 0

    def check_match_end(self) -> bool:
        """
        Returns True if no counters remain (match over).
        """
        return self.counter_pool.remainingCounters == 0
