"""
PROJECT EULER PROBLEM 55 - Lychrel Numbers
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers,
like 196, never produce a palindrome. A number that never forms a
palindrome through the reverse and add process is called a Lychrel
number. Due to the theoretical nature of these numbers, and for the
purpose of this problem, we shall assume that a number is Lychrel
until proven otherwise. In addition you are given that for every number
below ten-thousand, it will either (i) become a palindrome in less than
fifty iterations, or, (ii) no one, with all the computing power that
exists, has managed so far to map it to a palindrome. In fact, 10677 is
the first number to be shown to require over fifty iterations before
producing a palindrome: 4668731596684224866951378664
(53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves
Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
"""

def reverseAdd(x):
    if x < 10:
        return(x)
    else:
        str_x = str(x)
        str_x = str_x[::-1]
        return(x+int(str_x))

def isPalendrome(s):
    xf = len(s)-1
    palendrome = True
    for x in range(int(xf/2)+1):
        palendrome = palendrome and (s[x] == s[xf-x])
        if palendrome == False:
            break
    return palendrome

number_i = 196
number_max = 10000
lychrel = 0
reverse_adds = 50
for number_i in range(number_max):
    number = number_i
    count = 0
    while not isPalendrome(str(number)) and count < reverse_adds:
        number = reverseAdd(number)
        count += 1
    if count != reverse_adds:
        #print(f"It took {count} iterations to turn {number_i} into the palendrome {number}.")
        pass
    else:
        print(f"{number_i} is a Lychrel number!")
        lychrel += 1
print(f"There are {lychrel} Lychrel numbers under {number_max}!")
