# PROJECT EULER PROBLEM 30 - Digit Fifth Powers


from math import sqrt

max_n = 299999

results = []
for n in range(2,max_n+1):
    power5sum = sum([int(d)**5 for d in str(n)])
    if n == power5sum:
        results.append(n)

print(results)
total = 0
for n in results:
    total += n

print(total)

