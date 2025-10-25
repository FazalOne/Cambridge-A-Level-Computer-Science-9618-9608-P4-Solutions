class Node:
    def __init__(self,pdata):
        self.LeftPointer = -1   #INTEGER
        self.RightPointer = -1  #INTEGER
        self.Data = int(pdata)  #INTEGER
    def GetLeft(self):
        return self.LeftPointer
    def GetRight(self):
        return self.RightPointer
    def GetData(self):
        return self.Data
    def SetLeft(self, left):
        self.LeftPointer = left
    def SetRight(self, right):
        self.LeftPointer = right
    def SetData(self, data):
        self.Data = data

class TreeClass:
    def __init__(self):
        self.Tree = [Node(-1) for x in range(20)]   #ARRAY OF NODES
        self.FirstNode = -1     #INTEGER
        self.NumberNodes = 0    #INTEGER
    def InsertNode(self,NewNode):
        if self.NumberNodes == 20:
            print("Tree is full")
            return
        self.Tree[self.NumberNodes] = NewNode
        if self.NumberNodes == 0:
            self.NumberNodes += 1
            self.FirstNode = 0
        else:
            found = False
            currentindex = self.FirstNode
            while not found and currentindex != -1:
                if self.Tree[currentindex].Data >= NewNode.Data:
                    if self.Tree[currentindex].LeftPointer == -1:
                        self.Tree[currentindex].LeftPointer = self.NumberNodes
                        found = True
                    else:
                        currentindex = self.Tree[currentindex].LeftPointer
                else:
                    if self.Tree[currentindex].RightPointer == -1:
                        self.Tree[currentindex].RightPointer = self.NumberNodes
                        found = True
                    else:
                        currentindex = self.Tree[currentindex].RightPointer
            self.NumberNodes += 1
    def OutputTree(self):
        if self.NumberNodes == 0:
            print("No nodes")
        else:
            for x in range(self.NumberNodes):
                print(self.Tree[x].GetLeft(), end="\t")
                print(self.Tree[x].GetData(), end="\t")
                print(self.Tree[x].GetRight())

TheTree = TreeClass() #TreeClass
arr = [10,11,5,1,20,7,15] #ARRAY OF INTEGER
for x in arr:
    TheTree.InsertNode(Node(x))
TheTree.OutputTree()