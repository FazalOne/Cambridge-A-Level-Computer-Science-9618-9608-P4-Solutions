class Node:
    def __init__(self):
        self.LeftPointer = -1 #INTEGER
        self.RightPointer = -1 #INTEGER
        self.Data = "" #STRING

class BinaryTree:
    def __init__(self):
        self.NextNode = 0 #INTEGER

    def CreateTree(self,NodeData,Nodes):
        self.NodeArray = ["" for x in range(Nodes)] #ARRAY OF Nodes
        self.NodeArray[self.NextNode] = Node()
        self.NodeArray[self.NextNode].Data = NodeData

    def AttachLeft(self,NodeData,ParentNode):
        self.NextNode += 1
        self.NodeArray[self.NextNode] = Node()
        self.NodeArray[self.NextNode].Data = NodeData
        self.NodeArray[ParentNode].LeftPointer = self.NextNode

    def AttachRight(self,NodeData,ParentNode):
        self.NextNode += 1
        self.NodeArray[self.NextNode] = Node()
        self.NodeArray[self.NextNode].Data = NodeData
        self.NodeArray[ParentNode].RightPointer = self.NextNode

    def FindLeaves(self,CurrentNode):
        if(self.NodeArray[CurrentNode].LeftPointer != -1):
            self.FindLeaves(self.NodeArray[CurrentNode].LeftPointer)
        if(self.NodeArray[CurrentNode].RightPointer != -1):
            self.FindLeaves(self.NodeArray[CurrentNode].RightPointer)
        if((self.NodeArray[CurrentNode].RightPointer == -1) and(self.NodeArray[CurrentNode].LeftPointer == -1)):
            print(self.NodeArray[CurrentNode].Data)
        return

    def TraverseTree(self,Root):
        if (self.NodeArray[Root].LeftPointer != -1):
            self.TraverseTree(self.NodeArray[Root].LeftPointer)
        print(self.NodeArray[Root].Data)
        if (self.NodeArray[Root].RightPointer != -1):
            self.TraverseTree(self.NodeArray[Root].RightPointer)

NameTree = BinaryTree() #BinaryTree
NameTree.CreateTree("Red",14)
NameTree.AttachLeft("Blue", 0)
NameTree.AttachRight("Green", 0)
NameTree.AttachRight("Black", 2)
NameTree.AttachLeft("Brown", 2)
NameTree.AttachLeft("Peach", 3)
NameTree.AttachLeft("Yellow", 1)
NameTree.AttachRight("Purple", 1)
NameTree.AttachLeft("White", 6)
NameTree.AttachLeft("Pink", 7)
NameTree.AttachLeft("Grey", 9)
NameTree.AttachRight("Orange", 9)
NameTree.TraverseTree(0)
print()
NameTree.FindLeaves(0)