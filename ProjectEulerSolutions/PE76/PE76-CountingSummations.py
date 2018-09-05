# PROJECT EULER PROBLEM 76 - Counting Summations


from memoiseII import Memoise

@Memoise
def findSums(N,n_0):
    if N == 0:
        yield(0)
    elif N == 1:
        yield(1)
    else:
        for n in range(n_0,0,-1):
            dn = N-n
            new_n_0 = min([dn,n])
            if dn == 0:
                yield(1)
            elif dn == 1:
                yield(1)
            else:
                count = 0
                for s in findSums(dn,new_n_0):
                    count += s
                yield(count)
        

count = 0
for s in findSums(100,100):
    print(s)
    count += s

print(count-1)

