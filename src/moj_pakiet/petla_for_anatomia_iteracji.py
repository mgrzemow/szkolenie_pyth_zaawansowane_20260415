"""
Minimalna demonstracja anatomii petli `for` w Pythonie.

Na pierwszy rzut oka ten plik wydaje sie banalny, ale jego intencja jest
pokazanie bardzo waznego mechanizmu jezyka: petla `for` nie "zna" list,
napisow ani innych typow na sztywno. Dziala na dowolnym obiekcie
iterowalnym, czyli takim, z ktorego da sie pobrac iterator.

Instrukcja:

`for i in 'abc':`

ukrywa pod spodem kilka krokow:

- wywolanie `iter('abc')`,
- wielokrotne pobieranie kolejnych wartosci przez `next(...)`,
- zakonczenie petli po `StopIteration`.

To dlatego ten sam zapis skladni dziala dla napisow, list, krotek,
slownikow, generatorow, obiektow `range` i wielu klas wlasnych,
o ile realizuja odpowiedni protokol iteracji.

Najwazniejsze elementy skladni i mechanizmow to:

- `for ... in ...`,
- zmienna petli otrzymujaca kolejne wartosci,
- obiekt iterowalny,
- iterator i wyjatk `StopIteration`.

Plik jest bardzo maly, ale stanowi dobry punkt wyjscia do glebszego
omowienia iteratorow, generatorow i działania petli `for`.
"""

if __name__ == "__main__":
    for i in 'abc':
        print(i)
