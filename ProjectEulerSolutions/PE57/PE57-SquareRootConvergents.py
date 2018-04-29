"""
PROJECT EULER PROBLEM 57 - Square Root Convergents
It is possible to show that the square root of two can be expressed
as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the
eighth expansion, 1393/985, is the first example where the number
of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a
numerator with more digits than denominator?
"""

expansions = 1000

top_i = 1
bot_i = 1
top_f = 3
bot_f = 2
count = 0
for i in range(expansions):
    count += (len(str(top_f)) > len(str(bot_f)))
    #print(top_f,bot_f,count)
    top_next = 2*top_f + top_i
    bot_next = 2*bot_f + bot_i
    top_i = top_f
    bot_i = bot_f
    top_f = top_next
    bot_f = bot_next
print(count)
""" THIS TAKES 11 ETERNITIES
f = frac(1,1)
F = 1+frac(1,2)
for i in range(expansions):
    newF = frac(2*F.num()+f.num(),2*F.den()+f.den())
    f = frac(F.num(),F.den())
    F = frac(newF.num(),newF.den())
    print(F)
"""
