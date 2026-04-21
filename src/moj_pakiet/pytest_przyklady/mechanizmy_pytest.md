# Najwazniejsze Mechanizmy

W tych przykładach pojawiają się cztery podstawowe mechanizmy.

`assert`
- najprostszy sposób sprawdzania wyniku,
- pytest sam rozpisuje błąd, gdy warunek nie jest spełniony.

`fixture`
- przekazuje testowi gotowe dane albo obiekty,
- pozwala współdzielić setup między testami.

`parametrize`
- uruchamia ten sam test dla wielu zestawów danych,
- eliminuje duplikowanie bardzo podobnych testów.

`capsys`
- przechwytuje tekst wypisywany na standardowe wyjście,
- przydaje się do testowania funkcji używających `print`.

`monkeypatch`
- tymczasowo podmienia funkcję, metodę albo zmienną,
- jest wygodny do izolowania kodu od sieci, systemu plików albo środowiska.

`pytest-mock`
- dostarcza fixture `mocker`, która upraszcza pracę z `Mock`, `MagicMock`
  i operacjami `patch`,
- dobrze się sprawdza tam, gdzie chcesz jednocześnie podmieniać zależność
  i sprawdzać liczbę wywołań lub argumenty.
