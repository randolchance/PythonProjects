# PROJECT EULER PROBLEM 99 - Largest Exponential

from bigfloat import *

base_exp_list = []
with open('p099_base_exp.txt') as file:
    for line in file:
        line = line.rstrip("\n")
        line = line.split(",")
        base_exp_list.append(line)

biggest = [0,0]
with precision(4096):
    for i,base_exp in enumerate(base_exp_list):
        y = int(base_exp[1])
        x = int(base_exp[0])
        z = y*log10(x)
        #print(i,x,y,z)
        if z > biggest[1]:
            biggest = [i+1,z]

print(biggest)

