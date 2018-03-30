"""
PROJECT EULER PROBLEM 111 - Primes With Runs
Considering 4-digit primes containing repeated digits it is clear
that they cannot all be the same: 1111 is divisible by 11, 2222 is
divisible by 22, and so on. But there are nine 4-digit primes
containing three ones:

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

We shall say that M(n, d) represents the maximum number of repeated
digits for an n-digit prime where d is the repeated digit, N(n, d)
represents the number of such primes, and S(n, d) represents the sum
of these primes.

So M(4, 1) = 3 is the maximum number of repeated digits for a 4-digit
prime where one is the repeated digit, there are N(4, 1) = 9 such
primes, and the sum of these primes is S(4, 1) = 22275. It turns out
that for d = 0, it is only possible to have M(4, 0) = 2 repeated
digits, but there are N(4, 0) = 13 such cases.

In the same way we obtain the following results for 4-digit primes.

Digit, d	M(4, d)	N(4, d)	S(4, d)
0	2	13	67061
1	3	9	22275
2	3	1	2221
3	3	12	46214
4	3	2	8888
5	3	1	5557
6	3	1	6661
7	3	9	57863
8	3	1	8887
9	3	7	48073
For d = 0 to 9, the sum of all S(4, d) is 273700.

Find the sum of all S(10, d).
"""
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
"""612407567715"""
