def PrintArray():
    global TopPointer
    print("TopPointer is: ",TopPointer)
    for x in range (0, 10):
        print(DataStack[x])

def Push(Value):
    global TopPointer
    if TopPointer == 100:
        return False
    else:
        DataStack[TopPointer] = Value
        TopPointer = TopPointer + 1
        return True

def Pop():
    global TopPointer
    if TopPointer == 0:
        return -1
    else:
        ReturnData = DataStack[TopPointer - 1]
        TopPointer = TopPointer - 1
        return ReturnData

TopPointer = 0 #INTEGER
DataStack = [0 for x in range(100)] #ARRAY OF INTEGERS
Push(10)
Push(20)
Push(6)
Push(8)
Pop()
Pop()
Push(19)
Pop()
Push(50)
print(TopPointer)
PrintArray()