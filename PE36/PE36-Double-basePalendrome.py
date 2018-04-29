"""
PROJECT EULER PROBLEM 36 - Double-base Palendromes
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base,
may not include leading zeros.)
"""

def isPalendrome(s):
    xf = len(s)-1
    palendrome = True
    for x in range(int(xf/2)+1):
        palendrome = palendrome and (s[x] == s[xf-x])
        if palendrome == False:
            break
    return palendrome
 

palendrome_list = []
pal_val = 0
for x in range(1000001):
    b = str(bin(x))[2:]
    a = str(x)
    if isPalendrome(a) and isPalendrome(b):
        palendrome_list.append([a,b])
        pal_val += int(a)

print(palendrome_list)
print(pal_val)
