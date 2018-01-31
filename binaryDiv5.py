numbers = input().split(",")
values = []
for number in numbers:
    rev_number = "".join(reversed(number))
    y = 0
    for x in range(3,-1,-1):
        y += int(rev_number[x])*pow(2,x)
    if not y%5:
        values.append(number)
print(",".join(values))


"""MUCH BETTER"""

values = []
for number in numbers:
    x = int(number,2) 
    if not x%5:
        values.append(number)
print(",".join(values))
