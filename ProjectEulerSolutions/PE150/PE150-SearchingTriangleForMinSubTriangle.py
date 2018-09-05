# PROJECT EULER PROBLEM 150 - Searching a Triangular Array for a Sub-triangle Having Minimum-sum

def makeTri(size):
    new_tri = []
    t = 0
    K = -2**19
    a = 615949
    b = 797807
    z = 2**20
    for n in range(size):
        new_row = []
        for c in range(n+1):
            t = (a*t+b) % z
            s = t + K
            new_row.append(s)
        new_tri.append(new_row)
    return(new_tri)


tri = makeTri(1000)


minimum_tri = 0
tri_dict = {}

for l in range(1001):
    for r in range(len(tri)-l):
        new_cell_sum = sum(tri[r+l][:l+1])
        for c in range(len(tri[r])):
            if l == 0:
                S = tri_dict[(r,c)] = tri[r][c]
            else:
                if c > 0:
                    new_cell_sum = new_cell_sum - tri[r+l][c-1] + tri[r+l][c+l]
                S = tri_dict[(r,c)] + new_cell_sum
                tri_dict[(r,c)] = S
            minimum_tri = minimum_tri if minimum_tri < S else S
    #print(l)

print(minimum_tri)

