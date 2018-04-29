"""
PROJECT EULER PROBLEM 102 - Triangle Containment

Three distinct points are plotted at random on a Cartesian plane,
for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas
triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a
27K text file containing the co-ordinates of one thousand "random"
triangles, find the number of triangles for which the interior
contains the origin.

NOTE: The first two examples in the file represent the triangles
in the example given above.
"""

from operator import itemgetter

def readTriangles():
    triangle_list = []
    with open("p102_triangles.txt") as file:
        for line in file:
            tris = line.rstrip("\n")
            tris = tris.split(",")
            point_list = []
            for i in range(0,3):
                point_list.append([ tris[2*i], tris[2*i+1] ])
            triangle_list.append(point_list)
    #return(triangle_list)
    for triangle in triangle_list:
        yield(triangle)

X = 0
Y = 1

def computeLine(A,B):
    a_x = int(A[X])
    a_y = int(A[Y])
    b_x = int(B[X])
    b_y = int(B[Y])
    dy = a_y - b_y
    dx = a_x - b_x
    m = dy/dx if (dx!=0) else 'inf'
    b = a_y - m*a_x if m!='inf' else 'DNE'
    return([[a_x,a_y],[b_x,b_y],dy,dx,m,b])

def isBetween(x,i,f):
    if type(x) is str:
        return False
    return( (i >= x and x >= f) or (i <= x and x <= f) )

start = 0
end = 1
DY = 2
DX = 3
M = 4
B = 5

count = 0
for i,triangle in enumerate(readTriangles()):
    contains_origin = False
    a = triangle[0]
    b = triangle[1]
    c = triangle[2]
    ab = computeLine(a,b)
    bc = computeLine(b,c)
    ca = computeLine(c,a)
    line_list = []
    for line in [ab,bc,ca]:
        if isBetween(line[B], line[start][Y], line[end][Y]):
            line_list.append(line)
    if line_list:
        if isBetween(0, line_list[0][B], line_list[1][B]):
            contains_origin = True
            count += 1
    #print(i,triangle,contains_origin)
print(count)

# 228 CORRECT
