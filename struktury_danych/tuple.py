# tupla lub krotka to struktura która przechowuje więcej niż 1 wartość na raz

zmienna = (1,2,3,4)

print(zmienna)

a = ('dasda', 'dasda', 3.4)

b = ('1', 'dasda', 3.4, 'dsad',6,7,8,9)

print(a,b)


print(len(a))
print(a[1])

c = 0
while c < len(b):
    print(b[c])
    c += 1

print ('+++++++++++++++++++++++++++++++++++++++++++')

print (b[1:5])

print (b[1:])
print (b[:4])

print(b[1:6:2]) # od 1 do 6, ale co drugi
print(b[::2])   # z całej tupli ale co drugi
print(b[:-1])   # od początku do przedostatniego
print(b[-3:])   # 3 ostatnie

print(b[1:-1]) # bez krańców
print(b[::-1]) # wszystkie wypisane od tyłu


