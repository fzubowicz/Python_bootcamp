import random


gracz_x = random.randrange(1,11)
gracz_y = random.randrange(1,11)

skarb_x = random.randrange(1,11)
skarb_y = random.randrange(1,11)

krok = print(f'Podaj w którą stronę idziesz:\n'
             f'[l]ewo\n'
             f'[p]rawo\n'
             f'[g]óra\n'
             f'[d]ół\n'
             f'Wyjdziesz za planszę to zginiesz')

a = 1
while True:

    while a < 5:
        print(f'Pozycja gracza x: {gracz_x}, y: {gracz_y}')
        krok = input('Gdzie idziesz? ')
        p_gracz_x = gracz_x
        p_gracz_y = gracz_y

        if gracz_x == skarb_x and gracz_y == skarb_y:
            break

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

        wskazowka = random.randrange(1,6)
        if wskazowka != 1:
            if abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y) < abs(p_gracz_x - skarb_x) + abs(p_gracz_y - skarb_y):
                print('Ciepło')
            else:
                print('Zimno')


        a += 1
    skarb_x = random.randrange(1, 11)
    skarb_y = random.randrange(1, 11)
    print('Skarb się przemieścił')
    a = 1



    #print(f'Twoja aktualna pozycja to: x: {gracz_x}, y: {gracz_y} ')



print('Brawo! Znalazłeś skarb')



