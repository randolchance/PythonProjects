"""
PROJECT EULER PROBLEM 109 - Darts
In the game of darts a player throws three darts at a target board
which is split into twenty equal sized sections numbered one to twenty.

The score of a dart is determined by the number of the region that
the dart lands in. A dart landing outside the red/green outer ring
scores zero. The black and cream regions inside this ring represent
single scores. However, the red/green outer ring and middle ring
score double and treble scores respectively.

At the centre of the board are two concentric circles called the bull
region, or bulls-eye. The outer bull is worth 25 points and the inner
bull is a double, worth 50 points.

There are many variations of rules but in the most popular game the
players will begin with a score 301 or 501 and the first player to
reduce their running total to zero is a winner. However, it is normal
to play a "doubles out" system, which means that the player must land
a double (including the double bulls-eye at the centre of the board)
on their final dart to win; any other dart that would reduce their
running total to one or lower means the score for that set of three
darts is "bust".

When a player is able to finish on their current score it is called a
"checkout" and the highest checkout is 170: T20 T20 D25 (two treble
20s and double bull).

There are exactly eleven distinct ways to checkout on a score of 6:

D3	
D1	D2	 
S2	D2	 
D2	D1	 
S4	D1	 
S1	S1	D2
S1	T1	D1
S1	S3	D1
D1	D1	D1
D1	S2	D1
S2	S2	D1

Note that D1 D2 is considered different to D2 D1 as they finish on
different doubles. However, the combination S1 T1 D1 is considered
the same as T1 S1 D1.

In addition we shall not include misses in considering combinations;
for example, D3 is the same as 0 D3 and 0 0 D3.

Incredibly there are 42336 distinct ways of checking out in total.

How many distinct ways can a player checkout with a score less than 100?
"""

point_array = []
for i in range(1,21):
    point_array.append(i)
point_array.append(25)

start_score = 1
end_score = 100

out_array = []
for score in range(start_score,end_score+1):
    out_score_array = []
    # Last throw first
    for i in point_array:
        new_score = score - 2*i
        if new_score < 0:
            continue
        score_array = ['D'+str(i)]
        if new_score == 0:
            out_score_array.append([score_array])
            continue
        for j in point_array:
            for m in range(1,4):
                if (j == 25) and (m == 3):
                    continue
                if new_score < m*j:
                    continue
                if m == 1:
                    score_type = 'S'
                elif m == 2:
                    score_type = 'D'
                elif m == 3:
                    score_type = 'T'
                new_score_array = [score_type+str(j)] + score_array
                if new_score == m*j:
                    out_score_array.append(new_score_array)
                    continue
                newest_score = new_score - m*j
                for k in point_array:
                    for n in range(1,4):
                        if (k == 25) and (n == 3):
                            continue
                        if newest_score != n*k:
                            continue
                        if n == 1:
                            score_type = 'S'
                        elif n == 2:
                            score_type = 'D'
                        elif n == 3:
                            score_type = 'T'
                        newest_score_array = [score_type+str(k)] + new_score_array
                        unique_score = True
                        for S in out_score_array:
                            if (S[0] == newest_score_array[1]) and (S[1] == newest_score_array[0]):
                                unique_score = False
                                break
                        if unique_score:
                            out_score_array.append(newest_score_array)
    out_array.append([score,out_score_array])

score_count = 0
for out in out_array:
    print(out[0])
    for combo in out[1]:
        score_count += 1
        #print(combo)

print(score_count)
