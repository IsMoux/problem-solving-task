import pytest

class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap



@CacheDecorator()
def concatener(a, b, sep=" "):
    return f"{a}{sep}{b}"


@CacheDecorator()
def ajouter(a, b):
    return a + b

@CacheDecorator()
def multiplier(a, b):
    return a * b

def test_concatener_caching():
    #passe
    assert concatener("issam", "hadjallah") == "issam hadjallah"
    #ne passe pas
    assert concatener("hello", "issam") == "issam hadjallah"

def test_ajouter_caching():
    #passe
    assert ajouter(3, 3) == 6
    #ne passe pas
    assert ajouter(3, 3) == 3

def test_multiplier_caching():
    #passe 
    assert multiplier(3, 4) == 12
    # ne passe pas
    assert multiplier(3, 4) == 6


def tester_different_argument():
    #peux passer
    assert ajouter(2, 3) == 5
    #ne passe pas
    assert ajouter(2, 4) == 5
    # peux passer
    assert multiplier(2, 2) == 4
    # ne passe pas
    assert multiplier(3, 4) == 4

def test_cache():
    #passe 
    assert ajouter(5, 5) == 10
    assert ajouter(5, 5) == 10  
    #ne passe pas
    assert ajouter(5, 6) == 10


