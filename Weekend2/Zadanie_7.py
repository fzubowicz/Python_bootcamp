napis = input("Podaj napis: ")

a = napis.lower().count("a")
e = napis.lower().count("e")
i = napis.lower().count("i")
o = napis.lower().count("o")
u = napis.lower().count("u")
y = napis.lower().count("y")

print(f'Wszystkich samogłosek jest: {a + e + i + o + u +y}. Z czego występuje:\n'
      f'a {a} razy\n'
      f'e {e} razy\n'
      f'i {i} razy\n'
      f'o {o} razy\n'
      f'u {u} razy\n'
      f'y {y} razy\n')

################# aletrnatywne rozwiązanie

# text = input("Podaj tekst")
#
# SAMOGLOSKI = "aeiouy"
# ile_samoglosek = 0
#
# for znak in text:
#     if znak.lower() in SAMOGLOSKI:
#         ile_samoglosek += 1
#
# print(ile_samoglosek)


############## alternatywnie
SAMOGLOSKI = "aeiouy"
ile_samoglosek = 0

for s in SAMOGLOSKI:
    ile_samoglosek += napis.lower().count(s)
