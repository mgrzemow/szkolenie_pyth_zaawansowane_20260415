"""
Szczegolowa demonstracja pelnego cyklu zycia klasy tworzonej przez
metaklase.

Intencja tego modulu jest pokazanie, ze tworzenie klasy w Pythonie tez
jest procesem sterowanym przez obiekt - metaklase. Przyklad skupia sie
na czterech kluczowych metodach:

- `__prepare__`,
- `__new__`,
- `__init__`,
- `__call__`.

Kazda z nich odpowiada za inny etap:

- przygotowanie przestrzeni nazw klasy,
- utworzenie obiektu klasy,
- zainicjalizowanie obiektu klasy,
- stworzenie instancji klasy po pozniejszym wywolaniu.

Modul jest celowo "glosny": wypisuje informacje diagnostyczne, aby bylo
widac kolejnosc zdarzen i roznice miedzy tworzeniem klasy a tworzeniem
jej instancji. To dobry material do rozmowy o tym, ze instrukcja `class`
jest wykonywalna i moze byc przechwycona przez bardziej zaawansowany
mechanizm niz zwykle dziedziczenie.

Najwazniejsze mechanizmy i skladnia to:

- `class Meta(type)` jako definicja metaklasy,
- `@classmethod` przy `__prepare__`,
- przekazywanie dodatkowych argumentow klasowych przez `class A(..., suffix=..., akuku=...)`,
- rozroznienie miedzy `Meta.__call__` a `A.__init__`,
- dzialanie `super()` wewnatrz metod specjalnych metaklasy i klasy.

To modul bardziej zaawansowany niz zwykle dekoratory czy deskryptory,
ale bardzo dobrze pokazuje "co dzieje sie pod spodem" przy pracy
z klasami w Pythonie.
"""

# na podstawie świetnego artykułu:
# https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/

class Meta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print()
        print(f"  Meta.__prepare__({mcs=}, {name=}, {bases=}, {kwargs=})")
        return {"atr5": 99}

    # Most commonly - here!!!:
    def __new__(mcs, name, bases, attrs, **kwargs):
        print()
        print(f"  Meta.__new__({mcs=}, {name=}, {bases=}, {attrs=}, {kwargs=})")
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs, **kwargs):
        print()
        print(f"  Meta.__init__({cls=}, {name=}, {bases=}, {attrs=}, {kwargs=})")
        return super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print()
        print(f"  Meta.__call__({cls=}, {args=}, {kwargs=})")
        return super().__call__(*args, **kwargs)


if __name__ == "__main__":
    class A(metaclass=Meta, suffix="_get", akuku=99):
        cls_atr1 = 9

        def m1(self, x, y):
            print("m1", x, y)

        def __new__(cls, *args, **kwargs):
            print()
            print(f"  Class.__new__({cls=}, {args=}, {kwargs=})")
            return super().__new__(cls)

        def __init__(self, *args, **kwargs):
            print()
            print(f"  Class.__init__({self=}, {args=}, {kwargs=})")

    a = A("Jan", "Nowak")
    # print(a.atr5)
