# PROJECT EULER PROBLEM 9 - Special Pythagorean Triplet


from math import sqrt

abc_sum = 1000
for b in range(1,1000):
    for a in range(1,b):
        c = sqrt(a**2 + b**2)
        if c%1 == 0:
            c = int(c)
            if a+b+c == abc_sum:
                print(a,b,c,a**2,b**2,c**2,a*b*c)
                break

