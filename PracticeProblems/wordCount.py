words = input().split(" ")
word_set = sorted(set(words))
d = {}
for word in word_set:
    d[word] = words.count(word)
    print(f"{word}:{d[word]}")

""" OR, SINCE DICTS WOULD ELIMINATE REDUNDANT KEYS """

d = {}
for word in input().split(" "):
    d[word] = d.get(word,0)+1
    
words = sorted(d.keys())

for word in words:
    print(f"{word}:{d[word]}")
