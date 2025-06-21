from enum import Enum

class Suit(Enum):
    SPADES   = 1
    HEARTS   = 2
    CLUBS    = 3
    DIAMONDS = 4

class Card:
    def __init__(self, rank: int, suit: Suit = None):
        self.rank = rank
        self.suit = suit

    def is_joker(self) -> bool:
        return self.rank == 0

    def value(self) -> int:
        if self.is_joker() or self.suit is None:
            return 0
        return self.rank * self.suit.value
