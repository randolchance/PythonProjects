# PROJECT EULER PROBLEM 79 - Passcode Derivation

number_list = []
with open('p079_keylog.txt') as file:
    for line in file:
        line = line.rstrip("\n")
        number_list.append(line)

# Determine the numbers and length of the code
num_set = set()
for num in number_list:
    num_set |= set(list(num))
num_set = list(num_set)


# Find the numbers of the code from left to right
#   NOTE: Not explicitly mentioned, but there are no repeating digits
answer = ''
j_max = len(num_set)-1
for j in range(j_max+1):
    number = None
    for n in num_set:
        n_pos = True
        for num in number_list:
            i = num.find(n)
            if j == 0:
                n_pos = (i == 0 or i == -1)
            else:
                n_pos = (i == 0 or i == -1) or any([num[i-1] == a for a in answer])
            if not n_pos: break
        if n_pos:
            number = n
            break
    answer += n
    num_set.remove(number)
        
print(answer)

