import random
from centurion.card import Card, Suit

class Deck:
    def __init__(self, include_jokers: int = 2):
        # Build the standard 52 cards
        self.cards = [
            Card(rank, suit)
            for suit in Suit
            for rank in range(1, 14)
        ]
        # Add the specified number of Jokers (rank=0)
        for _ in range(include_jokers):
            self.cards.append(Card(0, None))

    def shuffle(self) -> None:
        """Randomize the order of cards."""
        random.shuffle(self.cards)

    def deal(self) -> Card:
        """Remove and return the top card."""
        return self.cards.pop(0)

    def has_cards(self) -> bool:
        """Check if any cards remain."""
        return len(self.cards) > 0

