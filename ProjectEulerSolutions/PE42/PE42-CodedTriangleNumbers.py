"""
PROJECT EULER PROBLEM 42 - Coded Triangle Numbers
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to
its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
If the word value is a triangle number then we shall call the word a
triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
"""
import re
from math import sqrt

A = 1/2
B = 1/2
alphabet = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def quadSolver(a,b,c):
    in_sqrt = b**2 - 4*a*c
    if in_sqrt < 0:
        return(["Non-real roots!"])
    return([(-b-sqrt(in_sqrt))/2/a,(-b+sqrt(in_sqrt))/2/a])

with open("p042_words.txt") as word_file:
    words = word_file.read()
words = re.sub('"', '', words)
words = words.split(",")

triangle_words = []
for word in words:
    word_sum = 0
    for letter in word:
        word_sum += alphabet.index(letter)
    roots = quadSolver(A,B,-word_sum)
    for root in roots:
        if (root >=0) and (root%1 == 0):
            triangle_words.append([word,int(root),word_sum])

print(triangle_words)
print(f"{len(triangle_words)} words out of a total {len(words)} words")
