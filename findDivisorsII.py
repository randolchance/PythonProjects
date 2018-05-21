from findFactorsII import findFactors
from memoise import Memoise

@Memoise
def findDivisors(factors, incl_one=True, incl_total=True):
    if not factors:
        return([])
    divisors = []
    if incl_one:
        divisors = [1]
    if type(factors) is int:
        if incl_total:
            divisors.append(factors)
        factors = findFactors(factors)
    elif type(factors) is tuple:
        if incl_total:
            t = 1
            for f in factors:
                t *= f
            divisors.append(t)
        new_factors = []
        for f in factors:
            new_factors += findFactors(f)
        factors = new_factors
    else:
        raise ValueError("Expected tuple or int")
    if len(factors) == 1:
        return(divisors)
    checked_dict = {}
    for i,f in enumerate(factors):
        if f in checked_dict:
            continue
        checked_dict[f] = True
        new_factors = factors[:i]+factors[i+1:]
        divisors += [f]+findDivisors(tuple(new_factors),False,True)

    return(sorted(list(set(divisors))))
