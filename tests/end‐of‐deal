import pytest
from centurion.engine import GameEngine
from centurion.card import Card, Suit

@pytest.fixture
def engine():
    eng = GameEngine(include_jokers=0)
    # stub out hands so we can control them
    eng.players = [[Card(1, Suit.SPADES)], [Card(2, Suit.HEARTS)]]
    return eng

def test_exact_100_ends(engine):
    engine.running_total = 100
    assert engine.check_deal_end() is True

def test_overshoot_multiple_of_10_ends(engine):
    engine.running_total = 120
    assert engine.check_deal_end() is True

def test_no_cards_left_ends(engine):
    engine.running_total = 50
    engine.players = [[], []]
    assert engine.check_deal_end() is True

def test_midgame_does_not_end(engine):
    engine.running_total = 55
    # both players still have cards from the fixture
    assert engine.check_deal_end() is False
