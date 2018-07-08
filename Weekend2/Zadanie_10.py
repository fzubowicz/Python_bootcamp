# napisz program zaliczający liczbę wystąpień każego znaku w podanym przez użytkowanika napisie

# slownik = {
#     'a': 0,
#     'b': 0,
#     'c': 0,
#     'd': 0,
#     'e': 0,
#     'f': 0,
#     'g': 0,
#     'h': 0,
#     'i': 0,
#     'j': 0,
#     'k': 0,
#     'l': 0,
#     'm': 0,
#     'n': 0,
#     'o': 0,
#     'p': 0,
#     'r': 0,
#     's': 0,
#     't': 0,
#     'u': 0,
#     'w': 0,
#     'x': 0,
#     'y': 0,
#     'z': 0,
#     'v': 0,
#     'q': 0
#
# }
#
# prompt = input('Podaj słowo')
#
# for x in prompt:
#     slownik[x] += 1
#
# print(slownik)


###### drugi sposób

# prompt = input('Podaj słowo')
# slownik = {}
#
#
# for x in prompt:
#     slownik[x] = slownik.get(x, 0) + 1


############# 3 rozwiązanie

prompt = input('Podaj słowo')
slownik = {}

for x in prompt:
    if x in slownik:
        slownik[x] += 1
    else:
        slownik[x] = 1

print(slownik)

