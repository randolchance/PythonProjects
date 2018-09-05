# PROJECT EULER PROBLEM 96 - Su Doku

from copy import deepcopy

SIZE = 9
NUM_SET = {str(i) for i in range(1,SIZE+1)}


def initFreeNumbers(aPuzzle):
    for j in range(SIZE):
        for i in range(SIZE):
            if puzzle[j][i] == '0':
                row_set = {aPuzzle[j][x] for x in range(SIZE) if type(aPuzzle[j][x]) is str and aPuzzle[j][x] != '0'}
                col_set = {aPuzzle[y][i] for y in range(SIZE) if type(aPuzzle[y][i]) is str and aPuzzle[y][i] != '0'}
                box_x = i//3*3
                box_y = j//3*3
                box_set = set()
                for m in range(3):
                    for n in range(3):
                        num = aPuzzle[box_y+m][box_x+n]
                        if type(num) is str and num != '0':
                            box_set |= {num}
                aPuzzle[j][i] = NUM_SET - (row_set|col_set|box_set)
                
def checkNotComplete(aPuzzle):
    count = 0
    for j in aPuzzle:
        for i in j:
            if type(i) is set:
                count += 1
    return(count)

def checkBadGuess(aPuzzle):
    for j in range(SIZE):
        for i in range(SIZE):
            if not aPuzzle[j][i]:
                return(True)
    return(False)

def writeNumber(aPuzzle,num,i,j):
    aPuzzle[j][i] = num
    for x in range(SIZE):
        if type(aPuzzle[j][x]) is set:
            aPuzzle[j][x] -= {num}
    for y in range(SIZE):
        if type(aPuzzle[y][i]) is set:
            aPuzzle[y][i] -= {num}
    box_x = i//3*3
    box_y = j//3*3
    for m in range(3):
        for n in range(3):
            if type(aPuzzle[box_y+m][box_x+n]) is set:
                aPuzzle[box_y+m][box_x+n] -= {num}

def logicPuzzle(aPuzzle):
    for j in range(SIZE):
        for i in range(SIZE):
            if type(aPuzzle[j][i]) is set and len(aPuzzle[j][i]) == 1:
                num = list(aPuzzle[j][i])[0]
                writeNumber(aPuzzle,num,i,j)
                return




def solvePuzzle(puzzle):
    empty_squares = checkNotComplete(puzzle)
    while empty_squares:
        prev_empty_squares = empty_squares
        logicPuzzle(puzzle)
        if checkBadGuess(puzzle):
            return(None)
        empty_squares = checkNotComplete(puzzle)
        if prev_empty_squares == empty_squares:
            for j in range(SIZE):
                for i in range(SIZE):
                    if type(puzzle[j][i]) is set:
                        for num in puzzle[j][i]:
                            theory_puzzle = deepcopy(puzzle)
                            writeNumber(theory_puzzle,num,i,j)
                            new_puzzle = solvePuzzle(theory_puzzle)
                            if new_puzzle != None:
                                return(new_puzzle)
                        return(None)
            return(None)
    return(puzzle)
                            
    


puzzle_list = []
with open('p096_sudoku.txt') as file:
    puzzle = []
    for line in file:
        line = line.rstrip("\n")
        if not line.isnumeric():
            if puzzle:
                puzzle_list.append(puzzle)
            puzzle = []
        else:
            puzzle.append([s for s in line])
    puzzle_list.append(puzzle)



total = 0
for i,puzzle in enumerate(puzzle_list):
    print(i)
    initFreeNumbers(puzzle)
    puzzle = solvePuzzle(deepcopy(puzzle))
    for row in puzzle:
        print(row)
    print("\n")
    val = int("".join(puzzle[0][0:3]))
    total += val

print(total)

