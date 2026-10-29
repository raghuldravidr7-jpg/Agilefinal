import pytest
from app import calculate_total
def test_calculate_total_positive():
    assert calculate_total(10.0, 2) == 20.0
def test_calculate_total_zero():
    assert calculate_total(5.5, 0) == 0.0
def test_calculate_negative_raises():
    try:
        calculate_total(-5.0, 2)
        assert False, "Expected ValueError"
    except ValueError:
        assert True

