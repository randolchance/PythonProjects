values = []
for x in range(1000,3001):
    if not int(x/1000)%2 and not int(x/100)%2 and not int(x/10)%2 and not x%2:
        values.append(str(x))

print(",".join(values))


"""OR"""
values = []
for x in range(1000,3001):
    s = str(x)
    if not int(s[0])%2 and not int(s[1])%2 and not int(s[2])%2 and not int(s[3])%2:
        values.append(str(x))
print(",".join(values))
