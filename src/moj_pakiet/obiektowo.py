"""
Krotka demonstracja podstaw programowania obiektowego w Pythonie.

Modul pokazuje kilka bardzo prostych elementow modelu obiektowego:

- definicje klasy i tworzenie instancji,
- atrybut klasowy wspoldzielony przez wszystkie obiekty,
- dziedziczenie przez klase potomna,
- ograniczanie atrybutow instancji przez `__slots__`.

Przyklad klasy `Czlowiek` jest z zalozenia minimalny. Chodzi tu nie
o realizm modelu, tylko o pokazanie skladni `class`, konstruktora
`__init__`, przypisania `self._imie` oraz dostepu do atrybutow
instancji i klasy.

Klasa `A` dziedziczy po `Czlowiek`, dzieki czemu mozna omowic
najprostszy wariant relacji "jest odmiana". To dobra okazja do
pokazania, ze obiekt potomny widzi elementy z klasy bazowej i moze
uzywac ich bez ponownej definicji.

Najwazniejsze elementy skladni to:

- `class Nazwa:`,
- `class Potomna(Bazowa):`,
- metoda `__init__`,
- `self.atr = ...`,
- `__slots__ = [...]` jako ograniczenie zestawu dozwolonych atrybutow.

To modul startowy do dalszych rozmow o enkapsulacji, dziedziczeniu,
metodach instancji i kontrolowanym dostepie do danych obiektu.
"""

class Czlowiek:
    __slots__ = ["_imie"]
    atr_klasowy = 123

    # __slots__ = ['imie']
    def __init__(self, imie):
        self._imie = imie

class A(Czlowiek):
    def m1(self):
        print(self._imie)

if __name__ == "__main__":
    c1 = Czlowiek("Jan")
    c2 = Czlowiek("Zosia")
    c1._imie = 'Ola'
    print(c1._imie)
