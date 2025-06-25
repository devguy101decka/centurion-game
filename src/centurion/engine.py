from centurion.deck import Deck
from centurion.card import Card
from centurion.counterpool import CounterPool
from typing import List

class GameEngine:
    def __init__(self, counters: int = 21, include_jokers: int = 2):
        # remember include_jokers so we can reset the deck later
        self.include_jokers = include_jokers

        # build & shuffle first deck
        self.deck = Deck(include_jokers)
        self.counter_pool = CounterPool(counters)

        # each player’s hand, running total, whose turn
        self.players: List[List[Card]] = [[], []]
        self.running_total: int = 0
        self.current_player: int = 0

    def start_match(self) -> None:
        """Reset deck, shuffle, deal 7 cards each, reset total & turn."""
        self.deck = Deck(self.include_jokers)
        self.deck.shuffle()
        self.players = [[], []]
        self.running_total = 0
        self.current_player = 0

        for _ in range(7):
            self.players[0].append(self.deck.deal())
            self.players[1].append(self.deck.deal())

    def play_turn(self, player_index: int, card_index: int) -> int:
        """Player plays a card; update total & switch turn."""
        card = self.players[player_index].pop(card_index)
        self.running_total += card.value()
        self.current_player = 1 - player_index
        return self.running_total

    def check_deal_end(self) -> bool:
        """
        Deal ends if:
          1) total == 100
          2) total > 100 and a multiple of 10
          3) both hands empty
        """
        if self.running_total == 100:
            return True
        if self.running_total > 100 and self.running_total % 10 == 0:
            return True
        if all(len(h)==0 for h in self.players):
            return True
        return False

    def award_counters(self, player_index: int, points: int) -> bool:
        """
        Player takes counters equal to points.
        Returns True if the pool is now empty (match over).
        """
        self.counter_pool.take(points)
        return self.counter_pool.remainingCounters == 0

    def check_match_end(self) -> bool:
        """Match ends when no counters remain."""
        return self.counter_pool.remainingCounters == 0
