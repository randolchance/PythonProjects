"""
PROJECT EULER PROBLEM 305 - Reflexive Position
Let's call S the (infinite) string that is made by concatenating
the consecutive positive integers (starting from 1) written down
in base 10.

Thus, S = 1234567891011121314151617181920212223242...

It's easy to see that any number will show up an infinite number
of times in S.

Let's call f(n) the starting position of the nth occurrence of n
in S.

For example, f(1)=1, f(5)=81, f(12)=271 and f(7780)=111111365.

Find ∑f(3^k) for 1≤k≤13.
"""

from operator import itemgetter

# Count the total digits of a string made up of the numbers 1 through x (excl)
def countDigits(x):
    if type(x) is str:
        x = int(x)
    x -= 1
    digits = len(str(x))
    count = 0
    for d in range(digits-1,-1,-1):
        count += (x - 10**d + 1) * digits if d == digits-1 else 9 * 10**d * (d+1)
    return(count)

def checkConsecutive(aList):
    if not all(aList):
        return(False)
    for i in range(len(aList)-1):
        if int(aList[i])+1 != int(aList[i+1]):
            return(False)
    return(True)

def sliceNumber(str_x,d=0,bigger_only=False,step_digit=True):
    if d == 0:
        yield(['',str_x])
    elif d == len(str_x):
        yield([str_x,''])
    else:
        str_x1 = str_x[:d]
        len_str_x1 = len(str_x1)
        str_x2 = str_x[d:]
        len_str_x2 = len(str_x2)
        if not (bigger_only and len_str_x2 < d):
            # This filters out lists of numbers that will have an entry that starts
            # with 0 since they make no sense in this context
            if str_x2[0] != '0':
                if len_str_x2 > d:
                    for slice_x2 in sliceNumber(str_x2,d,True,step_digit):
                        yield([str_x1]+slice_x2)
                    if step_digit:
                        for slice_x2 in sliceNumber(str_x2,d+1,True,False):
                            yield([str_x1]+slice_x2)
                if not bigger_only:
                    yield([str_x1,str_x2])
                elif (bigger_only and (len_str_x2 == d or (step_digit and len_str_x2 == d+1))):
                    yield([str_x1,str_x2])

def generateNumbers(n,occurrence):
    count = 0
    str_n = str(n)
    digits = len(str_n)
    final_list = []
    result_list = []
    for d in range(1,digits):
        for s in sliceNumber(str_n,d):
            #print(s)
            
            if checkConsecutive(s):
                #yield(s)
                count += 1
                if count == occurrence:
                    return(countDigits(s[0]))
            
            else:
                    if len(s[1]) - len(s[0]) == 1:
                        for j in range(1,10):
                            new_s = [str(j)+s[0]]
                            new_s += s[1:]
                            #print(new_s)
                            if checkConsecutive(new_s):
                                count += 1
                                if count == occurrence:
                                    return(countDigits(new_s[0]))
            if len(s) == 2:
                result_list.append(s)

    new_result_list = []
    for result in result_list:
        #print(result)
        new_result = [result[1]+result[0],result[1],result[0]]
        new_result_list.append(new_result)
    new_result_list = sorted(new_result_list,key=itemgetter(0))
    #print(new_result_list)

    first_list = list(set([str_n]+[item[0] for item in new_result_list]))
    #print(first_list)
    len_first_list = len(first_list)
    if count + len_first_list >= occurrence:
        # (n - count) has to be >= 1
        list_index = n - count - 1
        return(countDigits(first_list[list_index]))
    count += len_first_list
    
    number_list = [item[1:] for item in new_result_list]
    #print(number_list)
    
    new_number_list = []
    i_digits = 1
    while True:
        i = 0
        while i < 10**i_digits:
            str_i = str(i)
            for j in range(i_digits-len(str_i)):
                str_i = '0' + str_i
            new_new_number_list = [x[0]+str_i+x[1] for x in number_list]
            if str_i[0] != '0':
                for j in range(i_digits+1):
                    new_new_number_list.append(str_i[:j]+str_n+str_i[j:])
            else:
                new_new_number_list.append(str_n+str_i)
            new_number_list += new_new_number_list
            i += 1
            
        new_number_list = sorted(list(set(new_number_list)))
        for item in new_number_list:
            index = 0
            while True:
                index = item.find(str_n,index)
                if index == -1:
                    break
                count += 1
                if count == occurrence:
                    print("A:",item)
                    return(countDigits(item)+index+1)
                index += 1
            mod_item = item+str(int(item)+1)
            start_j = len(item)-(digits-1)
            end_j = len(item)
            for j in range(start_j,end_j):
                index = j
                if mod_item.startswith(str_n,index):
                    count += 1
                    if count == occurrence:
                        print("B:",item)
                        return(countDigits(item)+index+1)
                    #break
                
        #print(count)
        new_number_list = []
        i_digits += 1


total = 0
for k in range(1,14):
    n = 3**k
    print(k,n)
    index = generateNumbers(n,n)
    total += index
    print("INDEX:",index)
    
print("TOTAL: ", total)

# 18174995535140 CORRECT


