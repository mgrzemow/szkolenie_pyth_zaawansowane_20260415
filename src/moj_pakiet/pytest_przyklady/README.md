# Przyklady Pytest

Ten katalog zbiera małe, dydaktyczne przykłady do kursu `pytest`.

Układ jest celowo prosty:
- pliki `do_testow_*.py` zawierają kod, który testujemy,
- pliki `test_*.py` znajdują się w `tests/pytest_przyklady/`,
- każdy przykład pokazuje jeden główny mechanizm pytesta.

Najważniejsza idea:
- pytest sam wyszukuje pliki `test_*.py`,
- uruchamia funkcje `test_*`,
- wynik sprawdza zwykłymi `assert`,
- dodatkowe narzędzia dostarcza przez fixture, np. `capsys` albo `monkeypatch`.
