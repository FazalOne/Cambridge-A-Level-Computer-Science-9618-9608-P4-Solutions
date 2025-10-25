def PrintArray():
    global StackPointer
    print("StackPointer is: ",StackPointer)
    for x in range (0, 20):
        print(Parts[x])
def Push(Value):
    global StackPointer
    if StackPointer > 19:
        print("Stack full")
    else:
        Parts[StackPointer] = Value
        StackPointer = StackPointer + 1
        return True
def Pop():
    global StackPointer
    if StackPointer == 0:
        print("The stack is empty")
    else:
        StackPointer -= 1
        print(Parts[StackPointer])
        Parts[StackPointer] = '*'
StackPointer = 0 #INTEGER
Parts = ["" for x in range(20)] #ARRAY OF STRING
Push("Screw 1")
Push("Screw 2")
Push("Back case")
Push("Screw 3")
Push("Engine outer")
Pop()
Pop()
Push("Light 1")
Push("Light 2")
Push("Wheel 1")
Pop()
Pop()
PrintArray()