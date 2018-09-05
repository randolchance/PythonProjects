# PROJECT EULER PROBLEM 297 - Zeckendorf Representation

from memoise import Memoise

@Memoise
def fib(n):
    return(1 if n <= 1 else fib(n-2)+fib(n-1))

@Memoise
def fibComboCount(max_tuple):
    if len(max_tuple) == 0:
        return((0,0))
    else:
        total = 1
        ways = 1
        max_list = list(max_tuple)
        I = max_list.pop()
        for i in range(I,I-2,-1):
            L = max_list if i == I else [j for j in range(i%2==1,i+1,2)]
            if not L: continue
            C = fibComboCount(tuple(L))
            total += C[1] + (C[0] if i == I else 0)
            ways += C[0]
        return((ways,total))



M = 10**17

# Really all this does is find the number of fib numbers under M
n = 1
F = fib(n)
fib_list = []
while F < M:
    fib_list.append(F)
    n += 1
    F = fib(n)
fib_tuple = tuple(fib_list)

# Create a list of the indexes in fib_list that generate the largest
# possible number under M
max_fib_list = []
m = M
i = len(fib_list)-1
while i >= 0:
    F = fib_list[i]
    if m > F:
        m -= F
        i -= 2
        max_fib_list.append(F)
    else:
        i -= 1
max_fib_index_list = [fib_list.index(F) for F in max_fib_list]
max_fib_index_list.reverse()


print(fibComboCount(tuple(max_fib_index_list))[1])

