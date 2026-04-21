"""

Napisać generator, który będzie zwracał wszystkie dostępne notowania waluty o podanym kodzie z API NBP:

http://api.nbp.pl

Generator będzie wczytywał dane latami (wolno wysłać zapytanie tylko o rok danych na raz) i będzie zwracał (yield)notowania w kolejności odwrotnej chronologicznie (w tył).

Format pojedynczego notowania będzie słownikiem o postaci:
{
    'code': 'USD',
        'bid': 3.3,
        'ask': 3.4,
        'effectiveDate': <tutaj obiekt date z datą notowania>
}

Proponuję skorzystać z usługi:
https://api.nbp.pl/api/exchangerates/rates/c/gbp/2012-01-01/2012-01-31/?format=json

Zwróćcie uwagę, że w URLu są zawarte: kod waluty, i obie daty.
Jak wysłać zapytanie i przeczytać odpowiedź:

r = requests.get("https://api.nbp.pl/api/exchangerates/rates/c/gbp/2012-01-01/2012-01-31/?format=json")

# Sprawdzanie statusu zapytania:
# if r.status_code != 200:
#     print('coś nie tak', r.status_code)
#     exit()

# lub:
# r.raise_for_status()

# Format JSON to po prostu zagnieżdżona struktura słowników i list, a więc np cena bid # pierwszego notowania:
j = r.json()
print(j["rates"][0]["bid"])

Możemy oczywiście po listach iterować za pomocą pętli for.

Korzystamy z pakietu requests, który trzeba ściągnąć i zainstalować.
Aby to zrobić wpisujemy w oknie Terminal w Pycharm polecenie:
pip install requests

Dodadkowo dla ambitnych napisać 3 generatory przetwarzające notowania strumieniowo:
# 1. Wyliczał spread i dodawał do notowania jako wartość dla klucza 'spread'
# 2. Wyliczał zmianę względem dnia poprzedniego (dla ceny ask) - i dodawał do notowania jako wartość dla klucza 'delta'
# 3. Generator filtrujący, który będzie puszczał dalej tylko notowania spełniające warunek:
#    wartosc bezwzględna pola o nazwie nazwa_pola >= min wartosc

Ostatecznie chciałbym mieć możliwość np znaleźć notowania USD w których spread >= 0.08 i zmiana względem dnia poprzedniego była >=0.07:

g_nbp = generatorNBP("usd")
g1 = generuj_spread(g_nbp)
g2 = generuj_delta(g1)
g3 = filtruj(g2, "spread", 0.08)
g4 = filtruj(g3, "delta", 0.07)

"""

import itertools

import requests
import datetime as dt


class GeneratorNBPKlasa:
    def __init__(self, waluta) -> None:
        self.waluta = waluta
        self.szablon = (
            "https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/{}/?format=json"
        )
        self.d2 = dt.date.today()
        self.doczytaj_rok()
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.data):
            self.doczytaj_rok()
        n = self.data[self.idx]
        self.idx += 1
        #         zmodyfikować notowanie
        del n["no"]
        n["code"] = self.waluta
        n["effectiveDate"] = dt.date.fromisoformat(n["effectiveDate"])
        return n

    def doczytaj_rok(self):
        td1 = dt.timedelta(days=1)
        d1 = self.d2 - 365 * td1
        r = requests.get(self.szablon.format(self.waluta, d1, self.d2))
        if r.status_code == 404:
            raise StopIteration
        r.raise_for_status()
        self.data = r.json()["rates"][::-1]
        self.idx = 0
        self.d2 = d1 - td1


class GeneratorNBPKlasa:
    def __init__(self, waluta) -> None:
        self.waluta = waluta
        self.szablon = (
            "https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/{}/?format=json"
        )
        self.d2 = dt.date.today()
        self.doczytaj_rok()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            n = next(self.data)
        except StopIteration:
            self.doczytaj_rok()
            n = next(self.data)
        # zmodyfikować notowanie
        del n["no"]
        n["code"] = self.waluta
        n["effectiveDate"] = dt.date.fromisoformat(n["effectiveDate"])
        return n

    def doczytaj_rok(self):
        td1 = dt.timedelta(days=1)
        d1 = self.d2 - 365 * td1
        r = requests.get(self.szablon.format(self.waluta, d1, self.d2))
        if r.status_code == 404:
            return
        r.raise_for_status()
        self.data = reversed(r.json()["rates"])
        self.d2 = d1 - td1


if __name__ == "__main__":
    g_nbp = GeneratorNBPKlasa("usd")
    for n in g_nbp:
        print(n)

    # znowu zero
