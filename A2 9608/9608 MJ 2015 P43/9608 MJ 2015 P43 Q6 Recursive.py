def X(n):
    if (n == 0) or (n == 1):
        print(n, end="")
    else:
        X(n // 2)
        print(n % 2, end="")
X(40)