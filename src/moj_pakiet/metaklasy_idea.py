"""
Wprowadzenie do metaklas i dynamicznego tworzenia klas.

Ten plik ma charakter intuicyjny i krok po kroku prowadzi od prostych
obserwacji do bardziej zaawansowanej idei metaklasy. Najpierw pokazuje,
ze klasy sa zwyklymi obiektami, ktorym mozna dopisywac atrybuty, trzymac
je w slowniku i tworzyc instancje przez przekazanie samej klasy jako
argumentu do funkcji.

Dopiero na tym tle pojawia sie `type`, czyli wbudowany mechanizm
tworzenia klas. Przyklad `type("C", (), d)` pokazuje skladnie dynamicznej
budowy klasy z nazwy, listy baz i slownika atrybutow. To naturalny most
do metaklas, czyli obiektow sterujacych tym, jak klasy sa budowane.

W dalszej czesci modulu pokazane sa proste funkcje pelniace role
metaklasy:

- pusta metaklasa, ktora tylko deleguje do `type`,
- metaklasa modyfikujaca slownik klasy przed jej utworzeniem,
- wariant zmieniajacy nazwy atrybutow prywatnych.

Najwazniejsze mechanizmy i skladnia to:

- traktowanie klasy jako wartosci,
- `type` jako konstruktor klas,
- funkcje przyjmujace `cls_name`, `cls_inh` i `cls_dict`,
- `class X(metaclass=...)` jako skladnia przypisania metaklasy,
- operowanie na slowniku definicji klasy przed jej finalnym utworzeniem.

To modul przygotowujacy grunt pod pelniejszy przyklad metaklasy i pomaga
zobaczyc, ze metaprogramowanie klas zaczyna sie od bardzo zwyklych
operacji na obiektach i slownikach.
"""

class A:
    def __init__(self, p1) -> None:
        self.p1 = p1

    ...


class B:
    def __init__(self, p1) -> None:
        self.p1 = p1

    ...


if __name__ == "__main__":
    A.version = "1.2.3"

    def rob_instancje(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    a = rob_instancje(A, 12)
    print(a.p1)

    d = {"A": A, "B": B}
    a1 = d["A"](12)
    print(a1)

    print(type(12))

    class C:
        atr1 = 123

        def m1(self, x, y):
            return x - y

    # type tworzy klasę z elementów
    # type(cls_name, cls_inh, cls_dict)
    def m1(self, x, y):
        return x - y

    d = {"atr1": 123, "m1": m1}

    C1 = type("C", (), d)

    print(C1)
    c = C1()
    print(c.atr1)
    c.m1(1, 2)

    # pusta metaklasa - nic nie robi
    def moja_metaklasa(cls_name, cls_inh, cls_dict):
        return type(cls_name, cls_inh, cls_dict)

    class D(metaclass=moja_metaklasa):
        ...

    d = D()

    # prosta metaklasa - modyfikuje słownik klasowy
    def moja_metaklasa(cls_name, cls_inh, cls_dict):
        cls_dict['version'] = '1.2.3'
        return type(cls_name, cls_inh, cls_dict)

    class E(metaclass=moja_metaklasa):
        ...

    d = E()
    print(d.version)

    # prosta metaklasa - modyfikuje słownik klasowy
    def moja_metaklasa(cls_name, cls_inh, cls_dict):
        new_d = {}
        for atr_name, atr_val in cls_dict.items():
            # w tym miejsscu mogę modyfikować!
            new_d[atr_name] = atr_val
        new_d['version'] = '1.2.3'
        return type(cls_name, cls_inh, new_d)

    # zamiana __ na _
    def private_to_protected(cls_name, cls_inh, cls_dict):
        new_d = {}
        for atr_name, atr_val in cls_dict.items():
            print(atr_name, atr_val)
            if atr_name.startswith(f'_{cls_name}__'):
                atr_name = atr_name.removeprefix(f'_{cls_name}_')
            new_d[atr_name] = atr_val
        return type(cls_name, cls_inh, new_d)

    class E(metaclass=private_to_protected):
        __atr1 = 12

        def __m1(self):
            print('m1')

    e = E()
    print(e._atr1)
    e._m1()
