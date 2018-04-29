"""
PROJECT EULER PROBLEM 52 - Permuted Multiples
It can be seen that the number, 125874, and its double, 251748,
contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
"""

from collections import Counter

multiples = (2,3,4,5,6)

def permuteMultiples(start_val,end_val,multiple_list):
    x_0 = start_val
    x_f = end_val
    for x in range(x_0,x_f+1):
        x_list = [str(x)] + [str(x*i) for i in multiple_list]
        digit_list = []
        for s in x_list:
            digit_list.append(sorted([int(d) for d in s]))
        #print(digit_list)
        skip = False
        for i,d in enumerate(digit_list):
            if i == 0:
                continue
            if Counter(digit_list[0]) != Counter(d):
                skip = True
                break
        if not skip:
            return(x)

print(permuteMultiples(1,142857,multiples))
