"""
PROJECT EULER PROBLEM 58 - Spiral Primes
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom
right diagonal, but what is more interesting is that 8 out of the 13
numbers lying along both diagonals are prime; that is, a ratio of
8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a
square spiral with side length 9 will be formed. If this process
is continued, what is the side length of the square spiral for
which the ratio of primes along both diagonals first falls below 10%?
"""

"""
The next four corner numbers obey the rules:
TR: previousBR + size-1
TL: TR + size-1
BL: TL + size-1
BR: BL + size-1
then increase size by 2
"""

from math import sqrt

from primeCheck import isPrime


size = 1
ratio = 1.0
check_list = []
TR = TL = BL = BR = 1
prime_count = 0
while ratio >= 0.1:
    size += 2
    TR = BR + size-1
    TL = TR + size-1
    BL = TL + size-1
    BR = BL + size-1
    check_list = [TR,TL,BL,BR]
    total = 2*(size-1) + 1
    for x in check_list:
        if isPrime(x):
            prime_count += 1
    ratio = prime_count / total
print(prime_count,total,ratio,size)









