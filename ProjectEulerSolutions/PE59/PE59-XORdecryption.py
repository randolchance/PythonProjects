# PROJECT EULER PROBLEM 59 - XOR Decryption

from collections import Counter
import re

with open("p059_cipher.txt") as code_file:
    code = code_file.read()
print(code)

with open("p042_words.txt") as word_file:
    words = word_file.read()
words = re.sub('"', '', words)
word_list = [word.lower() for word in words.split(",")]
three_letter_words = [word for word in word_list if len(word) == 3]

code_list = [int(x) for x in code.split(",")]

out = ''
for word in three_letter_words:
    l_word = []
    for s in word:
        l_word.append(ord(s))
    i = 0
    new_code_list = []
    for val in code_list:
        new_code_list.append(str(chr(val^l_word[i])))
        i = (i+1)%3
    out = "".join(new_code_list)
    out_list = out.split(" ")
    hits = 0
    for item in out_list:
        if item in word_list:
            hits += 1
    if hits > 20:
        break

print(out)
total = 0
for s in out:
    total += ord(s)
print(total)

