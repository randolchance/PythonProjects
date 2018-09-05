# PROJECT EULER PROBLEM 4 - Largest Palindrome Product

def isPalindrome(X):
    s = str(X)
    xf = len(s)-1
    return(all([s[x] == s[xf-x] for x in range(int(xf/2)+1)]))

biggest = 0
for j in range(999,99,-1):
    for i in range(999,99,-1):
        product = i*j
        if isPalindrome(product) and product > biggest:
            biggest = product

print(biggest)

