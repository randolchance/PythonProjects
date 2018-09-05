# PROJECT EULER PROBLEM 39 - Integer Right Triangles


from math import sqrt

p_min = 7
p_max = 1000
p_dict = {}

for c in range(5,p_max-7):
    b = c-1
    a = sqrt(c**2-b**2)
    while a < b:
        if a%1 == 0:
            a = int(a)
            p = a+b+c
            if p <= p_max and p >= p_min:
                #print(p,[a,b,c])
                if p in p_dict:
                    p_dict[p].append([a,b,c])
                else:
                    p_dict[p] = [[a,b,c]]
        b -= 1
        a = sqrt(c**2-b**2)

max_val = [0,0]
for key,vals in p_dict.items():
    if len(vals) > max_val[1]:
        max_val = [key,len(vals)]
print(max_val)

