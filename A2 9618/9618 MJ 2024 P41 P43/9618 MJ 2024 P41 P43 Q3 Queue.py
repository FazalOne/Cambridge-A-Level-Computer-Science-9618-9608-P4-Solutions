def Enqueue(data):
    global QueueData, QueueHead, QueueTail
    if QueueTail == len(QueueData):
        return False
    if QueueHead == -1:
        QueueHead = 0
        QueueTail = 0
    QueueData[QueueTail] = data
    QueueTail += 1
    return True

def Dequeue():
    global QueueData, QueueHead, QueueTail
    if QueueHead == QueueTail or QueueHead == -1:
        print("Queue is empty")
        return False
    QueueHead += 1
    return QueueData[QueueHead - 1]

def StoreItems():
    count = 0
    for x in range(10):
        data = input("Enter the 7 character string: ")
        Total = int(data[0]) * 1 + int(data[1]) * 3 + int(data[2]) * 1 + int(data[3]) * 3 + int(data[4]) * 1 + int(data[5]) * 3
        Digit = Total // 10
        if Digit == 10:
            Digit = "X"
        if str(Digit) == str(data[6]):
            print("Input is valid!")
            if Enqueue(data[0:6]):
                print("Data is successfully enqueued!")
            else:
                print("Queue is full")
        else:
            print("Input is not valid!")
            count += 1
    print("Invalid inputs: ", count)

QueueData = ["" for x in range(20)] #ARRAY OF STRINGS
QueueHead = -1 #INTEGER
QueueTail = -1 #INTEGER
StoreItems()
returnVal = Dequeue() #INTEGER
if returnVal != False:
    print("Data dequeued: ", returnVal)