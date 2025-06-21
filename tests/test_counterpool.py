import pytest
from centurion.counterpool import CounterPool

def test_counterpool_take_less():
    pool = CounterPool(10)
    assert pool.take(4) == 4
    assert pool.remainingCounters == 6

def test_counterpool_take_exact():
    pool = CounterPool(5)
    assert pool.take(5) == 5
    assert pool.remainingCounters == 0

def test_counterpool_take_more_than_available():
    pool = CounterPool(3)
    assert pool.take(7) == 3
    assert pool.remainingCounters == 0
