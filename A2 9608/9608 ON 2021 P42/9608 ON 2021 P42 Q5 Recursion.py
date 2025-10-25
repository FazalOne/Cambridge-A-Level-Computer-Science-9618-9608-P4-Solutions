def NonRecursive(Num1, Num2):
    Value = 0 #INTEGER
    while Num1 < Num2:
        Value += Num1
        Num1 *=  2
    if Num1 > Num2:
        Value += 10
    else:
        Value += Num1
    return Value