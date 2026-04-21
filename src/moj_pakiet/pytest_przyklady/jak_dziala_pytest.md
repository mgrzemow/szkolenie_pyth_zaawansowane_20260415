# Jak Dziala Pytest

Pytest działa na prostych konwencjach.

Szuka:
- plików o nazwie `test_*.py`,
- funkcji o nazwie `test_*`,
- klas testowych, jeśli są potrzebne, choć na start zwykle nie są konieczne.

Najprostszy test wygląda tak:

```python
def test_dodawanie():
    assert 2 + 2 == 4
```

Co robi pytest:
- uruchamia test,
- przechwytuje wyjątki i nieudane asercje,
- pokazuje czytelny raport, co było po lewej i po prawej stronie `assert`.

Dlatego w pytest zwykle nie pisze się specjalnych metod typu `assertEqual`.
W większości przypadków wystarcza zwykły `assert`.
