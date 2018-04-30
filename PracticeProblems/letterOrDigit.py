import string

digits = 0
letters = 0

text = input()
for s in text:
    if s in string.ascii_letters:
        letters += 1
    elif s in string.digits:
        digits += 1

print("DIGITS: " + str(digits))
print("LETTERS: " + str(letters))


"OR USING A DICT"

d = {"DIGITS":0,"LETTERS":0}
for s in text:
    if s.isdigit():
        d["DIGITS"] += 1
    elif s.isalpha():
        d["LETTERS"] += 1

print("LETTERS:", d["LETTERS"])
print("DIGITS:", d["DIGITS"])
