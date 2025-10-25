class SaleData:
    def __init__(self, NewID, Quantity):
        self.ID = NewID #STRING
        self.Quantity = Quantity #INTEGER

def Enqueue(data):
    global CircularQueue, Tail, NumberOfItems
    if NumberOfItems == len(CircularQueue):
        return -1
    CircularQueue[Tail] = data
    Tail += 1
    if Tail == len(CircularQueue):
        Tail = 0
    NumberOfItems += 1
    return 1

def Dequeue():
    global CircularQueue, Head, NumberOfItems
    RecordRemoved = SaleData("", -1)
    if not NumberOfItems == 0:
        RecordRemoved = CircularQueue[Head]
        Head += 1
        if Head == len(CircularQueue):
            Head = 0
        NumberOfItems -= 1
    return RecordRemoved

def EnterRecord():
    id = input("Enter ID: ")
    quantity = input("Enter quantity: ")
    if Enqueue(SaleData(id,quantity)) == -1:
        print("Full")
    else:
        print("Stored")

CircularQueue = [SaleData("",-1) for x in range(5)] #ARRAY OF SaleData
Head = 0 #INTEGER
Tail = 0 #INTEGER
NumberOfItems = 0 #INTEGER

for x in range(6):
    EnterRecord()
RemovedRecord = Dequeue() #SaleData
if RemovedRecord.ID == "":
    print("Empty")
else:
    print("ID :",RemovedRecord.ID, "Quantity :",RemovedRecord.Quantity)
EnterRecord()
temp = Head #INTEGER
for x in range(NumberOfItems):
    print("ID :", CircularQueue[temp].ID, "Quantity :", CircularQueue[temp].Quantity)
    temp += 1
    if temp == len(CircularQueue):
        temp = 0