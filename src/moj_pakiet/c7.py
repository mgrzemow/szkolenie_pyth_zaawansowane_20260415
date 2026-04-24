"""
Ćwiczenie z użycia `property` w Pythonie.

Plik pokazuje, jak za pomocą właściwości:

- ukryć wewnętrzną reprezentację danych obiektu,
- dodać walidację przy zapisie atrybutu,
- wystawić wygodny interfejs tekstowy na zewnątrz,
- udostępnić dodatkową właściwość tylko do odczytu.

W tym przykładzie adres IP jest na zewnątrz obsługiwany jako napis
``"192.168.0.1"``, ale wewnątrz obiektu przechowywany jest jako krotka liczb.
"""


class Host:
    __slots__ = [
        "_ip"
    ]

    # Setter przyjmuje zapis tekstowy, waliduje go i zamienia na krotkę liczb.
    def _set_ip(self, ip):
        k = ip.split(".")
        if len(k) != 4:
            raise ValueError(f"ip address must be 4 digits: {ip}")
        k = [int(i) for i in k]
        if not all(0 <= i <= 255 for i in k):
            raise ValueError(f"ip address must be between 0 and 255: {ip}")
        self._ip = tuple(k)

    # Getter składa wewnętrzną krotkę z powrotem do formatu tekstowego.
    def _get_ip(self):
        return ".".join(str(i) for i in self._ip)

    # Właściwość `ip` daje kontrolowany dostęp do atrybutu `_ip`.
    ip = property(fget=_get_ip, fset=_set_ip)

    # Wariant read-only: brak settera oznacza, że tę właściwość można tylko odczytać.
    @property
    def ip_tuple(self):
        return self._ip

    def __init__(self, ip):
        # Używamy property już w konstruktorze, żeby walidacja działała od początku.
        self.ip = ip


# za pomocą property zmienić wewnętrzną reprezentację na krotkę (192, 168, 0, 1)
# dodać walidację, że każda z liczb jest (0..255)
# * dodać property read_only ip_tuple

if __name__ == "__main__":
    h = Host("192.168.0.234")
    print(h.ip)
    h.ip = "8.8.8.8"
    print(h.ip)
    h.ip = "8.8.8.99"
    print(h.ip_tuple)
