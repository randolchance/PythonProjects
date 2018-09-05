# PROJECT EULER PROBLEM 48 - Self Powers

mod_val = 10**10
print(mod_val)

total = 0
for i in range(1,1001):
    total += pow(i,i,mod_val)

print(total%mod_val)

