# PROJECT EULER PROBLEM 85 - Counting Rectangles


def countRectangles(m,n):
    if n == 0 or m == 0:
        raise ValueError("You know how rectangles work, right?")
    total = 0
    for j in range(n,0,-1):
        for i in range(m,0,-1):
            total += i*j
    return(total)


target = 2000000
closest = target
solution = []
p = 5
while True:
    max_m = p//2
    p_rects_dict = {}
    for m in range(1,max_m+1):
        n = p-m
        r = countRectangles(m,n)
        p_rects_dict[r] = [m,n]
        #print(m,n,r)
    for r in p_rects_dict.keys():
        diff = target-r
        if abs(diff) < closest:
            closest = abs(diff)
            solution = p_rects_dict[r]
    if all([abs(target-r) > 20*closest for r in p_rects_dict.keys()]):
        break
    p += 1

print(solution,closest)
print("AREA = ", solution[0]*solution[1])


