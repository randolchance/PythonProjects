# PROJECT EULER PROBLEM 188 - The Hyperexponentiation of a Number


import sys

sys.setrecursionlimit(2000)

Z = 10**8

def tetrate(a,k,Z):
    if k == 1:
        return(a)
    x = pow(a,tetrate(a,k-1,Z),Z)
    return(x)

x = tetrate(1777,1855,Z)
print(x)

# Apparently after about 4/1855 it yields the correct last 8 digits for every
# recursion thereafter. I've not thought particularly hard about why that is

