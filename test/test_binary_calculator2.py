from binary_calculator2 import binarycalc
import pytest

def test_addition():
    assert binarycalc(4, 2, "+") == [1, 1, 0]

def test_subtraction():
    assert binarycalc(4, 2, "-") == [1, 0]

def test_multiplication():
    assert binarycalc(4, 2, "*") == [1, 0, 0, 0]

def test_division():
    assert binarycalc(4, 2, "/") == [1, 0]
