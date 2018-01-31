li = [1,2,3,4,5,6,7,8,9,10]
li2 = map(lambda x: x**2, filter(lambda x: not x%2, li))
print(list(li2))
