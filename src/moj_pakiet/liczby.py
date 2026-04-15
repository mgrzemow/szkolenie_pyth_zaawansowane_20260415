# bigint
x = 999 ** 999
print(x)
print(type(x))

print((-9) ** .5)
print(type((-9) ** .5))
x = .1 + .2
y = .3
print(x == y)
print(x, y)
# round()
import math
print(math.isclose(x, y))
# ułamki zwykłe
import fractions

import decimal as dc
x = dc.Decimal('.1') + dc.Decimal('.2')
y = dc.Decimal('.3')
print(x)
