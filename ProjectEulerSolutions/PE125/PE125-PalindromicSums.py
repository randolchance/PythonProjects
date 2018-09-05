# PROJECT EULER PROBLEM 125 - Palindromic Sums

from math import sqrt

def makePalendrome(digits,first=False):
    for n in range(first,10):
        d = digits - 1
        if d == 0:
            yield(str(n))
        else:
            for m in makePalendrome(digits-1):
                yield(str(n)+m)


good_palendromes = []
for d in range(1,9):
    odd = (d%2 == 1)
    for n in makePalendrome(d//2+odd,True):
        p = None
        if odd:
            p = int(n + n[-2::-1])
        else:
            p = int(n + n[-1::-1])
        biggest_sq = int(sqrt(p))
        if biggest_sq**2 == p:
            biggest_sq -= 1
        for s in range(biggest_sq,0,-1):
            q = p
            good_p = False
            for r in range(s,0,-1):
                q -= r**2
                if q <= 0:
                    good_p = (q == 0)
                    break
            if good_p:
                good_palendromes.append(p)
                print(p)
                break

print(sum(good_palendromes))

