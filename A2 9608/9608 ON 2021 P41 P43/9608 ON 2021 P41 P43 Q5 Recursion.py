def Recursion(a, b):
    if a <= 100:
        return 1
    else:
        if a > b:
            return 5 + Recursion(a - 1, b)
        else:
            return 10 + Recursion(a - 10, b)

def Iterative(a, b):
    while True:
        if a <= 100:
            return 1
        elif a > b:
            a -= 1
            result = 5
        else:
            a -= 10
            result = 10
        a += result
print(Recursion(104, 102))