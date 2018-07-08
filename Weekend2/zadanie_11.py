numbers = set()

while True:
    user = input('Wpisz liczbę lub [end]')

    if user == 'end':
        break
    else:
        numbers = int(user)
        numbers.add(numbers)


print(f'Wprowadzono unikalnych liczb: {len(numbers)}')

liczby_parzyste = set(range(0,101, 1))






