import pytest
from zad1 import is_palindrome

def test_answer():
    assert is_palindrome("kajak")
    assert is_palindrome("Kobyła ma mały bok")