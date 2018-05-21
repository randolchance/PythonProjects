Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring
two units, green tiles measuring three units, and blue tiles measuring four units, it is
possible to tile a row measuring five units in length in exactly fifteen different ways.

How many ways can a row measuring fifty units in length be tiled?
from memoise import Memoise

RED = 2
GREEN = 3
BLUE = 4

@Memoise
def countBlockPermutations(total_cell_count):
    combo_count = 0
    for i in range(0,total_cell_count):
        remaining_cell_count = total_cell_count - i
        for colour in [RED,GREEN,BLUE]:
            if remaining_cell_count >= colour:
                combo_count += 1
                new_remaining_cell_count = remaining_cell_count - colour
                if new_remaining_cell_count >= RED:
                    combo_count += countBlockPermutations(new_remaining_cell_count)
    return(combo_count)

total_cell_count = 50
count = countBlockPermutations(total_cell_count)+1
print(count)

100808458960497
