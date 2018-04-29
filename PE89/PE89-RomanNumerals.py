"""
PROJECT EULER PROBLEM 89 - Roman Numerals
For a number written in Roman numerals to be considered valid there
are basic rules which must be followed. Even though the rules allow
some numbers to be expressed in more than one way there is always a
"best" way of writing a particular number.

For example, it would appear that there are at least six ways of
writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and
the last example is considered to be the most efficient, as it uses
the least number of numerals.

The 11K text file, roman.txt contains one thousand numbers written
in valid, but not necessarily minimal, Roman numerals; see About...
Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in
their minimal form.

Note: You can assume that all the Roman numerals in the file
contain no more than four consecutive identical units.
"""

# Parse numerals list
def readNumerals():
    numeral_list = []
    with open("p089_roman.txt") as file:
        for line in file:
            numeral = line.rstrip("\n")
            yield(numeral)


numeral_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
value_dict = {}
value_dict[1] = 'I'
value_dict[4] = 'IV'
value_dict[5] = 'V'
value_dict[9] = 'IX'
value_dict[10] = 'X'
value_dict[40] = 'XL'
value_dict[50] = 'L'
value_dict[90] = 'XC'
value_dict[100] = 'C'
value_dict[400] = 'CD'
value_dict[500] = 'D'
value_dict[900] = 'CM'
value_dict[1000] = 'M'
value_dict_keys = list(reversed(sorted(value_dict.keys())))

total_savings = 0
for numeral in readNumerals():
    value = 0
    d = 0
    while d < len(numeral):
        num_this = numeral_dict[numeral[d]]
        if d == len(numeral) - 1:
            value += num_this
            break
        num_next = numeral_dict[numeral[d+1]]
        if num_this < num_next:
            value += num_next - num_this
            d += 2
        else:
            value += num_this
            d += 1
    new_numeral = ''
    num_value = value
    for numeral_value in value_dict_keys:
        while value >= numeral_value:
            new_numeral += value_dict[numeral_value]
            value -= numeral_value
    savings = len(numeral)-len(new_numeral)
    if savings > 0:
        #print(numeral,num_value,new_numeral)
        total_savings += savings
        #print(savings)

print(total_savings)
# 743 characters
