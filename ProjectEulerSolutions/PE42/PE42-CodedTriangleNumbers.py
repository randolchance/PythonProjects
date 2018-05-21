# PROJECT EULER PROBLEM 42 - Coded Triangle Numbers
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
print("{} words out of a total {} words".format(len(triangle_words),len(words)))

