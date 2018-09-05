# PROJECT EULER PROBLEM 71 - Ordered Fractions

from fractions import Fraction

MAX_FRAC = Fraction(3,7)
MAX_d = 1000000


nearest_frac = Fraction(2,5)
try:
    for d in range(8,MAX_d+1):
        n = d*3//7
        frac = Fraction(n,d)
        #if frac.numerator != n or frac.denominator != d:
        #    continue
        if frac >= MAX_FRAC:
            continue
        #print(frac, float(frac))
        
        if frac > nearest_frac and frac < MAX_FRAC:
            nearest_frac = frac

except:
    pass
finally:
    print("\n",nearest_frac)
    print(nearest_frac.numerator)

