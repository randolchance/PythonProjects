# PROJECT EULER PROBLEM 87 - Prime Power Triplets


import primeCheckII


MAX_VAL = 50000000    

def findPrimePowerTriples():
    P_set = set()
    for p in primeCheckII.primes(2,-1):
        for q in primeCheckII.primes(2,-1):
            for r in primeCheckII.primes(2,-1):
                val = p**2+q**3+r**4
                if val < MAX_VAL:
                    P_set |= {val}
                else:
                    break_q = (r==2)
                    break_p = break_q and (q==2)
                    break
            if break_q:
                break
        if break_p:
            return(P_set)


print(len(findPrimePowerTriples()))



