
komunikat = 'Podaj kolejną liczbę lub wpisz [koniec]'
res = input(komunikat)

# najpierw obsłużwyjątkowe sytuacje
if res == 'koniec':
    exit('Nie wyrałeś żadnej liczby')


liczba = int(res)
min = liczba
max = liczba

while True:
    res = input(komunikat)
    if res == 'koniec':
        break

    liczba = int(res)
    if liczba > max:
        max = liczba
    if liczba < min:
        min = liczba

print( max, 'fddfsd',  min)