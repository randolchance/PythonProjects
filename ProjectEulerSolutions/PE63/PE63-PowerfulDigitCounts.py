# PROJECT EULER PROBLEM 63 - Powerful Digit Counts

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

