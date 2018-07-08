def czy_jest_pierwsza(a):
    for i in range(2, a):
        if a%i == 0:
            return False

    return True


def test_czy_pierwsza_dla_liczby_pierwszej():
    assert czy_jest_pierwsza(11) == True
    assert czy_jest_pierwsza(11) == True
    assert czy_jest_pierwsza(13) == True

def test_czy_pierwsza_dla_liczby_niepierwszej():
    assert czy_jest_pierwsza(4) == False
    assert czy_jest_pierwsza(15) == False

