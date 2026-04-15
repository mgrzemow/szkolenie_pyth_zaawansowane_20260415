x = []
print(type(x))
x = [
    1,
    2.44,
    "mama",
    True,
]

lista_imion = ['ala', 'ola', 'ula']
rekord_danych = ['ola',  34, 'Warszawa', 1.98]

lista_imion.append('tomek')
lista_imion.extend(['jan', 'paweł'])
print(lista_imion)
lista_imion += ['ewa', 'grześ']
print(lista_imion)

import time
import collections
# uwaga na wstawianie w środek
# w praktyce jeżeli użyję listy jako kolejki FIFO
for n in [50_000, 100_000, 200_000]:
    x = collections.deque()
    t1 = time.perf_counter()
    for i in range(n):
        x.insert(0, i)
    print(f'{n}: {time.perf_counter() - t1:.2f}')
    
# unpacking
rekord_danych = ['ola',  34, 'Warszawa', 1.98]
imie = rekord_danych[0]
wiek = rekord_danych[1]
miasto = rekord_danych[2]
wzrost = rekord_danych[3]
imie, wiek, miasto, wzrost = rekord_danych
print(imie, wiek, miasto, wzrost)
# zaawansowane
# co jeżeli ilość elementów jezt zmienna
rekord_danych_2 = ['ola',  34, 'Warszawa', 1.98, 'Polska']
rekord_danych_3 = ['ola',  34, 'Warszawa', 1.98, 'Polska', 'Europa']
lista_rekordow = [rekord_danych,
                  rekord_danych_2,
                  rekord_danych_3]
print(lista_rekordow)
for r in lista_rekordow:
    imie, wiek, miasto, wzrost, *reszta = r
    print(imie, wiek, miasto, wzrost, reszta)

for imie, wiek, miasto, wzrost, *reszta in lista_rekordow:
    print(imie, wiek, miasto, wzrost, reszta)

# konwencyjnie _ oznacza że wartość mnie nie interesuje
for imie, _, miasto, _, *_ in lista_rekordow:
    print(imie, miasto)

r = ['Jan', 'Nopwak', ['Kraków', 'Długa', 51]]
imie, nazw, (miasto, ulica, nr) = r

# unpacking działa między krotkami i listami

# krotki
# niemutowalne
# trochę wydajniejsze
x = (1,2,3)
print(type(x))
# jednoelementowa krotka
x = (9,)
print(x)
# UWAGA  cała ktorka jest niemutopwalna, ale elementy krotki już niekoniecznie
# zły zwyczaj - nie robić tak, bo to mylące
k = ([],[])
k[0].append(1)
k[0].append(2)
k[0].append(3)
print(k)
# tam gdzie jest to jednoznaczne, można pominąć ()
k = 1,2,3
print(k, type(k))