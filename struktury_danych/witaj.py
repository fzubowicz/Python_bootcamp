print ('Hello world!')


# int - liczba całkowita

a = 3
b = 4

asdfad = 8


# float - liczba ułamkowa

ulamek = 4.5
inne_opcje = .3
test = 3.

print (test)
print (inne_opcje)
print (ulamek)

print(3/15)
print(0.2)

# błędne rozwinięcie
print(0.1 + 0.2)


# napisy
napis1 = "ala ma kota"
napis2 = 'ala ma kota'

print(napis1 == napis2)

prawda = True
falsz = False



a = ""
if a:
    print('prawda')
else:
    print('falsz')



#wzory
pi = 3.14
pole_trojkata = 10 * 5/2
pole_kola = 3.14 * 7**2
pole_trapezu = (3+9) * 6.5 /2
objetosc_kuli = 4/3 * 3.14 * (7/8)**3

# print(pole_trojkata)
# print(pole_kola)
# print(pole_trapezu)
# print(objetosc_kuli)


# na zmiennych
h_troj = 10
pod_troj = 5
pole_trojkata = h_troj * pod_troj/2

r_k = 7
pole_kola = pi * r_k**2

podst = 3+9
h_trap = 6.5
pole_trapezu = podst * h_trap /2

r_kula = 7/8
objetosc_kuli = 4/3 * pi * r_kula**3


print(pole_trojkata)
print(pole_kola)
print(pole_trapezu)
print(objetosc_kuli)


imie = 'Filip'
wzrost = 190

print('imie:',imie,', a wzrost', wzrost )
print(f'imie: {imie},\na wzrost {wzrost}')


# zadanie 4

cena = 10.
waga = 2.5

# .2f - dwa miejsca po przecinku, \t tabulator
# < wyrównaj do lewej
# <10 wyrównaj do lewej w obrębie 10 znaków
# ^ wyrównaj do środka
# > wyrównaj do prawej
print(f'''
Cena za kg: \f{cena}  
Waga: \t\t  {waga} 
Koszt: \t\t  {waga * cena}''')

# alternatywnie
print(f'\n{"Cena:":<8} {cena:>5.2f} \n'
      f'{"Waga:":<8} {waga:>5.2f} \n'
      f'{"Koszt:":<8} {waga*cena:>5.2f}')


input()