"""
Prosty moduł do demonstracji `monkeypatch` w pytest.

Kod korzysta z `requests.get`, ale testy podmieniają tę funkcję lokalnie,
dzięki czemu nie wykonują prawdziwego połączenia HTTP.
"""

import requests


def pobierz_json(url):
    """Pobiera odpowiedź JSON spod wskazanego adresu."""
    response = requests.get(url, timeout=5)
    return response.json()


def pobierz_wartosc(url, klucz):
    """Zwraca pojedynczą wartość odczytaną z odpowiedzi JSON."""
    dane = pobierz_json(url)
    return dane[klucz]


if __name__ == "__main__":
    # Ten moduł ma sens głównie w testach, więc przykład zostaje opisowy.
    print("Uruchom testy pytest, aby zobaczyć monkeypatch w praktyce.")
