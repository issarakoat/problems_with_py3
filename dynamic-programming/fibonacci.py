
def fibonacci(n):
    if(n == 0):
        return 0
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)
    return a + b
print(fibonacci(7))