"""
Przykladowy modul z bardzo prostymi funkcjami arytmetycznymi.

Intencja tego pliku nie jest pokazanie zlozonego algorytmu, tylko
udostepnienie malego, czytelnego kodu do cwiczen z:

- adnotacji typow,
- pisania docstringow funkcji,
- importowania funkcji z modulu,
- uruchamiania prostych testow jednostkowych.

Funkcja `dodaj_liczby` sluzy jako glowny material pokazowy do omawiania
opisu parametrow, wartosci zwracanej i dokumentacji generowanej na
podstawie docstringa. Funkcja `podziel_liczby` jest prostsza i moze
sluzyc jako kontrast albo jako baza do testow zwiazanych z wyjatkiem
`ZeroDivisionError`.

Najwazniejsze elementy skladni to:

- `def` z adnotacjami typu przy argumentach i wyniku,
- `return` zwracajace prosty rezultat,
- docstring funkcji zapisany w potrojnych cudzyslowach,
- zwykle importowanie funkcji z modulu w innym pliku.

Taki modul jest celowo niewielki, bo pozwala skupic sie nie na logice
biznesowej, lecz na podstawowych narzedziach pracy z kodem Pythona:
czytelnosci, testowaniu, dokumentowaniu i analizie typow.
"""

def dodaj_liczby(a: int, b: float) -> float:
    """
    Adds two numbers and returns the result.

    Bardziej szczegółowy opis funkcji, 
    który może zawierać informacje o tym, co robi funkcja,
    jakie są jej parametry i co zwraca.

    **tekst boldem**

    1. punkt pierwszy
    2. punkt drugi

    [onet](http://www.onet.pl)


    
    Args:
        a (int): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b

def podziel_liczby(a, b):
    return a / b
