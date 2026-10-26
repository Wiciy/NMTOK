import pytest
from Zadania import fibonacci, is_palindrome

#Test dla is_palindrome
def test_is_palindrome_kajak():
    assert is_palindrome("kajak") is True

def test_is_palindrome_zdanie_ze_spacjami():
    assert is_palindrome("Kobyła ma mały bok") is True

def test_is_palindrome_python():
    assert is_palindrome("python") is False

def test_is_palindrome_pusty_ciag():
    assert is_palindrome("") is True

def test_is_palindrome_pojedynczy_znak():
    assert is_palindrome("A") is True

#Test dla fibonacci
def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_jeden():
    assert fibonacci(1) == 1


def test_fibonacci_piec():
    assert fibonacci(5) == 5


def test_fibonacci_dziesiec():
    assert fibonacci(10) == 55


def test_fibonacci_liczba_ujemna():
    with pytest.raises(ValueError):
        fibonacci(-1)