"""
PROJECT EULER PROBLEM 32 - Pandigital Products
We shall say that an n-digit number is pandigital if
it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254,
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so
be sure to only include it once in your sum.
"""

original_digit_pool = (1,2,3,4,5,6,7,8,9)
digit_groups = ((1,4,4),(2,3,4))

pandigital_product_list = []
product_sum = 0
for i in original_digit_pool:
    dl = []
    dpl = [x for x in original_digit_pool if x!=i]
    dl.append(i)
    for j in dpl:
        dl2 = [x for x in dl]
        dpl2 = [x for x in dpl if x!=j]
        dl2.append(j)
        for k in dpl2:
            dl3 = [x for x in dl2]
            dpl3 = [x for x in dpl2 if x!=k]
            dl3.append(k)
            for l in dpl3:
                dl4 = [x for x in dl3]
                dpl4 = [x for x in dpl3 if x!=l]
                dl4.append(l)
                for m in dpl4:
                    dl5 = [x for x in dl4]
                    dpl5 = [x for x in dpl4 if x!=m]
                    dl5.append(m)
                    for dg in digit_groups:
                        ml = [x for x in dl5]
                        pl = [x for x in dpl5]
                        multiplicand = 0
                        multiplier = 0
                        product = 0
                        for g in range(dg[0]):
                            multiplicand = ml.pop(0)+multiplicand*10
                        for g in range(dg[1]):
                            multiplier = ml.pop(0)+multiplier*10
                        product = multiplicand*multiplier
                        if product >= 10000:
                            continue
                        rl = [int(x) for x in str(product)]
                        rl.sort()
                        if rl == pl:
                            pandigital_product_list.append([multiplicand,multiplier,product])
                            product_sum += product

print(pandigital_product_list)
print(product_sum)
