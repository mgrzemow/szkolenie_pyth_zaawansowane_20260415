"""
Demonstracja metod specjalnych, zwanych potocznie metodami magicznymi.

Plik wykorzystuje klase `Spychacz` jako prosty model obiektu, na ktorym
mozna pokazywac, jak Python wywoluje specjalne metody w odpowiedzi
na skladnie i operacje wykonywane przez uzytkownika.

W module pojawiaja sie miedzy innymi:

- `__str__` i `__repr__` do tekstowej reprezentacji obiektu,
- `__eq__` i `__lt__` do porownan,
- `__add__` do przeciazania operatora `+`,
- komentarze dotyczace `__hash__`, `__bool__` i `__del__`.

Najwazniejsza idea jest taka, ze wiele elementow skladni Pythona nie jest
magia zarezerwowana dla typow wbudowanych. Za operacjami takimi jak
`print(obj)`, `obj1 < obj2`, `obj1 + obj2` albo sprawdzanie obiektu
w instrukcji `if` stoja konkretne metody specjalne, ktore mozna
zaimplementowac we wlasnej klasie.

Przyklad pokazuje tez wazna strone praktyczna: samo istnienie metody
specjalnej nie oznacza jeszcze, ze jej uzycie ma sens biznesowy.
Niektore operatory mozna przeciazyc technicznie, ale projektowo nie
zawsze jest to dobry pomysl. Dlatego plik ma charakter zarowno
techniczny, jak i dyskusyjny.

Najwazniejsze elementy skladni to definicja klasy, metody specjalne
rozpoznawane po nazwach z podwojnymi podkresleniami, zwykle instrukcje
warunkowe i operatory arytmetyczne oraz testy w bloku
`if __name__ == "__main__":`.
"""

import pathlib

class Spychacz:
    kierunki = "NESW"

    def __init__(self, nr_rej) -> None:
        self.nr_rej = nr_rej
        self.x = 0
        self.y = 0
        self.kierunek = 0

    def skrec_w_prawo(self):
        self.kierunek = (self.kierunek + 1) % 4
    
    def jedz(self, ile):
        if self.kierunki[self.kierunek] == 'N':
            self.y += ile
        elif self.kierunki[self.kierunek] == 'E':
            self.x += ile
        elif self.kierunki[self.kierunek] == 'S':
            self.y -= ile
        elif self.kierunki[self.kierunek] == 'W':
            self.x -= ile

    def __str__(self):
        return f'{self.__class__.__name__} ({self.nr_rej}), w punkcie ({self.x}, {self.y})'

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.nr_rej})'
    
    # haszowanie - zawsze parami - jeżeli chcę np używać instancji jako kluczy
    def __eq__(self, value: object) -> bool:
        print(self, value)
        return False

    # def __hash__(self) -> int:
    #     pass

    # inne operatory - wszystkie, ale musi to mieć sens

    # dodawanie 2 spychaczy  - można ale po co
    def __add__(self, other):
        print('add', self, other)
        return 678

    # ważne < używany w sortowaniu
    def __lt__(self, other):
        return self.nr_rej < other.nr_rej

    # konwersje do typów wbudowanych
    # uwaga na __bool__ - nie używać
    # def __bool__(self):
    #     return False
    
    # dekstruktor - nie działa
    # def __del__(self):
    #     print('__del__', self)

    

if __name__ == "__main__":
    s1 = Spychacz('wr34567')
    s2 = Spychacz('kr34567')
    s3 = Spychacz('kr34567')
    del(s3)
    # x = s1 + s2
    # print(x)
    # p1 = pathlib.Path(__file__).parent.parent / 'docs'    
    # x = [s1, s2]
    # x.sort()
    # print(x)
    # s1 + 12
    if s1:
        print('spychacz nie jest None')
    else:
        print('spychacz jest None')
