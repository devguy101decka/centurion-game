import pytest
from centurion.engine import GameEngine

@pytest.fixture
def engine():
    # start with a pool of 5 counters
    return GameEngine(counters=5, include_jokers=0)

def test_award_counters_and_no_match_end(engine):
    # award 2 counters to player 0
    match_over = engine.award_counters(player_index=0, points=2)
    assert match_over is False
    assert engine.counter_pool.remainingCounters == 3
    assert engine.check_match_end() is False

def test_award_counters_and_match_end(engine):
    # award all remaining counters
    match_over = engine.award_counters(player_index=1, points=5)
    assert match_over is True
    assert engine.counter_pool.remainingCounters == 0
    assert engine.check_match_end() is True
