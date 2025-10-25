class Node:
    def __init__(self):
        self.LeftPointer = -1 #INTEGER
        self.Data = None #INTEGER
        self.RightPointer = -1 #INTEGER
 
BinaryTree = [Node() for x in range(8)] #ARRAY OF Nodes
FreePointer = 0 #INTEGER
RootNode = 0 #INTEGER

def AddData(NewData):
    global FreePointer, RootNode

    NewNode = Node() #Node
    NewNode.Data = NewData
    BinaryTree[FreePointer] = NewNode
    PositionFound = False #BOOLEAN
    Pointer = RootNode #INTEGER
    print(BinaryTree[Pointer].LeftPointer," ",BinaryTree[Pointer].RightPointer)
    if FreePointer == 0:
        BinaryTree[FreePointer] = NewNode
    else:
        while not PositionFound:
            if NewNode.Data < BinaryTree[Pointer].Data:
                if BinaryTree[Pointer].LeftPointer == -1:
                    BinaryTree[Pointer].LeftPointer = FreePointer
                    PositionFound = True
                else:
                    Pointer = BinaryTree[Pointer].LeftPointer
            else:
                if BinaryTree[Pointer].RightPointer == -1:
                    BinaryTree[Pointer].RightPointer = FreePointer
                    PositionFound = True
                else:
                    Pointer = BinaryTree[Pointer].RightPointer
    print(Pointer)
    print(BinaryTree[Pointer].LeftPointer," ",BinaryTree[Pointer].RightPointer)
    FreePointer += 1

def InOrder(RootNode):
    if BinaryTree[RootNode].LeftPointer!= -1:
        InOrder(BinaryTree[RootNode].LeftPointer)
    print(str(BinaryTree[RootNode].Data))
    if BinaryTree[RootNode].RightPointer != -1:
        InOrder(BinaryTree[RootNode].RightPointer)

AddData(23)
print()
AddData(5)
print()
AddData(8)
print()
AddData(100)
print()
AddData(9)
print()
AddData(88)
print()
InOrder(0)