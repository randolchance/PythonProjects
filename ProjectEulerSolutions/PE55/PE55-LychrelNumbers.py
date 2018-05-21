# PROJECT EULER PROBLEM 55 - Lychrel Numbers

def reverseAdd(x):
    str_x = str(x)
    str_x = str_x[::-1]
    return(x+int(str_x))

def isPalindrome(X):
    s = str(X)
    xf = len(s)-1
    return(all([s[x] == s[xf-x] for x in range(int(xf/2)+1)]))


number_max = 10000
lychrel = 0
reverse_adds = 50
for number_i in range(1,number_max):
    number = number_i
    count = 1
    palindrome = False
    while not palindrome and count < reverse_adds:
        #print(number_i,number)
        number = reverseAdd(number)
        palindrome = isPalindrome(number)
        count += 1
    #print(number_i,number)
    if count < reverse_adds:
        #print(f"It took {count} iterations to turn {number_i} into the palindrome {number}.")
        pass
    else:
        print("{} is a Lychrel number!".format(number_i))
        lychrel += 1
print("There are {} Lychrel numbers under {}!".format(lychrel,number_max))

