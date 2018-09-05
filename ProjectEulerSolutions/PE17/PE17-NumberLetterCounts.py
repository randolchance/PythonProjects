# PROJECT EULER PROBLEM 17 - Number Letter Counts

digit_dicts = {}
digit_dicts[1] = 'one'
digit_dicts[2] = 'two'
digit_dicts[3] = 'three'
digit_dicts[4] = 'four'
digit_dicts[5] = 'five'
digit_dicts[6] = 'six'
digit_dicts[7] = 'seven'
digit_dicts[8] = 'eight'
digit_dicts[9] = 'nine'
digit_dicts[10] = 'ten'
digit_dicts[11] = 'eleven'
digit_dicts[12] = 'twelve'
digit_dicts[13] = 'thirteen'
digit_dicts[14] = 'fourteen'
digit_dicts[15] = 'fifteen'
digit_dicts[16] = 'sixteen'
digit_dicts[17] = 'seventeen'
digit_dicts[18] = 'eighteen'
digit_dicts[19] = 'nineteen'
digit_dicts[20] = 'twenty'
digit_dicts[30] = 'thirty'
digit_dicts[40] = 'forty'
digit_dicts[50] = 'fifty'
digit_dicts[60] = 'sixty'
digit_dicts[70] = 'seventy'
digit_dicts[80] = 'eighty'
digit_dicts[90] = 'ninety'

length = 0
for n in range(1,1001):
    out_str = ''

    bigger_num = False
    if n >= 1000:
        length += len('thousand')
        k = n//1000
        n %= 1000
        length += len(digit_dicts[k])
        out_str += digit_dicts[k] + " thousand"
        bigger_num = True
        
    if n >= 100:
        length += len('hundred')
        k = n//100
        n %= 100
        length += len(digit_dicts[k])
        out_str += " " + digit_dicts[k] + " hundred"
        bigger_num = True

    
    if bigger_num and n > 0:
        length += len('and')
        out_str += ' and'
        
    if n >= 10:
        if n in digit_dicts:
            length += len(digit_dicts[n])
            out_str += " " + digit_dicts[n]
            n = 0
        else:
            k = 10*(n//10)
            n %= 10
            length += len(digit_dicts[k])
            out_str += " " + digit_dicts[k]
            
    if n in digit_dicts:
        length += len(digit_dicts[n])
        out_str += " " + digit_dicts[n]
    print(out_str)

print(length)

