# liczba1 = int(input('Podaj 1 liczbę: '))
# liczba2 = int(input('Podaj 2 liczbę: '))
# znak = input('Podaj rodzaj operacji: ')

#
# if znak == '+':
#     print(liczba1 + liczba2)
# elif znak == '-':
#     print(liczba1 - liczba2)
# elif znak == '*':
#     print(liczba1 * liczba2)
# elif znak == '/' and liczba2 != 0:
#     print(liczba1 / liczba2)
# else:
#     print('Błąd')
#

# wersja 2

liczba1 = int(input('Podaj 1 liczbę: '))
liczba2 = int(input('Podaj 2 liczbę: '))
znak = input('Podaj rodzaj operacji: ')


if znak == '+':
    wynik = liczba1 + liczba2
elif znak == '-':
    wynik = liczba1 - liczba2
elif znak == '*':
    wynik = liczba1 * liczba2
elif znak == '/':
    if liczba2 == 0:
        exit('Nie wolno dzielić przez 0')
    wynik = liczba1 / liczba2
else:
    exit('nieznana operacja')
print(wynik)
