"""
PROJECT EULER PROBLEM 63 - Powerful Digit Counts
The 5-digit number, 16807=7**5, is also a fifth power.
Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

def powerfulDigitCount():
    i = 0
    j_0 = 1
    count = 0
    while True:
        i += 1
        for j in range(j_0,10):
            val = j**i
            if len(str(val)) == i:
                print("{}**{} = {}".format(j,i,val))
                count += 1
            else:
                if j_0 == 9:
                    return(count)
                else:
                    j_0 = j
        
            
print(powerfulDigitCount())

# 49 CORRECT
