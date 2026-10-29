import pytest
from app import calculate_total
def test_calculate_total_with_discount():
    assert calculate_total(100.0, 2, 10.0) == 180.0
def test_calculate_total_zero_discount():
    assert calculate_total(50.0, 1, 0.0) == 50.0
