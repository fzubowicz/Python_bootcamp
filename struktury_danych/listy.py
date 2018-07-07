#lista to struktura podobna do tupla, ale mogę ją modyfikować

lista = [1,2,3,4,5,6,7]

print(len(lista))
print(lista[0])

lista.append('ala')


lista.insert(3, 'kot')
lista.insert(-1, 'test')


print(lista)


lista[3] = 'tu był czwarty elemnet'


lista[3:7] = []




print(lista)

