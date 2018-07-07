wysokosc = int(input(f'Wysokość w cm: '))
szerokosc = int(input(f'Szerokość w cm: '))
dlugosc = int(input(f'Długość w cm: '))



print(f'Czy opakowanie jest większe niż 1000cm3? {wysokosc * szerokosc * dlugosc > 1000}, objętość wynosi {wysokosc * szerokosc * dlugosc} cm3')