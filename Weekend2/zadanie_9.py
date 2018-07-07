dictionary_products = {'jablka': 3.2, "gruszki": 4, "ziemniaki":2, "sliwki": 1.2}
dictionary_amount = {'jablka': 100, "gruszki": 20, "ziemniaki":500, "sliwki": 5}




end_ = ""
mark_ = False


while end_ != "end":
    print("W sklepie są dostępne produkty:")
    for k, v in dictionary_products.items():
        print(f' - {k} w cenie: {v}. Ilość na magazynie: {dictionary_amount[k]}')

    buy_sell = input('Chcesz [k]upić czy [s]przedać?')
    if buy_sell == "k":

        product = input("Jaki produkt wybierasz? ")
        amount = float(input("Ile chcesz kupić kg? "))

        if dictionary_amount[product] > amount and buy_sell == "k":

            print(f'Kupujesz {product} w cenie za kg wynoszącą {dictionary_products[product]}. Musisz zaplacić {amount * dictionary_products[product]}')
            dictionary_amount[product] -= amount
        elif buy_sell == "k" and dictionary_amount[product] < amount :
            print("Nie możesz tyle kupić. Brak takiej ilości w magazynie")

    if buy_sell == 's':
        product = input("Jaki produkt chcesz sprzedać? ")
        amount = float(input("Ile chcesz sprzedać kg? "))
        for k, v in dictionary_products.items():
            if k == product:
                dictionary_amount[product] += amount
                mark_ = True
        if mark_ != True:
            price_ = input("Jaka ma być cena produktu?")
            dictionary_products[product] = amount
            dictionary_amount[product] = price_

    end_ = input("Czy masz coś jeszcze do załatwienia? Jeśli nie wpisz [end]")


print("Dziękujemy za wybranie naszego sklepu")