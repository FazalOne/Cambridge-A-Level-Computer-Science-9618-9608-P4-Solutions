class Node:
    def __init__(self, data, ptr1,ptr2):
        self.Data = data #STRING
        self.LeftPointer = ptr1 #INTEGER
        self.RightPointer = ptr2 #INTEGER

def TraverseTree(RootPointer):
    if Tree[RootPointer].LeftPointer != -1:
        TraverseTree(Tree[RootPointer].LeftPointer)
    if Tree[RootPointer].RightPointer != -1:
        TraverseTree(Tree[RootPointer].RightPointer)
    print(Tree[RootPointer].Data)

RootPointer = 0 #INTEGER
FreePointer = 7 #INTEGER
Tree = [Node("", -1, -1) for x in range(10)] #ARRAY OF Nodes
Tree[0] = Node("D",4,1)
Tree[1] = Node("F",2,3)
Tree[2] = Node("E",-1,-1)
Tree[3] = Node("G",-1,-1)
Tree[4] = Node("B",6,5)
Tree[5] = Node("C",-1,-1)
Tree[6] = Node("A",-1,-1)
TraverseTree(RootPointer)