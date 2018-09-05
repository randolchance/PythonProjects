# PROJECT EULER PROBLEM 120 - Square Remainders

# First thing to note is that even values of n will always yield a remainder
# of 2, while odd powers will always yield 2*n*a. All other bigger powers
# of a are evenly divisible by a^2
# Thus odd values of n will always yield rmax and are the only ones worth
# considering
# Also when n == a, r = 0, and n == a+1 is the same as n == 1, however,
# if n is even and a is odd then n has to range to 2a in order to catch
# all possible vaues of r

def f(a,n):
    return((a-1)**n + (a+1)**n)

sum_rmax = 0
for a in range(3,1001):
    rmax = 2
    for n in range(1,2*a):
        if n%2 == 0: continue
        r = 2*n*a % a**2
        rmax = rmax if r < rmax else r
    sum_rmax += rmax

print(sum_rmax)

