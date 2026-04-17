import datetime as dt
import collections
import functools


def f1():
    print("f1")


print(f1.__call__)


class ObiektUdajacyFunkcje:
    def __call__(self):
        print("ObiektUdajacyFunkcje.__call__")


o = ObiektUdajacyFunkcje()
o()


def f2(a, b, c, x):
    return a * x * x + b * x + c


f2_l = lambda a, b, c, x: a * x * x + b * x + c
f2_l(1, 2, 3, 4)

d = collections.defaultdict(lambda: dt.date.today() + dt.timedelta(days=7))

print(d["ala"])

x = ["bez", "grog", "zebra"]


def zwiadowca(*args, **kwargs):
    print(args)
    print(kwargs)
    print("---")
    return 66


x.sort(key=zwiadowca)
print(x)


def ostatni_znak(s):
    return s[-1]


x.sort(key=ostatni_znak)
x.sort(key=lambda s: s[-1])
print(x)

x = ["Jan Kowalski", "Adam Nowak", "Adam Kowalski"]
x.sort(key=lambda s: s.split()[::-1])
print(x)

# w sortowaniu decyduje operator < czyli __lt__

d = {
    "-": lambda a, b: a - b,
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}
operacje = "2 * 6"
op1, operator, op2 = operacje.split()
op1 = float(op1)
op2 = float(op2)
wynik = d[operator](op1, op2)
print(wynik)

# map, filter i reduce

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
m = map(lambda i: i**2, x)
print(list(m))

f = filter(lambda i: i % 2 == 0, x)
print(list(f))

# jak złożyć map z filter
f = filter(lambda i: i % 2 == 0, x)
m = map(lambda i: i**2, f)
print(list(m))

x = ["ala", "ma", "kota", "", None, 0, False, True]
f = filter(None, x)
print(list(f))

# reduce jest w module functools
x = "potrzuje ygrekow to honorowa ogromna nadzieja"


def dodaj_pierszy_znak(agg, e):
    print(agg, e)
    return agg + e[0]


print(functools.reduce(dodaj_pierszy_znak, x.split(), ""))
print(functools.reduce(lambda agg, e: agg + e[0], x.split(), ""))

# użyć reduce aby pogrupować słowa po pierwszej literze w słowniku
# * użyć defaltdict
# * usunąc duplikaty
x = "ala alina alicja beata bartek zenon zenon"


def f_agg(d, slowo):
    klucz = slowo[0]
    if klucz not in d:
        d[klucz] = []
    d[klucz].append(slowo)
    return d


print(functools.reduce(f_agg, x.split(), {}))


def f_agg(d, slowo):
    d[slowo[0]].append(slowo)
    return d


print(functools.reduce(f_agg, x.split(), collections.defaultdict(list)))


def f_agg(d, slowo):
    d[slowo[0]].add(slowo)
    return d


print(functools.reduce(f_agg, x.split(), collections.defaultdict(set)))


def f_agg(d, slowo):
    d[slowo[0]].add(slowo)
    return d


print(functools.reduce(f_agg, x.split(), collections.defaultdict(set)))


def f_agg(d, slowo):
    return (d[slowo[0]].add(slowo), d)[1]


print(
    functools.reduce(
        lambda d, slowo: (d[slowo[0]].add(slowo), d)[1],
        x.split(),
        collections.defaultdict(set),
    )
)

x = [11, 22, 33, 44]
print(list(enumerate(x)))
print(list(map(lambda t: t[1] ** t[0], enumerate(x))))


# ciekawe gadżety w functools: partial, lru_cache
@functools.lru_cache(maxsize=None)
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

print(fibo(900))

# functools.partial pozwala na częściowe zastosowanie funkcji, czyli "zamrożenie" niektórych argumentów.
def potega(a, b=2):
    print(f"Obliczam {a} do potęgi {b}")
    return a**b

def do_kwadratu(x):
    print(f"Obliczam {x} do kwadratu")
    return potega(x, 2)

do_szescianu_partial = functools.partial(potega, b=3)

do_szescianu_partial(5)

