import pytest
from centurion.score import Score

def test_compute_base_only():
    s = Score()
    assert s.computeBase(9) == 9
    assert s.basePoints == 9

@pytest.mark.parametrize("total,expected", [
    ( 90, 0),   # under 100 → no penalty
    (100, 0),   # exactly 100 → no penalty
    (105, 0),   # 105 → floor(5/10)=0
    (111, 1),   # 111 → floor(11/10)=1
    (130, 3),   # 130 → floor(30/10)=3
])
def test_compute_penalty(total, expected):
    s = Score()
    assert s.computePenalty(total) == expected

def test_compute_final_points():
    s = Score()
    s.computeBase(9)
    s.computePenalty(130)
    assert s.computeFinal() == 6  # 9 – 3 = 6
    assert s.finalPoints == 6
