"""
PROJECT EULER PROBLEM 147 - Rectangles in Cross-hatched Grid
In a 3x2 cross-hatched grid, a total of 37 different rectangles could
be situated within that grid as indicated in the sketch.

There are 5 grids smaller than 3x2, vertical and horizontal dimensions
being important, i.e. 1x1, 2x1, 3x1, 1x2 and 2x2. If each of them is
cross-hatched, the following number of different rectangles could be
situated within those smaller grids:

1x1: 1 
2x1: 4 
3x1: 8 
1x2: 4 
2x2: 18

Adding those to the 37 of the 3x2 grid, a total of 72 different
rectangles could be situated within 3x2 and smaller grids.

How many different rectangles could be situated within 47x43 and
smaller grids?
"""

def countAllRectangles(M,N):
    count = 0
    for m in range(1,M+1):
        for n in range(1,N+1):
            for dx in range(1,m+1):
                for dy in range(1,n+1):
                    count += (m-dx+1)*(n-dy+1)
    return(count)

def makeDiagGrid(M,N):
    if M < 2 and N < 2:
        return(None)
    elif (N==1 and M>1):
        return(M-1)
    elif (N==1 and M>1):
        return(N-1)
    D = (M-1)+(N-1)
    diagGrid = []
    for j in range(D):
        row = []
        for i in range(D):
            row.append(not (i < (N-2-j) or i >= (D-(M-2-j)) or i <= (M-2-(D-j)) or i > (D-j+(D-N))))
        diagGrid.append(row)
    return(diagGrid)

def countDiagRectangles(diagGrid):
    D = len(diagGrid)
    count = 0
    for dy in range(1,D+1):
        for dx in range(1,dy+1):
            for j in range(0,D-(dy-1)):
                free = False
                next_false_abort = False
                for i in range(0,D-(dx-1)):
                    if free:
                        next_false_abort = True
                    free = True
                    for dy_j in range(0,dy):
                        for dx_i in range(0,dx):
                            try:
                                if diagGrid[j+dy_j][i+dx_i] == False:
                                    free = False
                                    break
                            except:
                                free = False
                                break
                        if not free:
                            break
                    if free:
                        count += 1 + int(dy!=dx)
                    else:
                        if next_false_abort:
                            break
    return(count)
            
try:
    MAX_M = 47
    MAX_N = 43
    count = 0
    for M in range(1,MAX_M+1):
        max_N = M if M < MAX_N else MAX_N
        for N in range(1,max_N+1):
            print(M,N)
            diagGrid = makeDiagGrid(M,N)
            if diagGrid != None:
                factor = 2 if (N < M and M <= MAX_N) else 1
                if type(diagGrid) == list:
                    count += factor*countDiagRectangles(diagGrid)
                else:
                    count += factor*diagGrid
    count += countAllRectangles(MAX_M,MAX_N)
except:
    print("aborted at: ", M,N,count)
print(count)

# 846910284 CORRECT
