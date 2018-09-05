# PROJECT EULER PROBLEM 7 - 10001st Prime

from primeCheckII import primes

count = 1
max_count = 10001
for p in primes():
    if count == max_count:
        print(p)
        break
    count += 1

