# PROJECT EULER PROBLEM 33 - Digit Cancelling Fractions

from fractions import Fraction

results = []
for denominator in range(11,100):
    if denominator % 10 == 0:
        continue
    for numerator in range(11,denominator):
        str_num = str(numerator)
        str_den = str(denominator)
        for k in str_num:
            if k not in str_den:
                continue
            try:
                n = int([s for s in str(numerator) if s != k][0])
            except:
                n = int(k)
            try:
                d = int([s for s in str(denominator) if s != k][0])
            except:
                d = int(k)
            if numerator/denominator == n/d:
                print(numerator,denominator,n,d)
                results.append(Fraction(n,d))

print(results)
frac = Fraction(1,1)
for r in results:
    frac *= r
print(frac.denominator)

