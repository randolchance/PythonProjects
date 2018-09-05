# PROJECT EULER PROBLEM 74 - Digital Factorial Chains

from memoise import Memoise

@Memoise
def factorial(x):
    if x == 0 or x == 1:
        return(1)
    return(x*factorial(x-1))

@Memoise
def digitFactorial(x):
    str_x = str(x)
    total = 0
    for s in str_x:
        total += factorial(int(s))
    return(total)


target_len = 60
total = 0
for n in range(2,1000000):
    chain_list = [n]
    new_n = n
    while True:
        new_n = digitFactorial(new_n)
        if new_n not in chain_list:
            chain_list.append(new_n)
        else:
            break
    if len(chain_list) > 59:
        print(n,len(chain_list))
    total += (len(chain_list) == target_len)


print(total)

