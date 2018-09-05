# PROJECT EULER PROBLEM 329 - Prime Frog


import sys
import os
sys.path.insert(0,os.path.expanduser("~/PythonProjects/venvBigFloat/lib/python3.5/site-packages"))

from gmpy import is_prime
from fractions import Fraction

tile_array = ['P' if is_prime(p+1) else 'N' for p in range(500)]

CROAK_SEQ = 'PPPPNNPPPNPPNPN'

# Take step to position t in tile_array a remainder seq of the CROAK_SEQ
def takeStep(P,t,seq,tile_array):
    if seq == '':
        yield(P)
    else:        
        s = seq[0]
        seq = seq[1:]

        P *= Fraction(2 if tile_array[t] == s else 1,3)

        steps = []
        dt_left = t-1
        if dt_left >= 0: steps.append(dt_left)
        dt_right = t+1
        if dt_right < len(tile_array): steps.append(dt_right)
        P /= len(steps)
        
        for dt in steps:
            for Psteps in takeStep(P,dt,seq,tile_array):
                yield(Psteps)
            

    
P_total = 0
for t in range(len(tile_array)):
    print(t)
    for P in takeStep(Fraction(1,500),t,CROAK_SEQ,tile_array):
        P_total += P

print(P_total)

