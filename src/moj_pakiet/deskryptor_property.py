"""
Demonstracja `property` jako najwygodniejszej, wbudowanej postaci
deskryptora w Pythonie.

Intencja tego modulu jest pokazanie dwoch rownowaznych sposobow
tworzenia wlasciwosci:

- przez jawne wywolanie `property(fget=..., fset=...)`,
- przez skladnie dekoratorowa `@property` i `@nazwa.setter`.

Przyklad wykorzystuje klase `Czlowiek`, w ktorej logiczny atrybut
`imie_nazwisko` nie musi byc przechowywany jako jeden napis. Getter
i setter pozwalaja ukryc wewnetrzna reprezentacje oparta o dwa pola:
`_imie` oraz `_nazwisko`, a jednoczesnie wystawic wygodny interfejs
na zewnatrz.

Modul pokazuje tez wariant property tylko do odczytu. Wlasciwosc
`nazwisko_imie` ma wyłącznie getter, co oznacza, ze mozna pobierac
jej wartosc, ale nie mozna ustawic jej bezposrednio z zewnatrz.

Najwazniejsze mechanizmy i elementy skladni to:

- atrybut prywatny umowny z podkresleniem,
- `property`, `@property` i `@imie_nazwisko.setter`,
- `__slots__` ograniczajace zestaw atrybutow instancji,
- kod wykonywany przy odczycie i zapisie atrybutu mimo skladni
  wygladajacej jak zwykly dostep do pola.

To dobry modul do omowienia przejscia od prostych atrybutow do
kontrolowanego API obiektu bez zmiany skladni po stronie uzytkownika.
"""

class Czlowiek:
    __slots__ = [
        # 'imie_nazwisko',
        '_imie',
        '_nazwisko'
    ]

    def _set_imie_nazwisko(self, imie_nazwisko):
        print(f'set {imie_nazwisko}')
        self._imie, self._nazwisko = imie_nazwisko.split()

    def _get_imie_nazwisko(self):
        print(f'get')
        return f'{self._imie} {self._nazwisko}'

    imie_nazwisko = property(fget=_get_imie_nazwisko, fset=_set_imie_nazwisko)

    def __init__(self, imie_nazwisko) -> None:
        self.imie_nazwisko = imie_nazwisko

class Czlowiek:
    __slots__ = [
        # 'imie_nazwisko',
        '_imie',
        '_nazwisko'
    ]

    @property
    def imie_nazwisko(self):
        print(f'get')
        return f'{self._imie} {self._nazwisko}'

    @imie_nazwisko.setter
    def imie_nazwisko(self, imie_nazwisko):
        print(f'set {imie_nazwisko}')
        self._imie, self._nazwisko = imie_nazwisko.split()



    # imie_nazwisko = property(fget=_get_imie_nazwisko, fset=_set_imie_nazwisko)

    # read_only
    @property
    def nazwisko_imie(self):
        return f'{self._nazwisko} {self._imie}'

    def __init__(self, imie_nazwisko) -> None:
        self.imie_nazwisko = imie_nazwisko



if __name__ == "__main__":
    c1 = Czlowiek('Jan Kowalski')
    print(c1.imie_nazwisko)
    c1.imie_nazwisko = 'Jan Nowak'
    print(c1.imie_nazwisko)
    print(c1.nazwisko_imie)
