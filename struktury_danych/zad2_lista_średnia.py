b = 4
lista = []

while len(lista) <= b:
    pyt = int(input('Podaj liczbę: '))
    lista.append(pyt)
print(sum(lista)/len(lista))