# PROJECT EULER PROBLEM 26 - Reciprocal Cycles


from bigfloat import *

REPEATS = 10

max_dkj = [1,0]
for i in range(2,1000):
    with precision(100*REPEATS*i):
        f = div(1,i)
        #print(i,f)
        str_f = str(f).lstrip('0.').lstrip('0')
        j = 0
        s = str_f[j]
        k = 1
        dkj = None
        while k < len(str_f):
            if s != str_f[k]:
                k += 1
            else:
                dkj = k-j
                try:
                    if all([str_f[n*dkj] == s for n in range(2,REPEATS+1)]):
                        max_dkj = [i,dkj] if dkj > max_dkj[1] else max_dkj
                        break
                    else:
                        k += 1
                except:
                    k += 1

print(max_dkj)
                    
