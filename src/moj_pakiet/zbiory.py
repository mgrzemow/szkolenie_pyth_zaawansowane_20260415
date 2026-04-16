import dataclasses
from typing import Any

s = set()
s = {1, 2, 3}
s.add(3)
s.add(3.0)
print(s)
print(3 == 3.0)
s.add((5, 6, 7))
print(s)
for e in s:
    print(e)

x = ["ala", "ma", "kota", "ala", "ma", "kota"]
# usuwanie duplikatów
print(list(set(x)))
# a jak zrobić to bez zmiany kolejności?
print(list({e: None for e in x}.keys()))
s = set(x)
print("ala" in s)
for e in s:
    print(e)

abcdef = set("abcdef")
defghi = set("defghi")
print(defghi & abcdef)
print(defghi | abcdef)
print(defghi - abcdef)
print(defghi ^ abcdef)

# haszowalność
print(hash("ala"))

# s = set()
# x = [1, 2, 3]
# s.add(x)
# x.append(4)
# s.add(x)
print("mama".__hash__())
print(hash("mama"))


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):

        # aby naprościej wyliczyć hasz na podstawie atrybutów, które definiują tożsamość obiektu
        # można użyć funkcji hash na krotce z tych atrybutów
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


a1 = A("mama", 11)
a2 = A("tata", 22)
s = set()
s.add(a1)
s.add(a1)
s.add(a2)
print(s)
a1.x = "tata"
for e in s:
    print(e.x)


@dataclasses.dataclass(frozen=True)
class A:
    x: str


a1 = A("mama")
a2 = A("tata")
s = set()
s.add(a1)
s.add(a1)
s.add(a2)
print(s)
# a1.x = "tata"
for e in s:
    print(e.x)

class A:
    def __init__(self, x):
        self.x = x
        self._frozen = True

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x

    def __setattr__(self, name: str, value: Any) -> None:
        if hasattr(self, "_frozen") and self._frozen:
            raise AttributeError("Obiekt jest zamrożony, nie można zmienić atrybutów.") 
        super().__setattr__(name, value)

a1 = A("mama")
a2 = A("tata")
s = set()
s.add(a1)
s.add(a1)
s.add(a2)
print(s)
a1.x = "tata"
for e in s:
    print(e.x)
