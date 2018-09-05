# PROJECT EULER PROBLEM 149 - Searching for a Maximum-sum Subsequence


_i = 0
_j = 1

def kToij(size,k):
    if k <= 0 :
        raise ValueError("k cannot be less than 1!")
    j = (k-1)//size
    i = (k-1)%size
    return((i,j))


def LFG(size):
    LFG_array = [[None for i in range(size)] for j in range(size)]
    for k in range(1,size**2+1):
        ij = kToij(size,k)
        if k <= 55:
            LFG_array[ij[_j]][ij[_i]] = (100003 - 200003*k + 300007*k**3)%1000000 - 500000
        elif k > 55:
            ij_k24 = kToij(size,k-24)
            ij_k55 = kToij(size,k-55)
            LFG_array[ij[_j]][ij[_i]] = (LFG_array[ij_k24[_j]][ij_k24[_i]] + LFG_array[ij_k55[_j]][ij_k55[_i]] + 1000000)%1000000 - 500000
    return(LFG_array)

EW = 0
NS = 1
NWSE = 2
NESW = 3
DIRS = (EW,NS,NWSE,NESW)

def grabLines(aGrid,direction):
    size = len(aGrid)
    if direction == EW:
        for j in range(size):
            yield(aGrid[j])
    elif direction == NS:
        for i in range(size):
            yield([aGrid[j][i] for j in range(size)])
    elif direction == NWSE:
        for d in range(size-1,0,-1):
            yield([aGrid[l][d+l] for l in range(size-d)])
        for d in range(size):
            yield([aGrid[d+l][l] for l in range(size-d)])
    elif direction == NESW:
        for d in range(size-1):
            yield([aGrid[d-l][l] for l in range(d+1)])
        for d in range(size-1,-1,-1):
            yield([aGrid[(size-1)-l][(size-1)-d+l] for l in range(d+1)])

def findLineMaxSum(line):
    if len(line) == 1: return(line[0])
    else:
        M = max(line)
        prev_sum_list = line[:]
        for l in range(1,len(line)):
            for i in range(len(prev_sum_list)-1):
                prev_sum_list[i] += line[l+i]
            prev_sum_list.pop()
            M = max([M]+prev_sum_list)
        return(M)


SIZE = 2000

a = LFG(SIZE)


M = None
for d in DIRS:
    print("dir: ",d)
    for l,line in enumerate(grabLines(a,d)):
        print(l)
        S = findLineMaxSum(line)
        if M is None:
            M = S
        else:
            M = M if M > S else S
    print(M)
print(M)
        
