def Enqueue(DataToAdd):
    global QueueArray,TailPointer,NoItems
    if NoItems == len(QueueArray):
        return False
    QueueArray[TailPointer] = DataToAdd
    TailPointer += 1
    if TailPointer > 9:
        TailPointer = 0
    NoItems += 1
    return True

def Dequeue():
    global QueueArray,HeadPointer,NoItems
    if NoItems == 0:
        return "FALSE"
    ReturnData = QueueArray[HeadPointer]
    HeadPointer += 1
    if HeadPointer > 9:
        HeadPointer = 0
    NoItems -= 1
    return ReturnData

QueueArray = ["" for x in range(10)] #ARRAY OF STRING
HeadPointer = 0 #INTEGER
TailPointer = 0 #INTEGER
NoItems = 0 #INTEGER

for x in range(11):
    if Enqueue(input("Enter data: ")):
        print("Data added!")
    else:
        print("Queue is full!")
print(Dequeue())
print(Dequeue())

temp = HeadPointer #INTEGER
for x in range(NoItems):
    print(QueueArray[temp])
    temp += 1
    if temp > 9:
        temp = 0