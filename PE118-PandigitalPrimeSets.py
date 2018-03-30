"""
PROJECT EULER PROBLEM 118 - Pandigital Prime Sets
Using all of the digits 1 through 9 and concatenating them freely
to form decimal integers, different sets can be formed.
Interestingly with the set {2,5,47,89,631}, all of the elements
belonging to it are prime.

How many distinct sets containing each of the digits one through
nine exactly once contain only prime elements?
"""

from permutations import permutation
from primeCheckII import IsPrime


isPrime = IsPrime()

def countDigits(x):
    return(len(str(x)))

def hasUniqueDigits(x):
    digits = list(str(x))
    digit_set = set(digits)
    return(len(digits) == len(digit_set))

def computeUniqueCombos(digit_list,n,min_prime=2):
    if len(digit_list) == 0:
        yield([])
    set_list = []
    for x in permutation(digit_list,n):
        x_str = ''
        for i in x:
            x_str += str(i)
        X = int(x_str)
        if X >= min_prime:
            new_digit_list = [i for i in digit_list if i not in x]
            if not isPrime(X):
                continue
            else:
                if len(new_digit_list) == 0:
                    set_list.append([X])
                else:
                    for N in range(n,len(new_digit_list)+1):
                        for y in computeUniqueCombos(new_digit_list,N,X):
                            set_list.append([X]+y)
    for item in set_list:
        yield(item)
    

count = 0
digit_list = [x for x in range(1,10)]

for n in range(1,len(digit_list)//2+1):
    for item in computeUniqueCombos(digit_list,n):
        print(item)
        count += 1

print(count)
# 44680
