def PrintArray():
    global Top
    print("StackPointer is: ",Top)
    for x in range (0, Top+1):
        print(StackData[x])

def Push(Data):
    global Top
    if Top == 8:
        return False
    else:
        Top += 1
        StackData[Top] = Data
        return True

def Pop():
    global Top
    if Top == 0:
        return -1
    else:
        ReturnData = StackData[Top - 1]
        Top -= 1
        return ReturnData

Top = -1 #INTEGER
StackData = [0 for x in range(8)] #ARRAY OF INTEGER
Push(20)
Push(35)
Push(43)
Push(55)
PrintArray()
Pop()
Pop()
Push(10)
PrintArray()
Pop()
Push(50)
Push(55)
Pop()
Push(65)
PrintArray()