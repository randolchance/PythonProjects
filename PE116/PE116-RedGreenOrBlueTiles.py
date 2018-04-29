"""
PROJECT EULER 116 - Red, Green, or Blue Tiles
A row of five black square tiles is to have a number of its tiles
replaced with coloured oblong tiles chosen from red (length two),
green (length three), or blue (length four).

If red tiles are chosen there are exactly seven ways this can be done.

If green tiles are chosen there are three ways.

And if blue tiles are chosen there are two ways.
	
Assuming that colours cannot be mixed there are 7 + 3 + 2 = 12 ways of
replacing the black tiles in a row measuring five units in length.

How many different ways can the black tiles in a row measuring fifty
units in length be replaced if colours cannot be mixed and at least one
coloured tile must be used?
"""

from memoise import Memoise

RED = 2
GREEN = 3
BLUE = 4

@Memoise
def countBlockPermutations(total_cell_count,colour):
    combo_count = 0
    for i in range(0,total_cell_count):
        remaining_cell_count = total_cell_count - i
        if remaining_cell_count >= colour:
            combo_count += 1
            new_remaining_cell_count = remaining_cell_count - colour
            if new_remaining_cell_count >= colour:
                combo_count += countBlockPermutations(new_remaining_cell_count,colour)
    return(combo_count)

total_cell_count = 5
count = 0
for colour in [RED,GREEN,BLUE]:
    add_count = countBlockPermutations(total_cell_count,colour)
    print(colour,add_count)
    count += add_count
print(count)

"""
For 50 cells:
RED(2) = 20365011073
GREEN(3) = 122106096
BLUE(4) =  5453760
TOTAL(R+G+B) = 20492570929
CORRECT
"""
