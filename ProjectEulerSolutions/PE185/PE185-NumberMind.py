# PROJECT EULER PROBLEM 185 - Number Mind

from collections import Counter

# Parse guess list
def readGuesses():
    guess_list = []
    with open("p185_realGuesses.txt") as file:
        for line in file:
            guess = line.rstrip(" correct\n")
            guess = guess.split(" ;")
            guess[1] = int(guess[1])
            guess_list.append(guess)
    return(guess_list)

# Generates string bit masks of x digits with n 0s
#  (it's a modified version of older code that was using the 0s rather than
#  the 1s; notice ln 101 of checkGuess uses the 0. I could make it use 1s
#  instead, but... meh)
def bitList(x,n):
    if x == 0:
        return([])
    out_str = ''
    if n == 0:
        for i in range(x):
            out_str += '1'
        return([out_str])
    out_list = []
    new_x = x-1
    new_n = n-1
    for i in range(x-(n-1)):
        i_str = out_str + '0'
        sub_bit_list = bitList(new_x,new_n)
        if not sub_bit_list:
            out_list.append(i_str)
            break
        for bit_str in sub_bit_list:
            new_str = i_str + bit_str
            out_list.append(new_str)
        out_str += '1'
        new_x -= 1
    return(out_list)
            

GUESS = 0
RIGHT = 1

guess_list = readGuesses()
NUM_OF_GUESSES = len(guess_list)
DIGITS = len(guess_list[0][GUESS])

# Recursively goes through the guesses and assumes each possible
# combination of numbers is correct. If it finds a logical contradiction
# it'll skip to the next assumption and continue
#  guess_num => The index of the current guess
#  guess_list => The guess list made from the .txt file of guesses
#  right_digits => The assumed correct digits, with 'x' as wildcards
#  right_so_far => How many digits are assumed correct so far
#                  (rather than counting non-wildcards from right_digits)
def checkGuess(guess_num,guess_list,right_digits,right_so_far):
    
    # This is an end condition of the recursive checkGuess function.
    # If it has gone through all the given guesses it will see if
    # there are any wildcards ('x') left in the 'right_digits' string.
    # If there is, it'll check through the guesses again to see
    # if that digit has only one possibility left. If so then
    # the wildcard is replaced by the only possible digit remaining
    if guess_num == NUM_OF_GUESSES:
        if 'x' in right_digits:
            for d in range(DIGITS):
                if right_digits[d] == 'x':
                    digit_list = [str(n) for n in range(10)]
                    for n in digit_list[:]:
                        for i in range(NUM_OF_GUESSES):
                            if guess_list[i][GUESS][d] == n:
                                digit_list.remove(n)
                                break
                    if len(digit_list) == 1:
                        right_digits = right_digits[:d] + digit_list[0] + right_digits[d+1:]
                    else:
                        return(False)
        return(right_digits)
                            
    check_guess = guess_list[guess_num][GUESS]
    check_right = guess_list[guess_num][RIGHT]
    #print(check_guess)
    
    # See if an assumed right digit matches a number in the next guess
    # and reduce the number of right digits in the next guess
    x_count = 0
    for d in range(DIGITS):
        if right_digits[d] != 'x':
            if right_digits[d] == check_guess[d]:
                if check_right == 0:
                    return(False)
                else:
                    check_right -= 1
        else:
            x_count += 1
    if x_count == 0:
        if check_right > 0:
            return(False)
        else:
            if guess_num+1 == NUM_OF_GUESSES:
                return(right_digits)

    # Build the next set of assumed right digits and try them
    if check_right > 0:
        check_right_so_far = right_so_far + check_right
        for bits in bitList(DIGITS-right_so_far,check_right):
            check_right_digits = ''
            next_guess = False
            for d in range(DIGITS):
                if right_digits[d] == 'x':
                    b = bits[0:1]
                    bits = bits[1:]
                    if b == '0':
                        new_digit = check_guess[d]
                        for i in range(guess_num):
                            if guess_list[i][GUESS][d] == new_digit:
                                next_guess = True
                                break
                        if next_guess:
                            break
                        check_right_digits += new_digit
                    else:
                        check_right_digits += 'x'
                else:
                    check_right_digits += right_digits[d]
            if next_guess:
                continue
            #print(check_right_digits)
            good_guess = checkGuess(guess_num+1,guess_list,check_right_digits,check_right_so_far)
            if good_guess:
                return(good_guess)
        return(False)
    else:
        return(checkGuess(guess_num+1,guess_list,right_digits,right_so_far))

print(guess_list)
right_digits = ''
for i in range(DIGITS):
    right_digits += 'x'
print(checkGuess(0,guess_list,right_digits,0))

