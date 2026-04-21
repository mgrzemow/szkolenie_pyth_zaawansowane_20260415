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
