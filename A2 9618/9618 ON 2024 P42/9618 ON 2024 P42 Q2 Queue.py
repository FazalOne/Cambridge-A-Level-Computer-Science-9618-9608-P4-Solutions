class Queue:
    def __init__(self):
        self.QueueArray = [-1 for x in range(100)] #ARRAY OF INTEGER
        self.HeadPointer = -1 #INTEGER
        self.TailPointer = 0 #INTEGER

def Enqueue(AQueue, TheData):
    if AQueue.TailPointer > 99:
        return AQueue, -1
    if AQueue.HeadPointer == -1:
        AQueue.HeadPointer = 0
    AQueue.QueueArray[AQueue.TailPointer] = TheData
    AQueue.TailPointer += 1
    return AQueue, 1

def Dequeue(AQueue):
    if AQueue.HeadPointer == -1 or AQueue.HeadPointer == AQueue.TailPointer:
        return AQueue, -1
    AQueue.HeadPointer += 1
    return AQueue, AQueue.QueueArray[AQueue.HeadPointer-1]

def ReturnAllData(TheQueue):
    Temp = "" #STRING
    for X in range(TheQueue.HeadPointer, TheQueue.TailPointer):
        Temp += str(TheQueue.QueueArray[X]) + " "
    return Temp

TheQueue = Queue() #Queue
for x in range(0, 10):
    Continue = True #BOOLEAN
    while Continue:
        DataInput = int(input("Enter a positive integer: ")) #INTEGER
        Continue = DataInput > -1
    TheQueue, ReturnValue = Enqueue(TheQueue, DataInput)
    if ReturnValue == -1:
        print("Queue full")
    else:
        print("Item inserted")
print(ReturnAllData(TheQueue))

TheQueue, ReturnValue = Dequeue(TheQueue) #INTEGER, INTEGER
if ReturnValue == -1:
    print("Queue empty")
else:
    print(ReturnValue, " is returned")
    TheQueue, ReturnValue = Dequeue(TheQueue)
if ReturnValue == -1:
    print("Queue empty")
else:
    print(ReturnValue, " is returned")
print(ReturnAllData(TheQueue))