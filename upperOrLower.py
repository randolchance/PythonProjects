text = input()

d = {"UPPERCASE":0,"LOWERCASE":0}
for s in text:
    if s.isupper():
        d["UPPERCASE"] += 1
    elif s.islower():
        d["LOWERCASE"] += 1

print(d["UPPERCASE"])
print(d["LOWERCASE"])
