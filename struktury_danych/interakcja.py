# imie = input('Wpisz swoje imię: ')
#
# print('Witaj: ', imie)
#
# wiek = int(input('Podaj swój wiek: '))
#
# print('Wiek za dwa lata: ', wiek + 2)
#
#
#
#
#
# if wiek >= 18:
#     print('Zapraszamy')
# else:
#     print('Jeszcze nie')
#



miasto_a = input('Podaj nazwę miasta początkowego: ')
miasto_b = input('Podaj nazwę miasta końcowego: ')
dystans = float(input('Podaj dystans: '))
cena_paliwa = float(input('Cena paliwa: '))
spalanie = float(input('Podaj spalanie na 100km: '))

print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {dystans * spalanie * cena_paliwa / 100: .2f} PLN' )
print(f'Koszt przejazdu {miasto_a}-{miasto_b} to {round(dystans * spalanie * cena_paliwa / 100,2)} PLN' )






print('Koniec programu')