"""
PROJECT EULER PROBLEM 59 - XOR Decryption
Each character on a computer is assigned a unique code and the
preferred standard is ASCII (American Standard Code for
Information Interchange). For example, uppercase A = 65,
asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert
the bytes to ASCII, then XOR each byte with a given value,
taken from a secret key. The advantage with the XOR function
is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then
107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the
plain text message, and the key is made up of random bytes.
The user would keep the encrypted message and the encryption
key in different locations, and without both "halves", it is
impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so
the modified method is to use a password as a key. If the
password is shorter than the message, which is likely, the
key is repeated cyclically throughout the message. The balance
for this method is using a sufficiently long password key for
security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists
of three lower case characters. Using cipher.txt (right click
and 'Save Link/Target As...'), a file containing the encrypted
ASCII codes, and the knowledge that the plain text must contain
common English words, decrypt the message and find the sum of
the ASCII values in the original text.
"""

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
        print(out)
        break
