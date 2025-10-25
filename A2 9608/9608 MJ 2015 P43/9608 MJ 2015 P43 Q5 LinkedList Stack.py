class Node:
    def __init__(self, Name, Pointer):
        self.Name = Name #STRING
        self.Pointer = Pointer #INTEGER
def CreateStack():
    Stack=[Node("",x) for x in range(1,10)] #ARRAY OF NODES
    Stack.append(Node("",-1))
    return Stack
def Push(NewName):
    global FreePointer, TopofStackPointer
    if FreePointer == -1:
        print("Error stack is full")
    else:
        TempPointer = FreePointer #INTEGER
        Stack[TempPointer].Name = NewName
        FreePointer = Stack[TempPointer].Pointer
        Stack[TempPointer].Pointer = TopofStackPointer
        TopofStackPointer = TempPointer
def Pop():
    global FreePointer, TopofStackPointer
    if TopofStackPointer == 0:
        print("Error stack is empty")
    else:
        FreePointer = TopofStackPointer
        TopofStackPointer = TopofStackPointer-1
def PrintStack():
    if TopofStackPointer == -1:
        print("Error Stack is empty")
        return
    CurrentPointer = TopofStackPointer #INTEGER
    while CurrentPointer != -1:
        print(Stack[CurrentPointer].Name)
        CurrentPointer = Stack[CurrentPointer].Pointer
    print()

TopofStackPointer = -1 #INTEGER
FreePointer = 0 #INTEGER
Stack = CreateStack()
Push("Ali")
Push("Jack")
Push("Ben")
Push("Ahmed")
Pop()
Push("Jatinder")
Pop()
PrintStack()