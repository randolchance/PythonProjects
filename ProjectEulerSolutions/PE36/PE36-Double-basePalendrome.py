# PROJECT EULER PROBLEM 36 - Double-base Palendromes

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

