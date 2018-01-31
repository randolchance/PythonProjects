from math import sqrt

def Q(x):
    C = 50
    H = 30
    return(sqrt(2 * C * x / H))

valuesStr = input().split(",")
values = []
for x in valuesStr:
    values.append(str(round(Q(int(x)))))

print(",".join(values))
