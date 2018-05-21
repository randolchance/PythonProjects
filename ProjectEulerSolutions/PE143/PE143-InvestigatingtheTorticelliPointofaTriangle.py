# PROJECT EULER PROBLEM 143 - Investigating the Torticelli Point of a Triangle


from math import sqrt

sum_dict = {}
total = 0
MAX_S = 120000
for c in range(2,120000):
    for p in range(1,int(c/sqrt(3))+1):
        n = sqrt(4*c**2-3*p**2)
        if (n-p)%2==0:
            r = int((n-p)/2)
            if p+r > MAX_S-p:
                break
            for q in range(p,r+1):
                s = p+q+r
                if s > MAX_S:
                    break
                b = sqrt(p**2+q**2+p*q)
                if b%1 == 0:
                    b = int(b)
                    a = sqrt(q**2+r**2+q*r)
                    if a%1 == 0:
                        a = int(a)
                        k = 1
                        P = p
                        S = s
                        #print(a,b,c)
                        while S <= MAX_S:
                            if S not in sum_dict:
                                sum_dict[S] = True
                                print(k*p,k*q,k*r," ",S)
                            total += S
                            k += 1
                            S = k*s
                            P = k*p

print(total)
# 136960903 WRONG
