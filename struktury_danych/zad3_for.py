lista = [1,2,3,4,5,6,7]


for el in lista:
    print(el)

tupla = ('dasda', 'asdasd', 3, 'dasdas')

for el in tupla:
    print(el)

for nr, element in enumerate(tupla, start= 1):
    print(nr, element)

print('=======================================')
for i in range(1,len(tupla),2):
    print(i, tupla[i])


kopia = tupla[-1::-1]
for el in tupla:
    print(el)