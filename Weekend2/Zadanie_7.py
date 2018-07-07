napis = input("Podaj napis: ")

a = napis.count("a")
e = napis.count("e")
i = napis.count("i")
o = napis.count("o")
u = napis.count("u")
y = napis.count("y")

print(f'Wszystkich samogłosek jest: {a + e + i + o + u +y}. Z czego występuje:\n'
      f'a {a} razy\n'
      f'e {e} razy\n'
      f'i {i} razy\n'
      f'o {o} razy\n'
      f'u {u} razy\n'
      f'y {y} razy\n')

