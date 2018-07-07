# a = 1
# b = 0
# while a <= 7:
#     temp = int(input(f'Podaj temperaturę dnia {a}: '))
#     b += temp
#     a += 1
#
# print(round(b/(a-1), 1))


# alternatywnie
ile_dni = 7
a = 1
temp = 0
while a <= ile_dni:
    temp += int(input(f'Podaj temperaturę dnia {a}: '))
    a += 1

print(round(temp/(a-1), 1))