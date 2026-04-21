

def dekorator(f_oryginalna):
    def f_nowa(*args, **kwargs):
        print('przed wywołaniem f_originalna')
        w = f_oryginalna(*args, **kwargs)
        print('po wywołaniu f_originalna')
        return w
    print('dekoruję', f_oryginalna)
    return f_nowa

@dekorator
def f1():
    print('f1')
    return 55

# f1 = dekorator(f1)


print(f1)
f1()