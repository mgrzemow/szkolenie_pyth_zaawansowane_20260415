"""
Spychacz będzie pamiętać:
 - nr rejestracyjny
 - kierunek NESW
 - pozycja x, y
 Spychacz będzie umieć:
 - się urodzić w (0, 0) skierowany na N
 - jechać n kroków przed siebie
 - skręcać w prawo o 90 stopni
 - wypisywać swoje dane
"""


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

    def wypisz(self):
        print(f'{self.__class__.__name__} ({self.nr_rej}), w punkcie ({self.x}, {self.y})')

if __name__ == "__main__":
    a = Spychacz("kr12345")
    a.wypisz()
    a.jedz(8)
    a.skrec_w_prawo()
    a.wypisz()
    a.jedz(8)
    a.skrec_w_prawo()
    a.wypisz()
    a.jedz(8)
    a.skrec_w_prawo()
    a.wypisz()
    a.jedz(8)
    a.skrec_w_prawo()
    a.wypisz()
