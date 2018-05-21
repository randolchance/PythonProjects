# PROJECT EULER PROBLEM 60 - Prime Pair Sets
import permutations
import primeCheckII
from memoise import Memoise

@Memoise
def combinePrimes(a,b):
    return(primeCheckII.PrimeCheck(int(str(a)+str(b))) and primeCheckII.PrimeCheck(int(str(b)+str(a))))


UNIQUE_PRIMES = 5
MIN_SUM = 792
p_dict = {x: p for x,p in enumerate(primeCheckII.primes(3,673))}

def primePairSets(a_0,p_dict ):
    for a in primeCheckII.primes(a_0):
        print(a)
        ab_list = []
        for i_b in range(len(p_dict)):
            b = p_dict[i_b]
            if combinePrimes(b,a):
                ab_list.append(b)
        while len(ab_list) > 3:
            b = ab_list.pop(0)
            print("\t",b)
            bc_list = []
            for c in ab_list:
                if combinePrimes(b,c):
                    bc_list.append(c)
            while len(bc_list) > 2:
                c = bc_list.pop(0)
                print("\t\t",c)
                cd_list = []
                for d in bc_list:
                    if combinePrimes(c,d):
                        cd_list.append(d)
                while len(cd_list) > 1:
                    d = cd_list.pop(0)
                    print("\t\t\t",d)
                    for e in cd_list:
                        if combinePrimes(d,e):
                            return([b,c,d,e,a])
        p_dict[len(p_dict)] = a

            
a_0 = 673
result = primePairSets(a_0,p_dict)

print(result)
total = 0
for x in result:
    total += x
print(total)

