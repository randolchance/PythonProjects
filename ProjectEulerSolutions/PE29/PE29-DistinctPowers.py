# PROJECT EULER PROBLEM 29 - Distinct Powers


l = []
for a in range(2,101):
    for b in range(2,101):
        x = a**b
        if x not in l:
            l.append(x)

print(len(l))

