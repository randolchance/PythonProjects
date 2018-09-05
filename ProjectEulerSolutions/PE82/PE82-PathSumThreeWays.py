# PROJECT EULER PROBLEM 82 - Path Sum: Three Ways

matrix = []
with open('p082_matrix.txt') as file:
    for line in file:
        line = line.rstrip("\n")
        row = line.split(",")
        matrix.append([int(r) for r in row])

# TEST MATRIX
#matrix = [[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]


result = 0
SIZE = len(matrix)

for c in range(SIZE-2,-1,-1):
    next_col = []
    for r in range(SIZE):
        #print(c,r)
        new_col = [matrix[j][c+1] for j in range(SIZE)]
        for j in range(SIZE):
            if j < r:
                new_col[j] += sum([matrix[J][c] for J in range(j,r)])
            elif j > r:
                new_col[j] += sum([matrix[J][c] for J in range(r+1,j+1)])
        next_col.append(matrix[r][c] + min(new_col))
    for j,row in enumerate(matrix):
        row.pop()
        row[-1] = next_col[j]

final_list = []
for row in matrix:
    final_list.append(row[0])
result = min(final_list)

print(result)

