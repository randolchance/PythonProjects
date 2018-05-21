# PROJECT EULER PROBLEM 111 - Primes With Runs
from primeCheck import isPrime
from collections import Counter

numbers = [x for x in range(0,10)]

def bitList(x,n):
    # NOTE: The additional -1 in the range is to omit masks with all 1s
    for i in range(1,(2<<(x-1))-1):
        out = str(bin(i)).lstrip("0b")
        while len(out) < x:
            out = "0"+out
        out = list(out)
        if Counter(out)['0'] == n:
            yield(out)

prime_dict = {}
result = 0
for i in range(0,10):
    for n in range(9,1,-1):
        prime_list = []
        for bits in bitList(10,n):
            if ((i%2==0) or (i==5)) and (bits[len(bits)-1]=='0'):
                continue
            if (i==0 and bits[0]=='0'):
                continue
            for j in range(0,10**(10-n)):
                #print(n,i,j)
                if ((j%2==0) or (j==5)) and (bits[len(bits)-1]=='1'):
                    continue
                J = str(j)
                while len(J) < (10-n):
                    J = '0'+J
                skip_j = False
                for jj in range(len(J)):
                    if int(J[jj]) == i:
                        skip_j = True
                        break
                if skip_j:
                    continue
                if (J[0]=='0' and bits[0]=='1'):
                    continue
                out_str = ''
                for bit in bits:
                    if bit == '0':
                        out_str += str(i)
                    else:
                        out_str += J[0:1]
                        J = J[1:]
                    out_val = int(out_str)
                if isPrime(out_val):
                    print(out_val)
                    prime_list.append(out_val)
                    result += out_val
        if len(prime_list) != 0:
            break
    prime_dict[i] = prime_list
print(result)
