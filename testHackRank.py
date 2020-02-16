import HackRank
arr = [3,2,1,3]
assert(HackRank.birthdayCakeCandles(arr) == 2)

tc = HackRank.timeConversion('06:40:03AM')
# print(tc)

arr = [4,73,67,38,33]
assert(HackRank.gradingStudents(arr) == [4, 75, 67, 40, 33])

arr = [0, 0, 0, 0, 1, 0]
assert(HackRank.jumpingOnClouds(arr) == 3)


repeatedString_problem = HackRank.repeatedString('aba',10)
assert(repeatedString_problem == 7)

arr = [1, 2, 3, 4, 5]
arr1 = [41,73, 89 ,7 ,10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
arr2 = [33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60, 87, 97]
assert(HackRank.rotLeft(arr, 4)==[5, 1, 2, 3, 4,])
assert(HackRank.rotLeft(arr1, 10)==[77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77])
assert(HackRank.rotLeft(arr2, 13)==[87, 97, 33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60])


# test = 30000
# factorial_recur = HackRank.factorial_recur(test)
# print(factorial_recur)

# factorial_iter = HackRank.factorial_iter(test)
# print(factorial_iter)

test = 900
print(HackRank.sum_recur(test))