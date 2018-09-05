# PROJECT EULER PROBLEM 24 - Lexicographic Permutations

from permutations import permutation

digits = [x for x in range(10)]
for i,p in enumerate(permutation(digits,len(digits))):
    if i+1 == 1000000:
        x = int("".join([str(j) for j in p]))
        print(x)
        break

