"""
PROJECT EULER PROBLEM 143 - Investigating the Torticelli Point of a Triangle
Let ABC be a triangle with all interior angles being less than 120 degrees.
Let X be any point inside the triangle and let XA = p, XC = q, and XB = r.

Fermat challenged Torricelli to find the position of X such that p + q + r
was minimised.

Torricelli was able to prove that if equilateral triangles AOB, BNC and AMC
are constructed on each side of triangle ABC, the circumscribed circles of
AOB, BNC, and AMC will intersect at a single point, T, inside the triangle.
Moreover he proved that T, called the Torricelli/Fermat point, minimises
p + q + r. Even more remarkable, it can be shown that when the sum is
minimised, AN = BM = CO = p + q + r and that AN, BM and CO also intersect
at T.

If the sum is minimised and a, b, c, p, q and r are all positive integers
we shall call triangle ABC a Torricelli triangle. For example, a = 399,
b = 455, c = 511 is an example of a Torricelli triangle, with
p + q + r = 784.

Find the sum of all distinct values of p + q + r ≤ 120000 for Torricelli
triangles.
"""


from math import sqrt

sum_dict = {}
total = 0
MAX_S = 120000
for c in range(2,120000):
    for p in range(1,int(c/sqrt(3))+1):
        n = sqrt(4*c**2-3*p**2)
        if (n-p)%2==0:
            r = int((n-p)/2)
            if p+r > MAX_S-p:
                break
            for q in range(p,r+1):
                s = p+q+r
                if s > MAX_S:
                    break
                b = sqrt(p**2+q**2+p*q)
                if b%1 == 0:
                    b = int(b)
                    a = sqrt(q**2+r**2+q*r)
                    if a%1 == 0:
                        a = int(a)
                        k = 1
                        P = p
                        S = s
                        #print(a,b,c)
                        while S <= MAX_S:
                            if S not in sum_dict:
                                sum_dict[S] = True
                                print(k*p,k*q,k*r," ",S)
                            total += S
                            k += 1
                            S = k*s
                            P = k*p

print(total)
# 136960903 WRONG
