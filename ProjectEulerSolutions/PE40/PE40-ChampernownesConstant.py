# PROJECT EULER PROBLEM 40 - Champernowne's Constant


def findDigit(d):
    if d == 1:
        return(str(1))
    n = 1
    s = '1'
    while len(s) < d:
        n += 1
        s += str(n)
    return(s[d-1])


result = 1
for p in range(7):
    d = 10**p
    s = findDigit(d)
    print(s)
    result *= int(s)

print(result)

