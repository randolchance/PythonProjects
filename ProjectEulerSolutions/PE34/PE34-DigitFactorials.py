# PROJECT EULER PROBLEM 34 - Digit Factorials

def factorial(n):
    if n==0 or n==1:
        return(1)
    return(n*factorial(n-1))

print(7*factorial(9))
print(9999999)

results = []
for i in range(3,2999999):
    if i == sum([factorial(int(s)) for s in str(i)]):
        print(i)
        results.append(i)

total = 0
for r in results:
    total += r

print(total)

