#array shit

#test for unique string no addition data structure
def IsUnique(s):
    if s == "":
        return True
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            # print(ord(s[j])) to get ascii num
            if s[i] == s[j]:
                return False
    return True
assert(IsUnique('abcd')==True)
assert(IsUnique('absa')==False)
assert(IsUnique('')==True)

def IsUnique_1(s):
    set_len = len(set(s))
    return set_len == len(s)
assert(IsUnique_1('abcd')==True)
assert(IsUnique_1('absa')==False)

def IsUnique_2(s):
    check_arr = []
    for i in range(0, 128):
        check_arr.append(False)
    for i in range(0, len(s)):
        val = ord(s[i])
        if check_arr[val]:
            return False
        check_arr[val] = True
    return True
assert(IsUnique_2('abcd')==True)
assert(IsUnique_2('absa')==False)