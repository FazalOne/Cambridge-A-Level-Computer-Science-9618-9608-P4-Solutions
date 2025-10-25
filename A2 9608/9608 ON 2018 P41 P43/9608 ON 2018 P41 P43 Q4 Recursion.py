def Calculate(Number):
    Value = -10 #INTEGER
    for count in range(1,Number+1):
        Value *= count
    return Value
print(Calculate(3))