class Node:
    def __init__(self):
        self.LeftPointer = -1 #INTEGER
        self.RightPointer = -1 #INTEGER
        self.Data = "" #STRING

def CreateTree():
    Tree = [Node() for x in range(9)] #ARRAY OF NODES
    RootPointer = -1 #INTEGER
    FreePointer = 0 #INTEGER
    for Index in range(9):
        Tree[Index].LeftPointer = Index + 1
        Tree[Index].RightPointer = -1
    Tree[8].LeftPointer = -1
    return Tree, RootPointer, FreePointer

def AddToTree(NewDataItem):
    global RootPointer, FreePointer, BinaryTree
    if FreePointer == -1:
        print("No free space left")
    else:
        NewNodePointer = FreePointer #INTEGER
        BinaryTree[NewNodePointer].Data = NewDataItem
        FreePointer = BinaryTree[FreePointer].LeftPointer
        BinaryTree[NewNodePointer].LeftPointer = -1
        if RootPointer == -1:
            RootPointer = NewNodePointer
        else:
            FindInsertionPoint(NewDataItem, RootPointer, NewNodePointer)

def FindInsertionPoint(NewDataItem, CurrentIndex, NewNodePointer):
    global BinaryTree
    if BinaryTree[CurrentIndex].Data > NewDataItem:
        if BinaryTree[CurrentIndex].LeftPointer == -1:
            BinaryTree[CurrentIndex].LeftPointer = NewNodePointer
        else:
            FindInsertionPoint(NewDataItem, BinaryTree[CurrentIndex].LeftPointer, NewNodePointer)
    else:
        if BinaryTree[CurrentIndex].RightPointer == -1:
            BinaryTree[CurrentIndex].RightPointer = NewNodePointer
        else:
            FindInsertionPoint(NewDataItem, BinaryTree[CurrentIndex].RightPointer, NewNodePointer)

def TraverseTree(Root):
    global BinaryTree
    if Root != -1:
        TraverseTree(BinaryTree[Root].LeftPointer)
        print(BinaryTree[Root].Data)
        TraverseTree(BinaryTree[Root].RightPointer)

BinaryTree, RootPointer, FreePointer = CreateTree() 
AddToTree("C")
AddToTree("A")
AddToTree("D")
AddToTree("B")
AddToTree("E")
TraverseTree(RootPointer)