# napisać dekorator, który będzie kowertował wartość zwracaną
# do int
# a jak się nie uda to do float
# a jak się nie uda to ValueError

import functools

def to_int_float(f_oryginalna):
    @functools.wraps(f_oryginalna)
    def f_nowa(*args, **kwargs):
        w = f_oryginalna(*args, **kwargs)
        try:
            return int(w)
        except ValueError:
            return float(w)
        return w
    return f_nowa

@to_int_float
def f1(p):
    return p

print(f1(11))
print(f1(11.222))
print(f1('12'))
print(f1('12.1123'))
# print(f1('asdasdas'))

print(f1)
print(f1.__closure__[0].cell_contents)
