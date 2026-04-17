x = range(10_000_000)
input("stop")
y1 = (i**2 for i in x)
input("stop")
y2 = (i / 14 for i in y1)
input("stop")
for i in y2:
    if i > 1000:
        break
    print(i)
