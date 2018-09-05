# PROJECT EULER PROBLEM 6 - Sum Square Difference

max_n = 100
nsum = 0
nsquared_sum = 0
for n in range(1,max_n+1):
    nsum += n
    nsquared_sum += n**2
nsum_squared = nsum**2
print(nsum_squared,nsquared_sum,nsum_squared - nsquared_sum)

