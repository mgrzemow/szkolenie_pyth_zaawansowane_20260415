d = {}
d = dict()
d = {'a': 1, 'b': 2, 'c': 3}
print(1 in d)
print('a' in d)
for klucz in d:
    print(klucz, d[klucz])
d['e'] = 5
d['d'] = 4
print(d)
# przed 3.4 - OrderedDict
print(sorted(d))
# sortowanie po kluczach
print(dict(sorted(d.items())))
# sortowanie po wartosciach
print(dict(sorted(d.items(), key=lambda item: item[1], reverse=True)))

print(d)
d1 = {'f':66, **d}
print(d1)

# słownik jako rekord

d = {'imie':'Jan',
     'nazwisko':'Kowalski',
     'wiek': 30}
print(d['imie'])

d = {
     'nazwisko':'Kowalski',
     'wiek': 30,
     'imie':'Jan',
     'inne_pole': 'wartosc'}
print(d['imie'])

