# raw strings
x = r'\d\d'

# byte strings
x = b'abc'
import requests

print(type(x))

imie = 'Jan'
wiek = 45
waga = 88.2343234234
print(f'>{imie:12}< ma {wiek} lat i waży {waga:.2f} kg.')

waluta = 'usd'


url_szablon = 'https://api.nbp.pl/api/exchangerates/rates/a/{}/?format=json'
url = url_szablon.format(waluta)

url = f'https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/?format=json'

# response = requests.get(url)
# print(response.json()['rates'][0]['mid'])

# 0 .. n-1
# -n .. -1
x = 'abcdefgh'
print(x[1:4])
print(x[:3])
print(x[-3:])
print(x[:-3])
print(x[3:])
print(x[1:-1])
print(x[::-1])

x = '   \t   ala \t ma   kota\n'
print(x.split())

x = 'mama'
y = x.upper()
print(id(x), id(y))
print(x is y)

x = 'as'
y = 'dsad'
z = 'dsad'
q = 'asdasd'
w = f'{x}{y}{z}{q}'

lista_w = ['ala', 'ma', 'kota']
print(' - '.join(lista_w))

# sprawdzanie czy st w czyms
print('ma' in 'ala ma kota')

x = 'Ala'
y = 'Ala '
print(x == y)
print(repr(x), repr(y))