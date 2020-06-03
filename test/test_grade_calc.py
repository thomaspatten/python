from grade_calc import grade_calc
import pytest

def test_a():
    assert grade_calc(70, 70, 70) == ('a')
    assert grade_calc(75,72,82)==('a')

def test_b():
    assert grade_calc(60, 60, 60) == ('b')
    assert grade_calc(69,70,70) ==('b')
def test_c():
    assert grade_calc(50,50,50)==('c')
    assert grade_calc(59,60,60)==('c')
def test_d():
    assert grade_calc(40,40,40)==('d')
    assert grade_calc(22,1,5)==('d')
