# PROJECT EULER PROBLEM 15 - Lattice Paths

from memoise import Memoise

GRID_N = 20
GRID_DX = GRID_N
GRID_DY = GRID_N
TOTAL_STEPS = GRID_DX + GRID_DY

@Memoise
def steps(x,y,remaining_steps):
    print(x,y)
    count = 0
    if remaining_steps == 0:
        return(0)
    # At a wall, there is only one path left to the bottom right corner
    if x == 0 or y == 0:
        return(1)
    
    # True = step right, False = step down
    for s in [True,False]:
        count += steps(x-s,y-(not s),remaining_steps-1)
    return(count)


print(steps(GRID_DX,GRID_DY,TOTAL_STEPS))

