x = 'mama tata mama mama tata ja'
{
    'mama': 3,
    'tata': 2,
    'ja': 1
}
d = {}
for word in x.split():
    # jeżeli pojawia się pierwszy raz
    if word not in d:
        d[word] = 1
    # a jak kolejny raz
    else:
        d[word] = d[word] + 1
print(d)

d = {}
for word in x.split():
    d[word] = d.get(word, 0) + 1
print(d)

import collections

def f1():
    return 0

d = collections.defaultdict(f1)
for word in x.split():
    d[word] += 1

print(d)

d = collections.defaultdict(lambda: 0)
for word in x.split():
    d[word] += 1

print(d)

d = collections.defaultdict(int)
for word in x.split():
    d[word] += 1

print(d)

x = 'ala alicja alina beata bartek'
{
    'a': ['ala', 'alicja', 'alina'],
    'b': ['beata', 'bartek']
}
d = {}
for word in x.split():
    first_letter = word[0]
    if first_letter not in d:
        d[first_letter] = []
    d[first_letter].append(word)
print(d)

# z użyciem get
d = {}  
for word in x.split():
    first_letter = word[0]
    lista = d.get(first_letter, [])
    lista.append(word)
    d[first_letter] = lista
print(d)

# z użyciem setdefault
d = {}  
for word in x.split():
    first_letter = word[0]
    d.setdefault(first_letter, []).append(word)
print(d)

# z użyciem defaultdict

d = collections.defaultdict(list)
for word in x.split():
    d[word[0]].append(word)
print(d)