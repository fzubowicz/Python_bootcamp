dictionary_products = {'jablka': 3.2, "gruszki": 4, "ziemniaki":2, "sliwki": 1.2}
dictionary_amount = {'jablka': 100, "gruszki": 20, "ziemniaki":500, "sliwki": 5}

product = input("Jaki produkt wybierasz? ")
ilosc = float(input("Ile chcesz kupic kg? "))


if dictionary_amount[product] > ilosc:
    print(f'Kupujesz {product} w cenie za kg wynoszącą {dictionary_products[product]}. Musisz zaplacić {ilosc * dictionary_products[product]}')
    dictionary_amount[product] -= ilosc
else:
    print("Nie możesz tyle kupić. Brak takiej ilości w magazynie")

print(dictionary_amount)