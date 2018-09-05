# PROJECT EULER PROBLEM 346 - Strong Repunits


MAX_K = 10**12
MAX_K = 1000

n = 2
repunit_dict = {1:1}
while n**2 < MAX_K:
    K = 0
    m = 0
    while K + n**m < MAX_K:
        K += n**m
        if m >= 2:
            if K not in repunit_dict:
                repunit_dict[K] = n
        m += 1
    #if m == 1: break
    #print(n,K)
    n += 1

print(len(repunit_dict))

total = 0
for key in repunit_dict.keys():
    total += key

print(total)

