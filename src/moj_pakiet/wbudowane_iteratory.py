"""
Najpierw szukaj iteratorów i obiektów iterowalnych w scope wbudowanym Pythona,
potem w `itertools`, a dopiero na końcu w `more-itertools`.

To zwykle prowadzi do najprostszego i najbardziej standardowego rozwiązania.
"""

# map: leniwie przekształca każdy element wejścia
m = map(lambda x: x * 2, [1, 2, 3, 4, 5])
print(m)
print(list(m))

# filter: leniwie zostawia tylko elementy spełniające warunek
f = filter(lambda x: x > 3, [1, 2, 3, 4, 5])
print(f)
print(list(f))

# zip: leniwie łączy wiele iterowalnych w krotki
z = zip([1, 2, 3], ["a", "b", "c"])
print(z)
print(list(z))

# reversed: zwraca iterator przechodzący po elementach od końca
reverse = reversed([1, 2, 3, 4, 5])
print(reverse)
print(list(reverse))

# enumerate: dodaje indeks do kolejnych elementów
enum = enumerate(["a", "b", "c"])   
print(enum)
print(list(enum))

# range: reprezentuje sekwencję liczb, po której można iterować
range_obj = range(1, 10, 2)
print(range_obj)
print(list(range_obj))

# keys: widok iterowalny po kluczach słownika
# values: widok iterowalny po wartościach słownika
# items: widok iterowalny po parach klucz-wartość
d = {"a": 1, "b": 2, "c": 3}
print(d.keys())
print(d.values())
print(d.items())

import itertools

x = 'abcdefgh'
# batched: grupuje elementy w kolejne porcje o zadanym rozmiarze
print(list(itertools.batched(x, 3)))

x1 = 'abc'
x2 = 'def'
# chain: spłaszcza kilka iterowalnych w jeden ciąg elementów
print(list(itertools.chain(x1, x2)))

y = [x1, x2]
# chain.from_iterable: spłaszcza iterowalny zawierający iterowalne
print(list(itertools.chain.from_iterable(y)))

# pairwise: zwraca kolejne sąsiadujące pary elementów
print(list(itertools.pairwise(x)))

# more-itertools: sięgaj tu dopiero, gdy builtins i itertools nie wystarczą
# np. przed 3.10 często używane było windowed
