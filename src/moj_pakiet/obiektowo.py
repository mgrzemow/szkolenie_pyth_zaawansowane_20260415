class Czlowiek:
    __slots__ = ["_imie"]
    atr_klasowy = 123

    # __slots__ = ['imie']
    def __init__(self, imie):
        self._imie = imie

class A(Czlowiek):
    def m1(self):
        print(self._imie)

c1 = Czlowiek("Jan")
c2 = Czlowiek("Zosia")
c1._imie = 'Ola'
print(c1._imie)
