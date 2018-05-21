# PROJECT EULER PROBLEM 44 - Pentagon Numbers


from math import sqrt

def P(n):
    return(int(n*(3*n-1)/2))

def iP(i,j):
    for n in range(i,j+1):
        yield(P(n))


A = 3/2
B = -1/2

def quadSolver(a,b,c):
    in_sqrt = b**2 - 4*a*c
    if in_sqrt < 0:
        return(["No real roots!"])
    else:
        return([(-b-sqrt(in_sqrt))/2/a,(-b+sqrt(in_sqrt))/2/a])

def isP(p):
    roots = quadSolver(A,B,-p)
    if len(roots) > 1:
        for i in roots:
            if i > 0 and i%1 == 0:
                return(True)
    return(False)


P_list = []
maxN = 4999
maxPs = int(quadSolver(A,B,-(P(maxN) + P(maxN+1)))[1])
result_list = []
for i in range(0,maxPs+1):
    P_list.append(P(i+1))

breakLoop = False
for i in range(1,maxN):
    for j in range(i+1,maxN+1):
        P_i = P_list[i]
        P_j = P_list[j]
        dP = P_j - P_i
        sP = P_j + P_i
        for item in result_list:
            if i == j-1 and dP > item:
                breakLoop = True
                break
        if isP(dP) and isP(sP):
            result_list.append(dP)
            print([i,P_i,j,P_j,dP,sP])
    if breakLoop:
        break

