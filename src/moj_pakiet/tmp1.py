def dekorator(f):
    counter = 0
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(counter)
        print("przed wywołaniem funkcji")
        wynik = f(*args, **kwargs)
        print("po wywołaniu funkcji")
        return wynik
    return wrapper

@dekorator
def f1():
    print("wywołanie f1")

f1()
f1()