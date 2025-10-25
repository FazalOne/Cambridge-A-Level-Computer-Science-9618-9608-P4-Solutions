def InsertData():
    global FirstNode, FirstEmpty
    arr = [int(input("Enter number to insert into array: ")) for x in range(5)] #ARRAY OF INTEGER
    for x in arr:
        if FirstEmpty == -1:
            print("Linked list is full!")
        else:
            LinkedList[FirstEmpty][0] = x
            FirstEmpty = LinkedList[FirstEmpty][1]
            if FirstNode == -1:
                FirstNode = 0

def OutputLinkedList():
    currentPointer = FirstNode #INTEGER
    if currentPointer == -1:
        print("Linked list is empty")
    else:
        while currentPointer != -1:
            print(LinkedList[currentPointer][0], LinkedList[currentPointer][1])
            currentPointer = LinkedList[currentPointer][1]

def RemoveData(ItemToRemove):
    global LinkedList, FirstNode, FirstEmpty
    if LinkedList[FirstNode][0] == ItemToRemove:
        NewFirst = LinkedList[FirstNode][1] #INTEGER
        LinkedList[FirstNode] = [-1, FirstEmpty]
        FirstEmpty = FirstNode
        FirstNode = NewFirst
    else:
        if FirstNode != -1:
            CurrentPointer = FirstNode #INTEGER
            PreviousNode = -1 #INTEGER
            while(ItemToRemove != LinkedList[CurrentPointer][0] and CurrentPointer != -1):
                PreviousNode = CurrentPointer
                CurrentPointer = LinkedList[CurrentPointer][1]
            if ItemToRemove == LinkedList[CurrentPointer][0]:
                LinkedList[PreviousNode][1] = LinkedList[CurrentPointer][1]
                LinkedList[CurrentPointer][0] = -1
                LinkedList[CurrentPointer][1] = FirstEmpty
                FirstEmpty = CurrentPointer

FirstEmpty = 0 #INTEGER
FirstNode = -1 #INTEGER
LinkedList = [[-1,x] for x in range(1,20)] + [[-1,-1]] #2D ARRAY OF INTEGERS
InsertData()
OutputLinkedList()
RemoveData(5)
print("After")
OutputLinkedList()