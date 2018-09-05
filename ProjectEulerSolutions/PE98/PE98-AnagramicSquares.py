# PROJECT EULER PROBLEM 98 - Anagramic Squares


from math import sqrt
from collections import Counter
    

with open('p098_words.txt') as file:
    words = file.read()
words = words.lstrip('"').rstrip('"')
words = words.split('","')


word_length_dict = {}

max_length = 1
min_length = 10
for word in words:
    l = len(word)
    max_length = l if l > max_length else max_length
    min_length = l if l < min_length else min_length
    if l in word_length_dict:
        word_length_dict[l].append(word)
    else:
        word_length_dict[l] = [word]

pair_list = []
for l in range(max_length,min_length-1,-1):
    letter_lists = [w for w in word_length_dict[l]]
    while letter_lists:
        word = letter_lists.pop()
        word_pair = [word]
        for other_word in letter_lists[:]:
            if Counter(word) == Counter(other_word):
                word_pair.append(other_word)
                letter_lists.remove(other_word)
        if len(word_pair) > 1:
            pair_list.append(word_pair)

#for pair in pair_list:
#    print(pair)


max_pair_length = len(pair_list[0][0])
min_pair_length = len(pair_list[-1][0])
n_0 = int(sqrt(10**max_pair_length))
n_f = int(sqrt(10**(min_pair_length-1)))
square_dict = {}
for n in range(n_0,n_f-1,-1):
    square = n**2
    s_list = [s for s in str(square)]
    if len(s_list) != len(set(s_list)): continue
    #print(square)
    l = len(str(square))
    if l in square_dict:
        square_dict[l].append(square)
    else:
        square_dict[l] = [square]
        
biggest_square = False
for word_pair in pair_list:

    word_length = len(word_pair[0])
    if word_length < len(str(biggest_square)):
        break
    square_list_of_size = square_dict[word_length]
    for square in square_list_of_size:
        for word in word_pair:
            s_list = [s for s in str(square)]
            other_word_pairs = [w for w in word_pair if w != word]
            letter_dict = {}
            for letter in word:
                letter_dict[letter] = s_list.pop(0)
            word_numbers_list = []
            for w in word_pair:
                str_num = ''
                for letter in w:
                    str_num += letter_dict[letter]
                word_numbers_list.append(int(str_num))
            for w in word_numbers_list[:]:
                if len(str(w)) < word_length:
                    word_numbers_list.remove(w)
            for number in word_numbers_list:
                if number == square: continue
                if number in square_list_of_size:
                    biggest_square = max([square,number,biggest_square])
                    print(word_pair,word_numbers_list)

print(biggest_square)

