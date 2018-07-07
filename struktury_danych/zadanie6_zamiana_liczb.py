lista = [1, 2, 3, 4, 5, 100, 0, -11]

min_ = lista[0]
max_ = lista[0]

for x in lista:
    if x >= max_:
        max_ = x
    if x <= min_:
        min_ = x

nr_max = lista.index(max_)
nr_min = lista.index(min_)

lista[nr_min] = max_
lista[nr_max] = min_


max_.isdigit()
