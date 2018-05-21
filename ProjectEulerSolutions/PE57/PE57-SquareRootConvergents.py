# PROJECT EULER PROBLEM 57 - Square Root Convergents

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
