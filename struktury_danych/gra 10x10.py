import random


gracz_x = random.randrange(1,11)
gracz_y = random.randrange(1,11)

skarb_x = random.randrange(1,10)
skarb_y = random.randrange(1,10)

print(f'Debug: gracz x: {gracz_x}, y: {gracz_y}')
print(f'Debug: skarb x: {skarb_x}, y: {skarb_y}')

krok = print(f'Podaj w którą stronę idziesz:\n'
             f'[l]ewo\n'
             f'[p]rawo\n'
             f'[g]óra\n'
             f'[d]ół\n'
             f'Wyjdziesz za planszę to zginiesz')


while True:
    print(f'Debug: gracz x: {gracz_x}, y: {gracz_y}')
    print(f'Debug: skarb x: {skarb_x}, y: {skarb_y}')
    krok = input('Gdzie idziesz?')
    p_gracz_x = gracz_x
    p_gracz_y = gracz_y

    if krok == 'l':
        gracz_x -= 1
    if krok == 'p':
        gracz_x += 1
    if krok == 'g':
        gracz_y -= 1
    if krok == 'd':
        gracz_y += 1


    if not (0 < gracz_x < 11 and 0 < gracz_y < 11):
        exit('Wyszedłeś poza planszę')

    if gracz_x == skarb_x and gracz_y == skarb_y:
        break

    if abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y) < abs(p_gracz_x - skarb_x) + abs(p_gracz_y - skarb_y):
        print('Ciepło')
    else:
        print('Zimno')



    print(f'Twoja aktualna pozycja to: x: {gracz_x}, y: {gracz_y} ')



print('Brawo! Znalazłeś skarb')





