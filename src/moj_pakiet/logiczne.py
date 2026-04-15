# print(True == 1)
# print(False == 0)

import datetime as dt
import re
x = None
x = re.match(r'\d\d', '8d')

class A:
    # Nie uzywać!!!
    def __bool__(self):
        print('wywołanie __bool__')
        return False
x = A()

if x:
    print(True, x)
else:
    print(False, x)

x = ''
if x and x[0] == 'a':
    print(True, x)
else:
    print(False, x)

print(None and 55)