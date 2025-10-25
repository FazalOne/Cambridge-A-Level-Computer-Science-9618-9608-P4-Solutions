class node:
    def __init__(self, theData, nextNodeNumber):
        self.data = theData #INTEGER
        self.nextNode = nextNodeNumber #INTEGER

def addNode(linkedList, currentPointer, emptyList):
    dataToAdd = int(input("Enter the data to add: ")) #INTEGER
    if not (emptyList < 0 or emptyList > 9):
        newNode = node(dataToAdd, -1) #node
        linkedList[emptyList] = newNode
        previousPointer = 0 #INTEGER
        while(currentPointer != -1):
            previousPointer = currentPointer
            currentPointer = linkedList[currentPointer].nextNode
        linkedList[previousPointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode
        return True
    return False

def outputNodes(linkedList, currentPointer):
        while(currentPointer != -1):
            print(str(linkedList[currentPointer].data))
            currentPointer = linkedList[currentPointer].nextNode
        
linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,7),node(56,3),node(0,9),node(0,-1)] #ARRAY OF nodes
startPointer = 0 #INTEGER
emptyList = 5 #INTEGER
outputNodes(linkedList, startPointer)
returnValue = addNode(linkedList, startPointer, emptyList) #BOOLEAN
if returnValue:
    print("Item successfully added")
else:
    print("Item not added, list full")
outputNodes(linkedList, startPointer)