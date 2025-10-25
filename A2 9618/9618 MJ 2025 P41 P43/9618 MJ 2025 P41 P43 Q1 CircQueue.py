def Enqueue(Data):
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems >= 20:
        return False
    if TailPointer == -1:
        HeadPointer = 0
        Queue[TailPointer] = Data
    TailPointer += 1
    if TailPointer == 20:
        TailPointer = 0
    Queue[TailPointer] = Data
    NumberItems +=1
    return True

def Dequeue():
    global Queue, HeadPointer, TailPointer, NumberItems
    if NumberItems <= 0:
        return -1
    else:
        ReturnValue = Queue[HeadPointer] #INTEGER
        HeadPointer +=1
        if HeadPointer >= 20:
            HeadPointer = 0
            NumberItems -=1
        if NumberItems == 0:
            HeadPointer = -1
            TailPointer = -1
        return ReturnValue

Queue = [-1 for x in range(20)] #ARRAY OF #INTEGER
HeadPointer = -1 #INTEGER
TailPointer = -1 #INTEGER
NumberItems = 0 #INTEGER
for x in range(1, 26):
    if Enqueue(x):
        print(x,"Successful")
    else:
        print(x,"Unsuccessful")
print(Dequeue())
print(Dequeue())