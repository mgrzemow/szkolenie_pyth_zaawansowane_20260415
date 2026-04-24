"""
Demonstracja dekoratora przechowujacego stan w domknieciu.

Intencja tego pliku jest pokazanie, ze dekorator moze nie tylko opakowac
funkcje dodatkowym kodem, ale tez zapamietywac dane pomiedzy kolejnymi
wywolaniami. W tym przypadku zapamietywany jest licznik uruchomien
dekorowanej funkcji.

Kluczowy mechanizm to zmienna `counter` zdefiniowana w funkcji
dekorujacej. Nie jest ona lokalna dla `wrapper`, ale tez nie jest
globalna. Nalezy do zakresu otaczajacego, dlatego do jej modyfikacji
potrzebne jest slowo kluczowe `nonlocal`.

Przyklad pokazuje nastepujace elementy:

- funkcje zagniezdzone,
- dekorator przez skladnie `@dekorator`,
- domkniecie przechowujace stan,
- `nonlocal` do modyfikacji zmiennej z wyzszego zakresu,
- opakowanie funkcji dodatkowymi komunikatami przed i po wywolaniu.

Najwazniejsza skladnia to `def dekorator`, `def wrapper`,
`nonlocal counter`, `*args`, `**kwargs` i `return wrapper`.
To bardzo dobry, maly przyklad ilustrujacy, ze dekorator nie musi
korzystac z klasy, aby zachowywac stan pomiedzy kolejnymi wywolaniami.
"""

def dekorator(f):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(counter)
        print("przed wywołaniem funkcji")
        wynik = f(*args, **kwargs)
        print("po wywołaniu funkcji")
        return wynik
    return wrapper

@dekorator
def f1():
    print("wywołanie f1")

if __name__ == "__main__":
    f1()
    f1()
