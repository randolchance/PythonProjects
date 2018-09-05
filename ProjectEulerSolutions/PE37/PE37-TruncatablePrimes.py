# PROJECT EULER PROBLEM 37 - Truncatable Primes

import primeCheckII

START_NUMS = ['1','2','3','5','7','9']
GOOD_NUMS = ['1','3','7','9']
GOOD_LEFT_NUMS = ['2','5']
BAD_END_NUMS = ['1','9']

def _truncPrimeLeft(str_p,trunc_primes):
    cut_left = str_p[1:]
    if cut_left == '1' or cut_left == '9':
        return(False)
    if int(cut_left) not in trunc_primes:
        while len(cut_left) > 0:
            if not primeCheckII.PrimeCheck(int(cut_left)):
                return(False)
            cut_left = cut_left[1:]
    return(True)

def _truncPrimeRight(str_p,trunc_primes):
    cut_right = str_p[:-1]
    if cut_right == '1' or cut_right == '9':
        return(False)
    if int(cut_right) not in trunc_primes:
        while len(cut_right) > 0:
            if not primeCheckII.PrimeCheck(int(cut_right)):
                return(False)
            cut_right = cut_right[:-1]
    return(True)


MAX_DIGITS = 7

def buildNum(str_x,trunc_primes):
    if len(str_x) == 0:
        for num in START_NUMS:
            for new_str_x in buildNum(num,trunc_primes):
                yield(new_str_x)
    elif len(str_x) < MAX_DIGITS:
        for num in GOOD_NUMS:
            if str_x[0] in GOOD_LEFT_NUMS:
                new_nums = [str_x+num]
            elif str_x[0] in BAD_END_NUMS and len(str_x) > 1:
                new_nums = [num+str_x]
            elif str_x[-1] in BAD_END_NUMS and len(str_x) > 1:
                new_nums = [str_x+num]
            else:
                new_nums = [num+str_x,str_x+num]
            for new_num in new_nums:
                if primeCheckII.PrimeCheck(int(new_num)):
                    if _truncPrimeLeft(new_num,trunc_primes) and _truncPrimeRight(new_num,trunc_primes):
                        yield(new_num)
                    for new_str_x in buildNum(new_num,trunc_primes):
                        yield(new_str_x)
                


all_trunc_primes = 11
trunc_primes = []
for num in buildNum('',trunc_primes):
    if num not in trunc_primes:
        print(num)
        trunc_primes.append(num)
    if len(trunc_primes) == all_trunc_primes:
        break
total = 0
if len(trunc_primes) < all_trunc_primes:
    print("ERROR! MAX_DIGITS is insufficient!")
else:
    total = 0
    for val in trunc_primes:
        total += int(val)
    print(total)
print(trunc_primes)

