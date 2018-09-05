# PROJECT EULER PROBLEM 14 - Longest Collatz Sequence


from memoise import Memoise

@Memoise
def collatz(x):
    return(3*x+1 if x%2 else x//2)


longest_chain = []
for x in range (1,1000000):
    chain = [x]
    while x != 1:
        x = collatz(x)
        chain.append(x)

    if len(chain) > len(longest_chain):
        longest_chain = chain[:]

print("{} produces the longest chain with a length of {}.".format(longest_chain[0],len(longest_chain)))

