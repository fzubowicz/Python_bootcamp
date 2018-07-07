wiek = int(input('Podaj rok urodzenia: '))


import datetime

if datetime.datetime.now().year - wiek >= 18:
    print('Pełnoletni')
else:
    print('Niepełnoletni')


