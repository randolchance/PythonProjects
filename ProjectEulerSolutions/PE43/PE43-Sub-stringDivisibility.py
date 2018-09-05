# PROJECT EULER PROBLEM 43 - Sub-string Divisibility


from primeCheckII import primes
from permutations import permutation

GOOD3 = [0,2,4,6,8]
GOOD5 = [0,5]

prime_list = [p for p in primes(2,18)]

results = []
for digit3 in GOOD3:
    digit_list = [x for x in range(10)]
    new_num = ['X' for x in range(10)]
    new_num[3] = digit3
    digit_list.remove(digit3)
    for digit5 in GOOD5:
        new_digit_list = digit_list[:]
        if digit3 == digit5:
            continue
        new_num[5] = digit5
        new_digit_list.remove(digit5)
        for p in permutation(new_digit_list,len(new_digit_list)):
            num = ''
            for d in new_num:
                if d == 'X':
                    num += str(p.pop(0))
                else:
                    num += str(d)

            good_num = True
            for d in range(1,8):
                val = int(num[d:d+3])
                if val%prime_list[d-1] != 0:
                    good_num = False
                    break
            if good_num:
                results.append(int(num))

print(results)
total = 0
for r in results:
    total += r

print(total)

