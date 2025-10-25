def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return (Unknown(X + 1, Y) * 2)
    elif X == Y:
        return 1
    else:
        print(X + Y)
        return (Unknown(X - 1, Y) // 2)

def IterativeUnknown(X, Y):
    ReturnVal = 1 #INTEGER
    while not X == Y:
        print(X + Y)
        if X < Y:
            X += 1
            ReturnVal *= 2
        else:
            X -=1
            ReturnVal //= 2
    return ReturnVal

print("Recursive:")
print("X 10 Y 15 ")
print(Unknown(10, 15))
print("X 10 Y 10 ")
print(Unknown(10, 10))
print("X 15 Y 10 ")
print(Unknown(15, 10))

print("Iterative:")
print("X 10 Y 15 ")
print(IterativeUnknown(10, 15))
print("X 10 Y 10 ")
print(IterativeUnknown(10, 10))
print("X 15 Y 10 ")
print(IterativeUnknown(15, 10))