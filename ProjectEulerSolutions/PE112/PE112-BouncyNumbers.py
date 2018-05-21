# PROJECT EULER PROBLEM 112 - Bouncy Numbers

def isBouncy(n):
    sN = str(n)
    isBouncy = False
    for i in range(len(sN)-2):
        for j in range(i+1,len(sN)-1):
            for k in range(j+1,len(sN)):
                if (int(sN[i]) > int(sN[j]) and int(sN[j]) < int(sN[k])) or (int(sN[i]) < int(sN[j]) and int(sN[j]) > int(sN[k])):
                    return True
    return False
    

bouncy = 0
not_bouncy = 0
n = 1
while True:
    is_n_bouncy = isBouncy(n)
    if is_n_bouncy:
        bouncy += 1
    else:
        #print(n)
        not_bouncy += 1
    ratio = bouncy/(bouncy+not_bouncy)
    #if n%1000 == 0:
    #    print(n,is_n_bouncy)
    #    print(ratio)
    #if n == 999999:
    #    print(not_bouncy)
    #    break
    if ratio >= 0.99:
        print("FINAL: ", n, is_n_bouncy)
        print(ratio)
        break
    n += 1
"""
FINAL:  1587000 True
0.99
"""
