pw_list = []
for pw in input().split(","):
    if len(pw) < 6 or len(pw) > 12:
        continue
    digit = False
    lowercase = False
    uppercase = False
    punctuation = False
    space = False
    for s in pw:
        space = space or s.isspace()
        digit = digit or s.isdigit()
        lowercase = lowercase or s.islower()
        uppercase = uppercase or s.isupper()
        for p in "$#@":
            punctuation = punctuation or (s == p)
    if digit and lowercase and uppercase and punctuation and not space:
        pw_list.append(pw)

print(",".join(pw_list))

"""USING REGEX"""

import re
pw_list = []
for pw in input().split(","):
    if len(pw) < 6 or len(pw) > 12:
        continue
    if not re.search("[a-z]",pw):
        continue
    if not re.search("[A-Z]",pw):
        continue
    if not re.search("[0-9]",pw):
        continue
    if not re.search("[@#$]",pw):
        continue
    if re.search("\s",pw):
        continue
    pw_list.append(pw)

print(",".join(pw_list))
