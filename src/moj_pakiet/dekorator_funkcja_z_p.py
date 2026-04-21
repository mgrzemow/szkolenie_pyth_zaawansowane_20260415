import functools


def dekorator(p1, p2):
    def dekorator_wlasciwy(f_oryginalna):
        @functools.wraps(f_oryginalna)
        def f_nowa(*args, **kwargs):
            print('przed wywołaniem f_originalna', p1, p2)
            w = f_oryginalna(*args, **kwargs)
            print('po wywołaniu f_originalna')
            return w
        print('dekoruję', f_oryginalna)
        return f_nowa
    return dekorator_wlasciwy

@dekorator(12, 33)
def f1():
    print('f1')
    return 55

# f1 = dekorator(f1)


print(f1)
f1()