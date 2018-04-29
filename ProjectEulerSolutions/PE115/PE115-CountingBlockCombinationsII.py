"""
PROJECT EULER 115 - Counting Block Combinations II
NOTE: This is a more difficult version of Problem 114.

A row measuring n units in length has red blocks with a minimum length
of m units placed on it, such that any two red blocks (which are allowed
to be different lengths) are separated by at least one black square.

Let the fill-count function, F(m, n), represent the number of ways that
a row can be filled.

For example, F(3, 29) = 673135 and F(3, 30) = 1089155.

That is, for m = 3, it can be seen that n = 30 is the smallest value for
which the fill-count function first exceeds one million.

In the same way, for m = 10, it can be verified that F(10, 56) = 880711
and F(10, 57) = 1148904, so n = 57 is the least value for which the
fill-count function first exceeds one million.

For m = 50, find the least value of n for which the fill-count function
first exceeds one million.
"""

from memoise import Memoise

@Memoise
def countBlockPermutations(total_cell_count,block_min_size):
    combo_count = 0
    for i in range(0,total_cell_count):
        remaining_cell_count = total_cell_count - i
        if remaining_cell_count >= block_min_size:
            for j in range(block_min_size,remaining_cell_count+1):
                combo_count += 1
                new_remaining_cell_count = remaining_cell_count - j
                if new_remaining_cell_count > block_min_size:
                    combo_count += countBlockPermutations(new_remaining_cell_count-1,block_min_size)
    return(combo_count)

block_min_size = 50
total_cell_count = 50
threshold = 1000000
while True:
    permutations = countBlockPermutations(total_cell_count,block_min_size)
    if permutations >= threshold:
        break
    total_cell_count += 1
print(permutations, total_cell_count)
"""
1053388; n = 168 CORRECT
"""
