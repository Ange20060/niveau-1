from calculatrice import calculer


def test_addition():
    assert calculer(2, 3, "+") == 5


def test_soustraction():
    assert calculer(10, 4, "-") == 6


def test_multiplication():
    assert calculer(3, 4, "*") == 12


def test_division():
    assert calculer(10, 2, "/") == 5
