class Node:
    def __init__(self, D, P):
        self.Data = D #STRING
        self.Pointer = P #INTEGER

    def GetData(self):
        return self.Data
    def GetPointer(self):
        return self.Pointer    
    def SetData(self,D):
        self.Data = D
    def SetPointer(self,P):
        self.Pointer = P

class LinkedList:
    def __init__(self):
        self.HeadPointer = -1 #INTEGER
        self.FreeListPointer = 0 #INTEGER
        self.NodeArray = [Node("", i+1) for i in range(8)] #ARRAY OF Nodes
        self.NodeArray[7].Pointer = -1

    def OutputListToConsole(self) :
        CurrentPointer = self.HeadPointer #INTEGER
        while CurrentPointer != -1:
            print(self.NodeArray[CurrentPointer].GetData())
            CurrentPointer = self.NodeArray[CurrentPointer].GetPointer()

    def FindInsertionPoint(self):
        PreviousPointer = self.FreeListPointer - 1
        NextPointer = self.FreeListPointer + 1
        return PreviousPointer,NextPointer

    def AddToList(self, NewData):
        NewNodePointer = self.FreeListPointer #INTEGER
        self.NodeArray[NewNodePointer].SetData(NewData)
        if self.HeadPointer == -1:
            self.FreeListPointer = self.NodeArray[self.FreeListPointer].GetPointer()
            self.HeadPointer = NewNodePointer
            self.NodeArray[NewNodePointer].SetPointer(-1)
        else:
            PreviousPointer, NextPointer = self.FindInsertionPoint()
            self.FreeListPointer = self.NodeArray[self.FreeListPointer].GetPointer()
            if PreviousPointer == -1 :
                self.NodeArray[NewNodePointer].SetPointer(self.HeadPointer)
                self.HeadPointer = NewNodePointer
            else:
                self.NodeArray[NewNodePointer].SetPointer(NextPointer)
                self.NodeArray[PreviousPointer].SetPointer(NewNodePointer)

contacts = LinkedList()
contacts.AddToList("Amy")
contacts.AddToList("Lisa")
contacts.AddToList("Wang")
contacts.OutputListToConsole()