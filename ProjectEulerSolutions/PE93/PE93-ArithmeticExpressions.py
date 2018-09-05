# PROJECT EULER PROBLEM 93 - Arithmetic Expressions


def generateNumberSet(aList,aSize):
    if aSize == 0:
        yield([])
    else:
        for i in aList:
            new_aList = [j for j in aList if j != i]
            for nList in generateNumberSet(new_aList,aSize-1):
                yield([i]+nList)
        
def generateOperationSet(ops,aSize):
    if aSize == 0:
        yield([])
    else:
        for i in range(len(ops)):
            o = ops[i]
            for oList in generateOperationSet(ops,aSize-1):
                yield([o]+oList)

def generateOrder(order_set):
    if not order_set:
        yield([])
    else:
        for o in order_set:
            new_order_set = [i for i in order_set if i != o]
            for oStr in generateOrder(new_order_set):
                yield([o]+oStr)

def compute(nList,ops,order):
    o = order.pop(0)
    order = [(i if i < o else i-1) for i in order]
    op = ops.pop(o)
    numA = nList.pop(o)
    numB = nList.pop(o)
    if op == '-':
        results = [numA-numB,numB-numA]
    elif op == '/':
        results = []
        try:
            results.append(numA/numB)
        except:
            pass
        try:
            results.append(numB/numA)
        except:
            pass
    elif op == '+':
        results = [numA+numB]
    elif op == '*':
        results = [numA*numB]
    else:
        raise ValueError("I don't know how this could have happened.")
    for result in results:
        new_nList = nList[:]
        new_nList.insert(o,result)
        if len(new_nList) == 1:
            yield(new_nList[0])
        else:
            for out in compute(new_nList,ops[:],order[:]):
                yield(out)


NUM_SET_SIZE = 4
OP_SET_SIZE = NUM_SET_SIZE-1
OPERATIONS = [o for o in "+-*/"]
OP_SET_RANGE = [0,OP_SET_SIZE]

A = ord('A')
ORDER_SET = [s for s in range(OP_SET_SIZE)]

num_dict = {}
for nList in generateNumberSet([i for i in range(1,10)],NUM_SET_SIZE):
    con_set = set()
    for o in generateOperationSet(OPERATIONS,OP_SET_SIZE):
        for a in generateOrder(ORDER_SET):
            #print(nList,o,a)
            for result in compute(nList[:],o[:],a[:]):
                if result >= 1 and result%1 == 0:
                    #print("\t",result)
                    con_set |= {int(result)}
    num = "".join([str(i) for i in sorted(nList)])
    if num in num_dict:
        num_dict[num] |= con_set
    else:
        num_dict[num] = con_set

best = ['',0]
for num in num_dict.keys():
    con_set = sorted(list(num_dict[num]))
    i = 0
    while con_set[i] == i+1:
        i += 1
    if i+1 > best[1]:
        best[0] = num
        best[1] = i+1
        #print(best)

print(best)

