from odd_even import even 
import pytest

def test_even():
    assert even(10)==True

def test_odd():
    assert even(7)==False