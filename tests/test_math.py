from src.math import add


def test_add_simple():
    assert 2 == add(1, 1)


def add_negative():
    assert 2 == add(4, -2)
