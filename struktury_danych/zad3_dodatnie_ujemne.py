lista = [1,2,3,4,5,-1,-2,-3,-4,-5, -7]

ujemne = 0
dodatnie = 0

for el in lista:
    if el < 0:
        ujemne += 1
    if el >= 0:
        dodatnie += 1

print(ujemne,dodatnie)