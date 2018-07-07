text = input('Podaj napis: ')

x = text.find(">")
y = text.find("<")


print(f'Pomiędz <> jest {x - y - 1}')


count_ = 0
mark_ = False
count_amount = 0

text = input('Podaj napis: ')


for x in text:
    if x == "<":
        mark_ = True
        count_amount += 1
    elif x == ">":
        mark_ = False

    if mark_:
        count_ += 1

print(count_ - count_amount)
