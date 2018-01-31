dim = input().split(",")
X = int(dim[0])
Y = int(dim[1])

list_array_Y = []

for y in range(Y):
    list_array_X = []
    for x in range(X):
        list_array_X.append(x*y)
    list_array_Y.append(list_array_X)

print(list_array_Y)

"""ALTERNATELY"""

multilist = [[0 for x in range(X)] for y in range(Y)]

for y in range(Y):
    for x in range(X):
        multilist[y][x] = x*y

print(multilist)
