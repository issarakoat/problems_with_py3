
def fibonacci(n):
    if(n == 0):
        return 0
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return a + b
assert(fibonacci(1) == 1)
assert(fibonacci(2) == 1)
assert(fibonacci(3) == 2)
assert(fibonacci(4) == 3)
assert(fibonacci(5) == 5)
assert(fibonacci(6) == 8)
assert(fibonacci(7) == 13)