number_list = []

for x in range(2000,3001):
    if (x%7 == 0) and (x%5 != 0):
        number_list.append(x)
        
print(number_list)
