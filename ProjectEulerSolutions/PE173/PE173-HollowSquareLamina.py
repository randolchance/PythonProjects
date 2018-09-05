# PROJECT EULER PROBLEM 173 - Hollow Square Lamina

tiles_max = 1000000

def f(n):
    return(4*(n-1))

n_max = tiles_max//4 + 1

count = 0
for n in range(3,n_max+1):
    T = tiles_max
    l_f = 4 if n%2 == 0 else 3
    for l in range(n,l_f-1,-2):
        T -= f(l)
        if T >= 0:
            count += 1
        else:
            break

print(count)

