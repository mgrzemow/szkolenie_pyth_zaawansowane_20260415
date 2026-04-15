"""
Ćwiczenie:

 1. Wczytać z konsoli długości 3 boków trójkąta
 2. Sprawdzić i wypisać na ekran:
  - czy trójkąt da się stworzyć
  - czy jest prostokątny
  - czy jest równoramienny
  - czy jest równoboczny

 Podpowiedzi:
  - czy niektóre warunki zależą od siebie i w jaki sposób? Jak to wpłynie na zagnieżdżenie if-ów?

 Rozszerzenia ćwiczenia:
 - czy da się wpisać takie dane, żeby wyszedł trójkąt równoramienny i prostokątny? Dlaczego nie i jak to ominąć?
 - co robi eval()?
"""

import math


if __name__ == '__main__':
    a = eval(input('Podaj długość boku: '))
    b = eval(input('Podaj długość boku: '))
    c = eval(input('Podaj długość boku: '))

    istnieje = a + b > c and a + c > b and b + c > a

    if not istnieje:
        print('Takiego trójkąta nie da się zbudować.')
    else:
        prostokatny = (
            math.isclose(a ** 2 + b ** 2, c ** 2)
            or math.isclose(a ** 2 + c ** 2, b ** 2)
            or math.isclose(b ** 2 + c ** 2, a ** 2)
        )
        rownoramienny = a == b or a == c or b == c
        rownoboczny = a == b == c

        print('Trójkąt da się zbudować.')
        print('Trójkąt jest prostokątny.' if prostokatny else 'Trójkąt nie jest prostokątny.')
        print('Trójkąt jest równoramienny.' if rownoramienny else 'Trójkąt nie jest równoramienny.')
        print('Trójkąt jest równoboczny.' if rownoboczny else 'Trójkąt nie jest równoboczny.')
