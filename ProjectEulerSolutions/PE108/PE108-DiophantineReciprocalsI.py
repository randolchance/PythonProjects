# PROJECT EULER PROBLEM 108 - Diophantine Reciprocals I

from primeCheckII import primes
from findDivisors import generateDivisors
from collections import Counter

def recursivePowerLoop(aDict,aKeys,total):
    if not aKeys:
        yield(1)
    else:
        p = 0
        X = aKeys[0]
        p_max = 2*aDict[X]
        x = 1
        new_keys = aKeys[1:]
        new_list = []
        while x <= total and p <= p_max:
            val_list = [x*val for val in recursivePowerLoop(aDict,new_keys,total) if x*val <= total]
            new_list += val_list
            p += 1
            x = X**p
        for item in new_list:
            yield(item)

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
            count_dict = Counter(new_number_list)
            for x in tried_list:
                if Counter(x) == count_dict:
                    dupe = True
            if not dupe:

                number = computeValue(new_number_list)
                old_divisors = len([x for x in recursivePowerLoop(count_dict,sorted(count_dict.keys()),number)])
                                        
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
"""
