# PROJECT EULER PROBLEM 38 - Pandigital Multiples


n_list = ['9']
val_list = []
loop = True
while loop:
    print(n_list)
    n_list_copy = n_list[:]
    n_list = []
    for str_n in n_list_copy:
        new_n_list = []
        for d in '987654321':
            if d not in str_n:
                new_str_n = str_n+d
                #print(new_str_n)
                if len(new_str_n) < 4:
                    new_n_list.append(new_str_n)
                str_num = ''
                good_num = True
                for i in range(1,10):
                    str_num += str(i*int(new_str_n))
                    if len(str_num) > 9:
                        good_num = False
                        break
                    elif len(str_num) == 9:
                        break
                if good_num:
                    if sorted([s for s in str_num]) == [str(x) for x in range(1,10)]:
                        val_list.append(int(str_num))
        n_list += new_n_list
    if not n_list:
        break

print(max(val_list))

