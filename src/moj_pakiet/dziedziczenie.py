"""
Demonstracja dziedziczenia, klas abstrakcyjnych i polimorfizmu
na przykladzie prostego modelu pracownikow.

Intencja tego modulu jest pokazanie, jak budowac hierarchie klas, w ktorych
czesc zachowania jest wspolna, a czesc nadpisywana lub rozszerzana
w klasach pochodnych. Punktem wyjscia jest abstrakcyjna klasa pracownika,
z ktorej wynikaja kolejne poziomy specjalizacji.

W przykladzie wykorzystane sa nastepujace mechanizmy Pythona:

- `abc.ABCMeta` i `@abc.abstractmethod` do definiowania klasy abstrakcyjnej,
- dziedziczenie jednobazowe i rozbudowywanie metod w klasach potomnych,
- `super()` do wywolywania logiki z klasy bazowej,
- `__slots__` do jawnego okreslenia zestawu atrybutow instancji,
- prosta fabryka obiektow z losowymi danymi przy pomocy biblioteki `faker`.

Najwazniejsza skladnia, ktora warto tu obserwowac, to `class X(Y)`,
metody `__init__`, przekazywanie argumentow nazwanych przez `*`
i `**kwargs`, wywolywanie `super().__init__(...)` i `super().pracuj(...)`,
a takze polimorficzne uruchamianie tej samej metody `pracuj`
na obiektach roznych klas.

Modul dobrze pokazuje tez roznice miedzy:

- kontraktem zdefiniowanym przez klase abstrakcyjna,
- wspolna implementacja w klasie bazowej,
- dodatkowymi regułami dopisywanymi przez `Kierownik` i `Dyrektor`.

To przyklad malego modelu obiektowego, na ktorym mozna omowic sens
dziedziczenia i sytuacje, w ktorych klasy potomne nie zastepuja logiki
bazowej, lecz ja rozszerzaja.
"""

import abc
import faker 

class PracownikAbstract(metaclass=abc.ABCMeta):
    __slots__ = ["_zarobki", "imie"]

    def __init__(self, *, imie) -> None:
        self.imie = imie
        self._zarobki = 0

    def wyplata(self):
        tmp = self._zarobki
        self._zarobki = 0
        return tmp

    @abc.abstractmethod
    def pracuj(self): 
        ...


class Pracownik(PracownikAbstract):
    __slots__ = ["_stawka_nad", "_stawka_norm", "_zarobki"]

    def __init__(self, *, stawka_norm, stawka_nad, **kwargs) -> None:
        super().__init__(**kwargs)
        self._stawka_norm = stawka_norm
        self._stawka_nad = stawka_nad
        self._zarobki = 0

    def pracuj(self, ile_h):
        if ile_h <= 8:
            self._zarobki += ile_h * self._stawka_norm
        else:
            self._zarobki += 8 * self._stawka_norm + (ile_h - 8) * self._stawka_nad


class Kierownik(Pracownik):
    __slots__ = ["_bonus_kier"]

    # dodatkowo jeżeli pracuje >= 10 to dostanie kwotowy bonus_kier
    def __init__(self, *, bonus_kier, **kwargs):
        super().__init__(**kwargs)
        self._bonus_kier = bonus_kier

    def pracuj(self, ile_h):
        # jak się dobrać do self klasy bazowej?
        # dla pojedynczego dziedziczenia super() mogę traktować jak self klasy bazowej
        super().pracuj(ile_h)
        if ile_h >= 10:
            # doliczyć bonus kier
            self._zarobki += self._bonus_kier


class Dyrektor(Kierownik):
    __slots__ = ["_bonus_dyr"]

    def __init__(self, *, bonus_dyr, **kwargs):
        super().__init__(**kwargs)
        self._bonus_dyr = bonus_dyr

    def pracuj(self, ile_h):
        # jak się dobrać do self klasy bazowej?
        # dla pojedynczego dziedziczenia super() mogę traktować jak self klasy bazowej
        super().pracuj(ile_h)
        self._zarobki += self._bonus_dyr



# napisać funkcję zatrudnij_zespol(ile_p, ile_k, ile_d):
# zwraca listę odpowiednich obiektów

def zatrudnij_zespol(ile_p = 10, ile_k = 2, ile_d = 1):
    f = faker.Faker('PL_pl')
    lista_p = []
    for _ in range(ile_p):
        lista_p.append(Pracownik(imie=f.first_name(), stawka_norm=20, stawka_nad=40))
    for _ in range(ile_k):
        lista_p.append(Kierownik(imie=f.first_name(), stawka_norm=20, stawka_nad=40, bonus_kier=300))
    for _ in range(ile_d):
        lista_p.append(Dyrektor(imie=f.first_name(), stawka_norm=20, stawka_nad=40, bonus_kier=300, bonus_dyr=1000))
    return lista_p

if __name__ == "__main__":
    # p1 = Dyrektor(
    #     imie="Jan", stawka_norm=20, stawka_nad=40, bonus_kier=300, bonus_dyr=500
    # )
    # print(p1.wyplata())  # 0
    # p1.pracuj(5)  # naliczy się 600, w sumie 600
    # p1.pracuj(2)  # naliczy się 540, w sumie 1140
    # p1.pracuj(12)  # naliczy się 8*20 + 4*40 + 300 + 500 =1120, w sumie 2260
    # print(p1.wyplata())  # 2260
    # print(p1.wyplata())  # 0

    lista_p = zatrudnij_zespol(ile_p = 10, ile_k = 2, ile_d = 1)
    for p in lista_p:
        p.pracuj(3)
        p.pracuj(9)        
        p.pracuj(12)

    fundusz_plac = sum(p.wyplata() for p in lista_p)
    print(fundusz_plac)
