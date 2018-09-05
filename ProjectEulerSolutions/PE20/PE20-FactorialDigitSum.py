# PROJECT EULER PROBLEM 20 - Factorial Digit Sum


def factorial(n):
    if n == 0 or n == 1:
        return(1)
    return(n*factorial(n-1))

total = 0

for s in str(factorial(100)):
    total += int(s)

print(total)

