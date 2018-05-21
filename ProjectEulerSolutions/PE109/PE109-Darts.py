# PROJECT EULER PROBLEM 109 - Darts

point_array = []
for i in range(1,21):
    point_array.append(i)
point_array.append(25)

start_score = 1
end_score = 99

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
