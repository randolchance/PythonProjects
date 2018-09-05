# PROJECT EULER PROBLEM 45 - Triangular, Pentagonal, and Hexagonal

from math import sqrt

def quadSolver(a,b,c):
    in_sqrt = b**2 - 4*a*c
    if in_sqrt < 0:
        return(["Non-real roots!"])
    return([(-b-sqrt(in_sqrt))/2/a,(-b+sqrt(in_sqrt))/2/a])

def TriNum(n):
    return(int(n*(n+1)/2))
def Square(n):
    return(int(n**2))
def PentNum(n):
    return(int(n*(3*n-1)/2))
def HexNum(n):
    return(int(n*(2*n-1)))


#Pfn = [A,B] for use in the quadSolver
Pfn = [[] for x in range(7)]
Pfn[3] = [1/2,1/2]
Pfn[4] = [1,0]
Pfn[5] = [3/2,-1/2]
Pfn[6] = [2,-1]

P = [None for x in range(7)]
P[3] = TriNum
P[4] = Square
P[5] = PentNum
P[6] = HexNum


n = 286
while True:
    
    T = TriNum(n)
    if quadSolver(Pfn[5][0],Pfn[5][1],-T)[1]%1 == 0 and quadSolver(Pfn[6][0],Pfn[6][1],-T)[1]%1 == 0:
        print(T)
        break
    n += 1
    
