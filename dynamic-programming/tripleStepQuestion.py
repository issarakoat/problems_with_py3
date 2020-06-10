# A child is running up a staircase with n steps and hop either 1, 2, or 3 steps at a time
# Implement method to count how many way possible ways the child can run up

def countWays(step, memo):
    if( step < 0 ):
        return 0
    elif( step == 0 ):
        return 1
    elif( memo[step] > -1):
        return memo[step]
    elif( memo[step] == -1):
        memo[step] = countWays(step - 1, memo) + countWays(step - 2, memo) + countWays(step - 3, memo)
        return memo[step]
    else:
        pass

def countWaysInit(steps):
    memo = []
    for i in range(0, steps + 1):
        memo.append(-1)
    return countWays(steps, memo)
assert(countWaysInit(3) == 4)
assert(countWaysInit(4) == 7) 
assert(countWaysInit(5) == 13)
