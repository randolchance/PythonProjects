# PROJECT EULER PROBLEM 53 - Combinatoric Selections

from combinations import nCr

threshold = 1000000
count = 0
count_list = []
for n in range(1,101):
    for r in range(1,n+1):
        result = nCr(n,r)
        if result > threshold:
            count += 1
            count_list.append([n,r,nCr])
print(count)
            
            
