def insert(data):
    global currentPointer
    ListLength = len(LinkedList) #INTEGER
    if ListLength == 0:
        LinkedList.append([data,-1])
    else:
        LinkedList.append([data,-1])
        EntryPointer = ListLength #INTEGER
        LinkedList[currentPointer][1] = EntryPointer
        currentPointer = EntryPointer

def insertAt(data,index):
    ListLength = len(LinkedList) #INTEGER
    if ListLength == 0:
        print("Sorry, list does not exist.")
    elif index>=ListLength:
        print("Sorry, index is out of bounds.")
    else:
        currentPointer = headpointer #INTEGER
        count = 1 #INTEGER
        while count != index and currentPointer!= -1:
            currentPointer = LinkedList[currentPointer][1] 
            count +=1
        LinkedList.append([data,-1]) 
        EntryPointer = ListLength #INTEGER
        LinkedList[EntryPointer][1] = LinkedList[currentPointer][1]
        LinkedList[currentPointer][1] = EntryPointer
        OutputList()
        
def remove(data):
    if len(LinkedList) == 0:
        print("Sorry, list is empty.")
        return
    
    global headpointer
    if LinkedList[headpointer][0] == data:
        headpointer = LinkedList[headpointer][1]
        print("Data {} found at head and deleted.".format(data))
        return

    Temp = headpointer #INTEGER
    Temp2 = headpointer #INTEGER
    while Temp2 !=- 1:
        if(LinkedList[Temp2][0] == data):
            LinkedList[Temp][1] = LinkedList[Temp2][1]
            print("Data {} found at {} and deleted.".format(data,Temp2))
            if LinkedList[Temp][1] == -1: 
                global currentPointer
                currentPointer = Temp
            return
        Temp = Temp2 
    print("Data {} does not exist in list".format(data))
    return

def OutputList():
    currentPointer = headpointer #INTEGER
    if len(LinkedList) == 0:
        print("Sorry, list is empty.")
        return
    while(currentPointer != -1):
        print("CurrentPointer: {} | Data: {} | NextPointer: {}".format(currentPointer,LinkedList[currentPointer][0],str(LinkedList[currentPointer][1])))
        currentPointer = LinkedList[currentPointer][1]
def FindElement(data):
    currentPointer = headpointer #INTEGER
    while(currentPointer != -1):
        if LinkedList[currentPointer][0] == data:
            print("Search Result: CurrentPointer: {} | Data: {} | NextPointer: {}".format(currentPointer,LinkedList[currentPointer][0],str(LinkedList[currentPointer][1])))
            return
        currentPointer = LinkedList[currentPointer][1]
    print("Data {} does not exist in list".format(data))

LinkedList = [] #2D ARRAY OF INTEGERS
currentPointer = 0 #INTEGER
headpointer = currentPointer #INTEGER
insert(99)
insert(125)
insert(121)
insert(97)
insert(109)
insert(95)
insert(135)
insert(149)