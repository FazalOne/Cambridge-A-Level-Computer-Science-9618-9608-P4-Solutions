class Node:
    def __init__(self, data):
        self.data = data #INTEGER
        self.Pointer = -1 #INTEGER

def insert(Node):
    global currentpointer
    ListLength = len(LinkedList) #INTEGER
    if ListLength == 0:
        LinkedList.append(Node)
    else:
        LinkedList.append(Node)
        EntryPointer = ListLength
        LinkedList[currentpointer].Pointer = EntryPointer
        currentpointer = EntryPointer

def DeleteNode(data):
    if len(LinkedList) == 0:
        print("Sorry, list is empty.")
        return

    global headpointer
    if LinkedList[headpointer].data == data:
        headpointer = LinkedList[headpointer].Pointer
        print("Data {} found at head and deleted.".format(data))
        return

    Temp = headpointer #INTEGER
    Temp2 = headpointer #INTEGER
    while Temp2 != -1:
        if LinkedList[Temp2].data == data:
            LinkedList[Temp].Pointer = LinkedList[Temp2].Pointer
            print("Data {} found at {} and deleted.".format(data,Temp2))
            if LinkedList[Temp].Pointer == -1:
                global currentPointer
                currentPointer = Temp
            return
        Temp = Temp2
        Temp2 = LinkedList[Temp2].Pointer
    print("Data {} does not exist in list".format(data))
    return

def OutputList():
    currentPointer = headpointer #INTEGER
    if len(LinkedList) == 0:
        print("Sorry, list is empty.")
        return
    while(currentPointer != -1):
        print("CurrentPointer: {} | Data: {} | NextPointer: {}".format(currentPointer,LinkedList[currentPointer].data,str(LinkedList[currentPointer].Pointer)))
        currentPointer = LinkedList[currentPointer].Pointer

def FindValue(data):
    currentPointer = headpointer #INTEGER
    while(currentPointer != -1):
        if LinkedList[currentPointer].data == data:
            print("Search Result: CurrentPointer: {} | Data: {} | NextPointer: {}".format(currentPointer,LinkedList[currentPointer].data,str(LinkedList[currentPointer].Pointer)))
            return currentPointer
        currentPointer = LinkedList[currentPointer].Pointer
    print("No such data exists")
    return -1

LinkedList = [] #ARRAY OF Nodes
currentpointer = 0 #INTEGER
headpointer = currentpointer #INTEGER
insert(Node(77))
insert(Node(69))
insert(Node(54))
insert(Node(82))
insert(Node(96))

print(FindValue(96))

print()
OutputList()
print()

print(DeleteNode(54))
OutputList()
print()

print(DeleteNode(74))
OutputList()
print()

print(DeleteNode(96))
OutputList()