# PROJECT EULER PROBLEM 68 - Magic 5-gon Ring


NUM_POOL = [i for i in range(1,11)]
GONS = 5
GON_STR_LEN = 16

def permute(aList,r):
    if r > len(aList):
        raise ValueError("r cannot be bigger than list size")
    elif r == 0 or not aList:
        yield([])
    else:
        for i in aList:
            new_aList = [x for x in aList if x != i]
            for a in permute(new_aList,r-1):
                yield([i]+a)

gon_int_list = []
# First loop forces lowest number to be the first chosen and letting
# combo be the other combinations of other outer numbers
for f in range(len(NUM_POOL)-(GONS-1)):
    for combo in permute(NUM_POOL[f+1:],GONS-1):
        combo = [NUM_POOL[f]]+combo
        #print(combo)
        inner_num_pool = [n for n in NUM_POOL if n not in combo]
        for p in permute(inner_num_pool,len(inner_num_pool)):
            gon_list = [[combo[i],p[i],p[(i+1)%GONS]] for i in range(GONS)]
            gon_sum_list = [sum(gon_list[i]) for i in range(GONS)]
            if not all([gon_sum_list[0] == s for s in gon_sum_list[1:]]): continue
            print(gon_sum_list)
            print(combo,p)
            print(gon_list)
            gon_str = ''
            for gon in gon_list:
                gon_str += "".join([str(n) for n in gon])
            if len(gon_str) == GON_STR_LEN:
                gon_int_list.append(int(gon_str))

print(max(gon_int_list))

