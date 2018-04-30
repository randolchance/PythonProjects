def divisor(x):
    for i in range(1,x+1):
        if not x%i:
            yield(i)

max_divisors = 50
i = 0
I = 0
while True:
    i += 1
    I += i
    divisor_list = list(divisor(I))
    print(divisor_list)
    if len(divisor_list) > max_divisors:
        print(i)
        print(divisor_list)
        break
