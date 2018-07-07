x = int(input('Podaj x: '))
y = int(input('Podaj y: '))



if x <= 10:
    if y <= 10:
        print('Lewy górny róg')
    elif y > 10 and y < 90:
        print('Lewy margines')
    elif y >= 90:
        print('Lewy dolny róg')
elif x > 10 and x < 90:
    if y <= 10:
        print('Gorny margines')
    elif y >= 90:
        print('Dolny margines')
    elif y > 10 and y < 90:
        print('Środek')
elif x >= 90:
    if y <= 10:
        print('Prawy górny róg')
    elif y > 10 and y < 90:
        print('prawy margines')
    elif y >= 90:
        print('prawy dolny róg')
else:
    print('Poza planszą lub błąd')



## alternatywnie

#x = int(input('Podaj x: '))
#y = int(input('Podaj y: '))

if x <= 10:
    pos_x = 'left'
elif x >= 90:
    pos_x = 'right'
else:
    pos_x = ''

if y <= 10:
    pos_y = 'top'
elif y >= 90:
    pos_y = 'bottom'
else:
    pos_y = ''

# oba wypełnione
if pos_x and pos_y:
    print(pos_x, pos_y, 'corner')
#tylko jeden wypełniony
elif pos_x or pos_y:
    print(pos_x, pos_y, 'edge')
else:
# oba puste
    print('center')



