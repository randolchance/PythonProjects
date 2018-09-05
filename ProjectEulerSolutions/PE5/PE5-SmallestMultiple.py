# PROJECT EULER PROBLEM 5 - Smallest Multiple

from collections import Counter
from findFactors import findFactors

factors = []
for i in range(20,1,-1):
    new_factors = findFactors(i)
    new_factor_count = Counter(new_factors)
    factor_count = Counter(factors)
    for k in new_factor_count:
        if k in factor_count:
            while new_factor_count[k] > factor_count[k]:
                factors.append(k)
                factor_count = Counter(factors)
        else:
            factors.append(k)

factors.sort()
print(factors)
number = 1
for x in factors:
    number *= x

print(number)

