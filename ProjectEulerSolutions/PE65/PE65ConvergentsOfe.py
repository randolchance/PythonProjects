# PROJECT EULER PROBLEM 65 - Convergents of e



from fractions import Fraction

MAX_TERMS = 100

k_seq = tuple([2]+[(1 if (x+2)%3 != 0 else 2*(x+2)//3) for x in range(99)])


def computeFraction(k_seq,max_terms,term=0):
    if term < max_terms:
        frac = Fraction(k_seq[term])
        yield(frac if k_seq[term]%1 != 0 else k_seq[term])
        for c in computeFraction(k_seq,max_terms,term+1):
            yield(frac+Fraction(1,c))


final_num = 0
for i,c in enumerate(computeFraction(k_seq,MAX_TERMS)):
    final_num = c.numerator if type(c) is Fraction else c
    print(i+1,c.numerator if type(c) is Fraction else c)
    
total = sum([int(s) for s in str(final_num)])
print(total)

