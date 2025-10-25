class Node:
    def __init__(self, Name, Pointer):
        self.Name = Name #STRING
        self.Pointer = Pointer #INTEGER
def CreateQueue():
    Queue = [Node("",x) for x in range(1,10)] #ARRAY OF NODES
    Queue.append(Node("",-1))
    return Queue
def AddName(NewName):
    global FreePointer, HeadPointer, TailPointer
    if FreePointer == -1:
        print("Error")
    else:
        CurrentPointer = FreePointer #INTEGER
        Queue[CurrentPointer].Name = NewName
        FreePointer = Queue[CurrentPointer].Pointer
        if HeadPointer == -1:
            HeadPointer = CurrentPointer
        Queue[CurrentPointer].Pointer = -1
        Queue[TailPointer].Pointer = CurrentPointer
        TailPointer = CurrentPointer
def RemoveName():
    global FreePointer, HeadPointer, TailPointer
    if HeadPointer == -1:
        print("Error")
    else:
        print("Dequeud: ",Queue[HeadPointer].Name)
        CurrentPointer = HeadPointer #INTEGER
        HeadPointer = Queue[CurrentPointer].Pointer
        if HeadPointer == -1:
            TailPointer = -1
        Queue[CurrentPointer].Pointer = FreePointer
        FreePointer = CurrentPointer

def PrintQueue():
    global HeadPointer
    CurrentPointer = HeadPointer #INTEGER
    while CurrentPointer != -1:
        print(Queue[CurrentPointer].Name)
        CurrentPointer = Queue[CurrentPointer].Pointer
    print()
HeadPointer = -1 #INTEGER
FreePointer = 0 #INTEGER
TailPointer = -1 #INTEGER
Queue = CreateQueue() #ARRAY OF NODES
AddName("Ali")
AddName("Jack")
AddName("Ben")
AddName("Ahmed")
PrintQueue()
RemoveName()
PrintQueue()
AddName("Jatinder")
PrintQueue()
RemoveName()
PrintQueue()