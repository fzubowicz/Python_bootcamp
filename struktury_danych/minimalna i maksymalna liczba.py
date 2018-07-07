
komunikat = 'Podaj kolejną liczbę lub wpisz [koniec]'
res = input(komunikat)
min = ''
max = ''

while res != 'koniec':
    res = int(res)
    if min == '' and max == '':
        max = res
        min = res
    elif res < min:
        min = res
    elif res > max:
        max = res
    res = input(komunikat)


print(f'max to {max}, min to {min}')

