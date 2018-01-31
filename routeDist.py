from math import sqrt

pos = [0,0]
while True:
    move = input()
    if not move:
        break
    if "UP" in move:
        pos[1] += int(move[len("UP")+1:])
    elif "DOWN" in move:
        pos[1] -= int(move[len("DOWN")+1:])
    elif "LEFT" in move:
        pos[0] -= int(move[len("LEFT")+1:])
    elif "RIGHT" in move:
        pos[0] += int(move[len("RIGHT")+1:])

print(int(sqrt(pow(pos[0],2)+pow(pos[1],2))))

"""OR"""

pos = [0,0]
while True:
    move = input().split(" ")
    if not move:
        break
    if move[0] == "UP":
        pos[1] += int(move[1])
    if move[0] == "DOWN":
        pos[1] -= int(move[1])
    if move[0] == "LEFT":
        pos[0] -= int(move[1])
    if move[0] == "RIGHT":
        pos[0] += int(move[1])

print(int(sqrt(pos[0]**2+pos[1]**2)))
