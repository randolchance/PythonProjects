# PROJECT EULER PROBLEM 206 - Concealed Square

from math import sqrt

CONCEALED_SQUARE = "1_2_3_4_5_6_7_8_9_0"

def getDigit(x,digit):
    str_x = str(x)
    if digit >= len(str_x):
        return(0)
    return(str_x[-(digit+1)])

MAX_DIGITS = 10


def nextDigit(digit):
    if digit == 0:
        for new_digit_num in range(10):
            square = new_digit_num**2
            new_digit = getDigit(square,0)
            if new_digit == CONCEALED_SQUARE[-1]:
                yield(str(new_digit_num))
    else:
        for str_num in nextDigit(digit-1):
            for new_digit_num in range(10):
                new_str_num = str(new_digit_num)+str_num
                num = int(new_str_num)
                square = num**2
            
                CS_digit = CONCEALED_SQUARE[-(digit+1)]

                if CS_digit == "_":
                    yield(new_str_num)
                elif CS_digit == str(getDigit(square,digit)):
                    yield(new_str_num)


result = None
for num in nextDigit(MAX_DIGITS-1):
    str_square = str(int(num)**2)
    if len(str_square) == len(CONCEALED_SQUARE):
        good_num = True
        for i,s in enumerate(CONCEALED_SQUARE):
            if s != "_":
                if str_square[i] != s:
                    good_num = False
                    break
        if good_num:
            result = int(str_square)
            break

print(result,sqrt(result))
        
        
