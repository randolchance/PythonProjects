from collections import Counter


def cubicPermutations(i):
    while True:
        i += 1
        str_i = str(i**3)
        count_i = Counter(str_i)
        len_i = len(str_i)
        j = i
        while True:
            j += 1
            str_j = str(j**3)
            if len(str_j) > len_i:
                break
            if Counter(str_j) == count_i:
                k = j
                while True:
                    k += 1
                    str_k = str(k**3)
                    if len(str_k) > len_i:
                        break
                    if Counter(str_k) == count_i:
                        l = k
                        while True:
                            l += 1
                            str_l = str(l**3)
                            if len(str_l) > len_i:
                                break
                            if Counter(str_l) == count_i:
                                m = l
                                while True:
                                    m += 1
                                    str_m = str(m**3)
                                    if len(str_m) > len_i:
                                        break
                                    if Counter(str_m) == count_i:
                                        return([i,j,k,l,m])


i = 345
result = cubicPermutations(i)

#answer = [5027, 7061, 7202, 8288, 8384]

# VERIFY
for i in range(1,len(result)):
    check = Counter(str(result[0]**3))
    if Counter(str(result[i]**3)) == check:
        print(f"Verified! {result[i]}")
ANSWER = result[0]**3

print(f"The smallest cube with 5 cubic permutations of its digits is {ANSWER}!")
