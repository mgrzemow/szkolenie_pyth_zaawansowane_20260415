"""
Wprowadzenie do idei dekoratorow w Pythonie.

Plik ma charakter pokazowy i zestawia dwa podstawowe warianty:

- dekorator bez parametrow,
- dekorator z parametrami, czyli dekorator-fabryka.

Najwazniejsza intencja tego modulu to pokazanie, ze dekorator nie jest
"magia skladni", tylko zwyklym mechanizmem pracy na funkcjach jako
obiektach. Funkcja moze zostac przekazana jako argument, opakowana
inna funkcja i zwrocona jako nowa wartosc przypisana pod ta sama nazwa.

Drugi wazny temat to moment wykonania kodu. Czesci dekoratora wykonuje
sie juz podczas definicji funkcji, a nie dopiero przy jej pozniejszym
wywolaniu. Dlatego komunikaty `print('dekoruje', ...)` pojawiaja sie
przed uruchomieniem funkcji demonstracyjnej.

Najwazniejsze elementy skladni to:

- definicje funkcji zagniezdzonych,
- przekazywanie `*args` i `**kwargs`,
- skladnia `@dekorator` oraz `@dekorator_2(12, 33)`,
- zwracanie funkcji z funkcji,
- przechwytywanie danych z zewnetrznego zakresu przez domkniecia.

Modul dobrze sluzy jako punkt wyjscia przed wejsciem w bardziej
zaawansowane warianty dekoratorow opartych o klasy, `wraps`
albo dodatkowa konfiguracje.
"""


# dekorator bez parametrów
def dekorator(f_oryginalna):
    def f_nowa(*args, **kwargs):
        print('przed wywołaniem f_originalna')
        w = f_oryginalna(*args, **kwargs)
        print('po wywołaniu f_originalna')
        return w
    print('dekoruję', f_oryginalna)
    return f_nowa

# dekorator z parametrami

def dekorator_2(p1, p2):
    def dekorator_wlasciwy(f_oryginalna):
        def f_nowa(*args, **kwargs):
            print('przed wywołaniem f_originalna', p1, p2)
            w = f_oryginalna(*args, **kwargs)
            print('po wywołaniu f_originalna')
            return w
        print('dekoruję', f_oryginalna)
        return f_nowa
    return dekorator_wlasciwy

if __name__ == "__main__":
    @dekorator_2(12, 33)
    def f1():
        print('f1')
        return 55

    # f1 = dekorator(f1)

    print(f1)
    f1()
