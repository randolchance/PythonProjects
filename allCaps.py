lines = []

while True:
    line = input()
    if not line: break
    lines.append(line.upper())

print("\n".join(lines))
