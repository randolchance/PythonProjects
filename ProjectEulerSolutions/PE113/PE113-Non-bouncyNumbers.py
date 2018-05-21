# PROJECT EULER PROBLEM 113 - Non-bouncy Numbers

def countNonBouncies(digit_count):
    digit_count -= 1
    digit_count_dict = {}
    if digit_count == 0:
        for i in range(0,9):
            digit_count_dict[i] = [1,0]
        digit_count_dict[9] = [0,0]
    else:
        sub_digit_count_dict = countNonBouncies(digit_count)
        for i in range(9,-1,-1):
            count = 0
            for j in range(9,i-1,-1):
                count += sub_digit_count_dict[9-j][1]+1
            digit_count_dict[i] = [count,0]
        for i in range(0,10):
            digit_count_dict[9-i][1] = digit_count_dict[i][0]-1
        count = 0
        for k in digit_count_dict.keys():
            for i in range(0,2):
                count += sub_digit_count_dict[k][i]
        digit_count_dict[0][0] = count
                
    return(digit_count_dict)


total_digits = 99  # up to 99999... total_digits
count_dict = countNonBouncies(total_digits)

key_list = sorted(count_dict.keys())
count = 0
for key in key_list:
    print(count_dict[key])
    for i in range(0,2):
        count += count_dict[key][i]
print(count)

"""
46545610993618
"""
