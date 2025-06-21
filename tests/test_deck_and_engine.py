import pytest
from centurion.engine import GameEngine
from centurion.deck import Deck

def test_start_match_deals_7_each():
    engine = GameEngine(include_jokers=0)
    engine.start_match()
    # Each player has 7 cards
    assert len(engine.players[0]) == 7
    assert len(engine.players[1]) == 7
    # Deck size is reduced by 14
    assert len(engine.deck.cards) == 52 - 14

def test_deck_has_cards_and_deal():
    deck = Deck(include_jokers=0)
    assert deck.has_cards() is True
    # After dealing one, size should drop by 1
    top = deck.deal()
    assert isinstance(top, object)
    assert len(deck.cards) == 52 - 1
