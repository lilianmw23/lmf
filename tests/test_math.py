import pytest

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 1 - 1 == 0

@pytest.mark.parametrize("a,b,expected", [(0, 5, 0), (1, 5, 5), (2, 5, 10), (-3, 5, -15), (-5, -5, 25)])
def test_multipication(a, b, expected):
    assert a * b == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        1 / 0