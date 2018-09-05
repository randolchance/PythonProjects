# PROJECT EULER PROBLEM 119 - Digit Power Sum

def sumDigits(n):
    return(sum([int(s) for s in str(n)]))

result_list = []
d = 2
while len(result_list) < 30:
    min_N = 10**(d-1)
    max_N = 10**d
    sumSet = {i for i in range(2,9*d+1)}
    for n in sumSet:
        i = 2
        while True:
            N = n**i
            if N >= min_N and N < max_N:
                if n == sumDigits(N):
                    print(n,i,N)
                    result_list.append(N)
            elif N >= max_N: break 
            i += 1
    d += 1

print(sorted(result_list))

