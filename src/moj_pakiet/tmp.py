"""
Roboczy modul porownujacy dwa sposoby uzyskania "leniwie liczonego"
atrybutu w obiekcie.

Plik ma charakter eksperymentalny i zestawia dwa podejscia do podobnego
problemu:

- reczne cache'owanie wyniku wewnatrz `property`,
- wykorzystanie `functools.lru_cache` razem z `property`.

Pierwsza wersja klasy `A` pokazuje klasyczny wzorzec:
przy pierwszym odczycie sprawdzamy, czy instancja ma juz ukryty atrybut,
a jesli nie - obliczamy wartosc, zapisujemy ja i zwracamy. To jest
reczne memoizowanie na poziomie instancji.

Druga wersja pokazuje bardziej eksperymentalne zestawienie dekoratorow
`@property` i `@functools.lru_cache()`. Dzieki temu modul nadaje sie do
porownania, jakie elementy skladni Pythona mozna laczyc oraz jak bardzo
kolejnosc dekoratorow i miejsce przechowywania stanu wplywaja na efekt.

Najwazniejsze mechanizmy i skladnia to:

- `@property`,
- sprawdzanie `hasattr`,
- zapisywanie wartosci w ukrytym atrybucie instancji,
- dekorator `@functools.lru_cache()`,
- nadpisanie w pliku jednej definicji klasy `A` przez kolejna.

To nie jest modul produkcyjny, tylko notatnik techniczny do rozmowy
o cache'owaniu, dekoratorach i leniwej ewaluacji atrybutow.
"""

import functools

class A:
    @property
    def atr1(self):
        if not hasattr(self, '_atr1'):
            print('wyliczam')
            self._atr1 = 66
            return 66
        else:
            return self._atr1


class A:
    @property
    @functools.lru_cache()
    def atr1(self):
        print('wyliczam')
        return 66

if __name__ == "__main__":
    a = A()
    print(a.atr1)
    # a.atr1 = 11
    print(a.atr1)
