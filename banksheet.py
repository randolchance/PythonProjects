total = 0
while True:
    s = input()
    if not s:
        break
    total += ((s[0]=="D") - (s[0]=="W"))*int(s[2:])

print(total)
