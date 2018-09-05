# PROJECT EULER PROBLEM 205 - Dice Game


import sys
import os
sys.path.insert(0,os.path.expanduser("~/PythonProjects/venvBigFloat/lib/python3.5/site-packages"))
from bigfloat import *

from collections import Counter

dice6 = (1,2,3,4,5,6)
dice4 = (1,2,3,4)


def rollDice(die,times):
    face_counts = Counter(die)
    for t in range(1,times):
        new_face_counts = []
        for count in face_counts.keys():
            for d in die:
                new_face_counts += face_counts[count]*[d + count]
        face_counts = Counter(new_face_counts)
    return(face_counts)


peter_rolls = 9
colin_rolls = 6

peter = rollDice(dice4,peter_rolls)
colin = rollDice(dice6,colin_rolls)

peter_total_combos = len(dice4)**peter_rolls
colin_total_combos = len(dice6)**colin_rolls

with precision(100):
    O_peter_wins = O_colin_wins = O_draw = 0
    for p_roll in peter.keys():
        #print("P: ",p_roll,peter[p_roll],peter[p_roll]/peter_total_combos)
        for c_roll in colin.keys():
            if p_roll > c_roll:        
                #print("C: ",c_roll,colin[c_roll],colin[c_roll]/colin_total_combos)
                
                O_peter_wins += peter[p_roll]*colin[c_roll]
            elif p_roll < c_roll:
                O_colin_wins += peter[p_roll]*colin[c_roll]
            else:
                O_draw += peter[p_roll]*colin[c_roll]

    P_peter_wins = div(O_peter_wins,(peter_total_combos*colin_total_combos))
    P_colin_wins = div(O_colin_wins,(peter_total_combos*colin_total_combos))
    P_draw = div(O_draw,(peter_total_combos*colin_total_combos))
    print(P_peter_wins,P_colin_wins,P_draw,sum([P_peter_wins,P_colin_wins,P_draw]))

