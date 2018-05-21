A row measuring seven units in length has red blocks with a minimum
length of three units placed on it, such that any two red blocks
(which are allowed to be different lengths) are separated by at least
one black square. There are exactly seventeen ways of doing this.

How many ways can a row measuring fifty units in length be filled?

NOTE: Although the example above does not lend itself to the
possibility, in general it is permitted to mix block sizes.
For example, on a row measuring eight units in length you
could use red (3), black (1), and red (4).
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

print(countBlockPermutations(7,3)+1)

