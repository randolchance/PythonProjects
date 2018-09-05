# PROJECT EULER PROBLEM 2 - Even Fibonacci Numbers

from memoise import Memoise

@Memoise
def fib(n):
    if n == 0 or n == 1:
        return(1)
    else:
        return(fib(n-2)+fib(n-1))


max_val = 4000000
total = 0
x = 1
while True:
    val = fib(x)
    if val > max_val:
        break
    if val%2 == 0:
        total += val
    x += 1

print(total)
