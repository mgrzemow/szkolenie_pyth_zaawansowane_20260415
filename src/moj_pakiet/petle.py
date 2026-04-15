# operator walrus :=

# while (imie := input('Podaj imie: ')) != 'koniec':
#     print(f'Cześć {imie}')

r = 10
h = 10
v = (s := 3.14 * r * r) * h
print(s, v)

# for - czyli dla wszystkich elementów czegoś
for znak in 'abc':
    print(znak)

for liczba in [1,2,3,4,5]:
    print(liczba)

with open('venv/liczby.py', 'rt', encoding='utf8') as f:
    for linia in f:
        print(repr(linia))