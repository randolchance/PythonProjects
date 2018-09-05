# PROJECT EULER PROBLEM 19 - Counting Sundays

months = {}
months[1] = 31
months[2] = 28
months[3] = 31
months[4] = 30
months[5] = 31
months[6] = 30
months[7] = 31
months[8] = 31
months[9] = 30
months[10] = 31
months[11] = 30
months[12] = 31

year = 1900
month = 1
day = 7
leap = False

count = 0
while year <= 2000:
    day += 7
    if day > months[month]:
        day %= months[month]
        month += 1
        if leap and month == 3:
            day -= 1
        if month > 12:
            month %= 12
            year += 1
            leap = (year%4==0) and ((year%100!=0) or (year%400==0))
    if day == 1 and year > 1900:
        print("Sunday {}/{}/{} Leap: {}".format(day,month,year,leap))
        count += 1

print(count)
    
