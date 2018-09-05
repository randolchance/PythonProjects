# PROJECT EULER PROBLEM 50 - Consecutive Prime Sum


import primeCheckII

MAX_p = 1000000

prime_list = []
with open("primes.txt") as file:
    for line in file:
        p = int(line.rstrip("\n"))
        if p > MAX_p:
            break
        prime_list.append(p)


min_run_len = 22

run_len = min_run_len
prime_sum = 0
for i in range(len(prime_list)):
    if prime_sum + prime_list[i] < MAX_p:
        prime_sum += prime_list[i]
    else:
        run_len = i+1




i = 0
run = True
run_list = []
prime_sum = 0
while run:
    run_list = prime_list[i:i+run_len]
    prime_sum = sum(run_list)
    if prime_sum > MAX_p:
        i = 0
        run_len -= 1
    elif primeCheckII.PrimeCheck(prime_sum):
        run = False
    else:
        i += 1
    print(i,run_len)

print(prime_sum, len(run_list), run_list)

