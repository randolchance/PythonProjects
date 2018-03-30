"""
PROJECT EULER PROBLEM 108 - Diophantine Reciprocals I

In the following equation x, y, and n are positive integers.

1/x + 1/y = 1/n

For n = 4 there are exactly three distinct solutions:

1/5 + 1/20 = 1/4
1/6 + 1/12 = 1/4
1/8 + 1/8 = 1/4

What is the least value of n for which the number of distinct solutions
exceeds one-thousand?

NOTE: This problem is an easier version of Problem 110; it is strongly
advised that you solve this one first.
"""

from primeCheck import primes
from findDivisors import generateDivisors
from collections import Counter

def computeValue(numList):
    val = 1
    for num in numList:
        val *= num
    return(val)

prime_list = [p for p in primes(2,30)]

number_list = [2]

total_divisors = 1000

try_list = [number_list]
k = 0
result = []
while True:
    #print([[computeValue(i),len([x for x in generateDivisors(i)]),i] for i in try_list])
    tried_list = []
    for attempt in try_list:

        skip_attempt = False
        
        last_p = 'NaN'
        for p in prime_list:
            escape = not Counter(attempt)[p]
            new_number_list = sorted(attempt + [p])
            if last_p != 'NaN':
                number_dict = Counter(new_number_list)
                if number_dict[p] > number_dict[last_p]:
                    continue
            dupe = False
            for x in tried_list:
                if Counter(x) == Counter(new_number_list):
                    dupe = True
            if not dupe:

                number = computeValue(new_number_list)
                
                old_divisors = len([x for x in generateDivisors(new_number_list)])
                if old_divisors > total_divisors:
                    if len(result) == 0:
                        result = [number, old_divisors, new_number_list]
                        print('RESULT: ' + str(result))
                    elif number < result[0]:
                        result = [number, old_divisors, new_number_list]                
                        print('RESULT: ' + str(result))
                    skip_attempt = True
                    escape = True
                if len(result) != 0:
                    if number > result[0]:
                        skip_attempt = True
                        escape = True
                if not skip_attempt:
                    tried_list.append(new_number_list)
            if escape:
                break
            last_p = p
        if skip_attempt:
            continue
    try_list = [t for t in tried_list]
    if len(try_list) == 0:
        break

print(result)
"""
n = 245044800, and has 1008 unique possible x,y combos
"""
