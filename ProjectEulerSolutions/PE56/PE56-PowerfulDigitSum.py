# PROJECT EULER PROBLEM 56 - Powerful Digit Sum

def sumDigits(x):
    return(sum([int(s) for s in str(x)]))

highest_digit_sum = [100,100,1]
for a in range(99,1,-1):
    for b in range(100,1,-1):
        digit_sum = [a,b,sumDigits(a**b)]
        highest_digit_sum = digit_sum if digit_sum[2] > highest_digit_sum[2] else highest_digit_sum


print(highest_digit_sum)

