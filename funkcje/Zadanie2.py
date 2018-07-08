def more_than(napis, prog):
    wynik = set()
    for letter in napis:
        if napis.count(letter) > prog:
            wynik.add(letter)

    return wynik


def test_more_than():
    assert more_than('ala ma kota a kot ma ale', 3) == {'a', ' '}
