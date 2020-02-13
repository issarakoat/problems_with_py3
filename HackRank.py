import re
def SayHello():
    print('yo motherfucker!')
def birthdayCakeCandles(ar):
    sort = sorted(ar)
    high = (sort[len(sort)-1]) 
    res = sort.count(high)
    return res
    #convert 12 clock system to 24 clock system
def timeConversion(s):
    PM = re.search("PM", s)
    hh = int(s[0]+s[1])
    the_less = s[2:len(s)-2]
    if PM:# check if PM
        if hh != 12:
            hh += 12
        return str(hh)+the_less
    else:
        if hh == 12:
            return '00' + the_less
        if hh < 10:
            return '0'+str(hh) + the_less
        return str(hh) + the_less
def gradingStudents(grades):
    # Write your code here
    res = []
    for grade in grades:
        if grade < 38:
            res.append(grade)
        elif grade % 5 >= 3:
            mainder = grade % 5
            mainder = 5 - mainder
            res.append(grade + mainder)
        else:
            res.append(grade)
    return res
def jumpingOnClouds(c):
    jump = -1
    index = 0
    while index < len(c):
        #if 2 jumps available, do it. count the jump, update the the index
        if index + 2 < len(c) and c[index+2] != 1:
            jump += 1
            index += 2
        else:
            jump += 1
            index += 1
    return jump
def repeatedString(s, n):
    count = 0
    count_remainder = 0
    time = n // len(s)
    for i in s:
        if i == 'a':
            count += 1
    mod = n % len(s)
    if mod == 0:
        return count * time
    else:
        for i in range(0, mod):
            if s[i] == 'a':
                count_remainder += 1
        return (count * time) + count_remainder

def rotLeft(a, d):
    res = []
    target_index = (len(a) - 1) - d
    for i in range(0, len(a)):
        if i >= d:
            res.append(a[i])
    for j in range(0, len(a) - 1 - target_index):
        res.append(a[j])
    return res

# cant really go that big :( maybe like 990
def factorial_recur(num):
    if num == 0:
        return 1
    return num * factorial_recur(num-1)
def factorial_iter(num):
    res = 1
    while num > 1:
        res *= num
        num -= 1
    return res
