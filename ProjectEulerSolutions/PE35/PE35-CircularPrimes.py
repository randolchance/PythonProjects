# PROJECT EULER PROBLEM 35 - Circular Primes

import primeCheckII

def _rotPrime(str_p):
    new_str_p = str_p[1:]+str_p[0]
    p_list = [int(str_p)]
    while new_str_p != str_p:
        if not primeCheckII.PrimeCheck(int(new_str_p)):
            return(False)
        p_list.append(int(new_str_p))
        new_str_p = new_str_p[1:]+new_str_p[0]
    return(p_list)


BAD_NUMS = ['2','4','5','6','8','0']

circ_primes = []
for p in primeCheckII.primes(2,1000000):
    if p in circ_primes:
        continue
    str_p = str(p)
    if len(str_p) == 1:
        circ_primes.append(p)
    else:
        if not any([b in str_p for b in BAD_NUMS]):
            rot_primes = _rotPrime(str_p)
            if rot_primes:
                for val in rot_primes:
                    if val not in circ_primes:
                        circ_primes.append(val)
                print(rot_primes)

print(circ_primes)
print(len(circ_primes))

