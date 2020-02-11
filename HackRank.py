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