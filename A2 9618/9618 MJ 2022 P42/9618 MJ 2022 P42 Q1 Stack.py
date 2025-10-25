def Push(DataToPush):
    global StackData, StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = DataToPush
        StackPointer += 1
    return True

def Pop():
    global StackData, StackPointer
    if StackPointer == 0:
        return -1
    else:
        ReturnData = StackData[StackPointer - 1] #INTEGER
        StackPointer -= 1
    return ReturnData

def PrintArray():
    print("StackPointer: ", StackPointer)
    for x in range(StackPointer):
        print(StackData[x])

StackData = [0 for x in range(10)] #ARRAY OF INTEGER
StackPointer = 0 #INTEGER
for x in range(0, 11):
    TempNumber = int(input("Enter a number: ")) #INTEGER
    if Push(TempNumber):
        print("Stored")
    else:
        print("Stack full")
PrintArray()
Pop()
Pop()
PrintArray()