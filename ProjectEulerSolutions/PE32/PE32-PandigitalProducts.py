# PROJECT EULER PROBLEM 32 - Pandigital Products
from permutations import permutation

digits = [i for i in range(1,10)]

final_result_dict = {}
product_sum = 0
for n in range(1,3):
    m = 5-n
    for p in permutation(digits,n):
        if p == [1]:
            continue
        new_digits = [x for x in digits if x not in p]
        for q in permutation(new_digits,m):
            r = [x for x in new_digits if x not in q]
            multiplicand = int("".join([str(i) for i in p]))
            multiplier = int("".join([str(i) for i in q]))
            result = multiplicand * multiplier
            if result > 9999:
                continue
            result_list = sorted([i for i in str(result)])
            if '0' in result_list:
                continue
            product_list = sorted([str(i) for i in r])
            if product_list == result_list:
                if result not in final_result_dict:
                    final_result_dict[result] = [multiplicand,multiplier]
                    product_sum += result

print(final_result_dict)
print(product_sum)

