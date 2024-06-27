import pytest
from calc.operations import add, subtract, multiply, divide

def test_add():
    # Teste l'addition de deux nombres positifs
    assert add(2, 3) == 5
    # Teste l'addition d'un nombre négatif et d'un nombre positif
    assert add(-1, 1) == 0
    # Teste l'addition de deux zéros
    assert add(0, 0) == 0

def test_subtract():
    # Teste la soustraction de deux nombres positifs
    assert subtract(3, 2) == 1
    # Teste la soustraction où le premier nombre est plus petit
    assert subtract(2, 3) == -1
    # Teste la soustraction de deux zéros
    assert subtract(0, 0) == 0

def test_multiply():
    # Teste la multiplication de deux nombres positifs
    assert multiply(2, 3) == 6
    # Teste la multiplication d'un nombre négatif et d'un nombre positif
    assert multiply(-1, 1) == -1
    # Teste la multiplication d'un nombre par zéro
    assert multiply(0, 5) == 0

def test_divide():
    # Teste la division de deux nombres positifs
    assert divide(6, 3) == 2
    # Teste la division d'un nombre négatif par un nombre positif
    assert divide(-4, 2) == -2
    # Teste la division qui ne donne pas un entier
    assert divide(5, 2) == 2.5

    # Teste la division par zéro et vérifie qu'une exception est levée
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
