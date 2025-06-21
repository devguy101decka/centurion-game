import pytest
from centurion.card import Card, Suit

def test_joker_value():
    joker = Card(0, None)
    assert joker.is_joker() is True
    assert joker.value() == 0

@pytest.mark.parametrize("rank,suit,expected", [
    (1, Suit.SPADES,    1*1),
    (13, Suit.DIAMONDS, 13*4),
    (5, Suit.CLUBS,     5*3),
])
def test_value_non_joker(rank, suit, expected):
    card = Card(rank, suit)
    assert card.is_joker() is False
    assert card.value() == expected
