liczba = int(input(f'Podaj liczba: '))

print(f'Liczba jest podzielna przez 2, 3 oraz większa niż 10 lub jest to liczba 7 {(liczba%2 ==0 and liczba%3 ==0 and liczba > 10) or liczba == 7}')


