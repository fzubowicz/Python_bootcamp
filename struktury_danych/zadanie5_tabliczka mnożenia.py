print(' ', end = ' ')
for x in range(10):
    print(f'{x: >2}', end=' ')
print()

for el in range(10):
    print(el, end = ' ')
    for al in range(10):
        print(f'{el*al: >2}', end = ' ')
    print()

