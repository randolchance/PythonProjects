def gen(a,b):
    for x in range(a,b):
        if not x%7:
            yield x

for i in gen(0,777):
    print(i)
