class RecordData:
    def __init__(self):
        self.ID = "" #STRING
        self.Total = 0 #INTEGER

def Enqueue(data):
    global Queue, HeadPointer, TailPointer
    if TailPointer == 50:
        print("Sorry, queue is full.")
    else:
        Queue[TailPointer] = data
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0
        print("Data Enqueued.")

def Dequeue():
    global HeadPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Sorry, Queue is empty.")
        return "Empty"
    else:
        HeadPointer += 1
        print("Dequeued")
        return Queue[HeadPointer - 1]

def ReadData():
    try:
        with open("QueueData.txt","r") as File:
            for Line in File:
                Enqueue(Line.strip("\n"))
    except FileNotFoundError:
        print("File not found, please check your filename or path.")

def TotalData():
    global NumberRecords, Records
    DataAccessed = Dequeue() #STRING
    if NumberRecords == 0:
        Records[NumberRecords].ID = DataAccessed
        Records[NumberRecords].Total = 1
        NumberRecords += 1
    else:
        Flag = False #BOOLEAN
        for X in range(NumberRecords - 1):
            if Records[X].ID == DataAccessed:
                Records[X].Total += 1
                Flag = True
        if not Flag:
            Records[NumberRecords].ID = DataAccessed
            Records[NumberRecords].Total = 1
            NumberRecords += 1

def OutputRecords():
    for x in range(NumberRecords):
        print("ID {} Total {}".format(Records[x].ID,Records[x].Total))

Queue = ["" for x in range(50)] #ARRAY OF STRING
HeadPointer = -1 #INTEGER
TailPointer = 0 #INTEGER
ReadData()
Records = [RecordData() for x in range(50)] #ARRAY OF RecordData
NumberRecords = 0 #INTEGER
while HeadPointer != TailPointer:
    TotalData()
OutputRecords()