# PROJECT EULER PROBLEM 21 - Amicable Numbers


from findFactors import findFactors
from findDivisors import findDivisors

def isAmicable(x):
    divisor_list = findDivisors(findFactors(x))[:-1]
    new_x = sum(divisor_list)
    if new_x == x:
        return(False)
    divisor_list = findDivisors(findFactors(new_x))[:-1]
    return(x==sum(divisor_list))


total = 0
for x in range(1,10000):
    total += x if isAmicable(x) else 0

print(total)

