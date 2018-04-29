"""
PROJECT EULER PROBLEM 121 - Disc Game Prize Fund
A bag contains one red disc and one blue disc. In a game of chance
a player takes a disc at random and its colour is noted. After each
turn the disc is returned to the bag, an extra red disc is added,
and another disc is taken at random.

The player pays £1 to play and wins if they have taken more blue
discs than red discs at the end of the game.

If the game is played for four turns, the probability of a player
winning is exactly 11/120, and so the maximum prize fund the banker
should allocate for winning in this game would be £10 before they
would expect to incur a loss. Note that any payout will be a whole
number of pounds and also includes the original £1 paid to play the
game, so in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated to a single
game in which fifteen turns are played.
"""

from memoise import Memoise
from fractions import Fraction
from math import gcd

@Memoise
def bitList(x,n):
    if x == 0:
        return([])
    out_str = ''
    if n == 0:
        for i in range(x):
            out_str += '0'
        return([out_str])
    out_list = []
    new_x = x-1
    new_n = n-1
    for i in range(x-(n-1)):
        i_str = out_str + '1'
        sub_bit_list = bitList(new_x,new_n)
        if not sub_bit_list:
            out_list.append(i_str)
            break
        for bit_str in sub_bit_list:
            new_str = i_str + bit_str
            out_list.append(new_str)
        out_str += '0'
        new_x -= 1
    return(out_list)

def bitRange(x,n,n_max=-1):
    if n_max == -1:
        n_max = x
    for N in range(n,n_max+1):
        for bits in bitList(x,N):
            yield(bits)


turns = 15
min_wins = turns//2+1
print(turns,min_wins)
total_frac = Fraction()
total = 0
for bits in bitRange(turns,min_wins):
    i_frac = Fraction(1,1)
    for i,b in enumerate(bits):
        bottom = 2+i
        # Red disk: b = 0 ; blue disk: b = 1
        top = bottom-1 if b == '0' else 1
        i_frac *= Fraction(top,bottom)
    total_frac += i_frac
    
print(total_frac)
Owin = total_frac.numerator
Olose = total_frac.denominator - total_frac.numerator

print("Owin = {} ; Olose = {}".format(Owin,Olose))
Oratio = Olose/Owin
print(Owin/Olose)
print(Oratio)
print(int(Oratio)+1)

# 2269 CORRECT
