# PROJECT EULER PROBLEM 67 - Maximum Path Sum II

triangle = []
with open('p067_triangle.txt') as file:
    for line in file:
        line = line.rstrip("\n")
        row = line.split(" ")
        triangle.append([int(r) for r in row])


result = 0
rows = len(triangle)
for r in range(rows-2,-1,-1):
    row = triangle.pop()
    for i in range(len(triangle[r])):
        triangle[r][i] += max([row[i],row[i+1]])
    print(triangle[r])
    if r == 0:
        result = triangle[0][0]

print(result)

