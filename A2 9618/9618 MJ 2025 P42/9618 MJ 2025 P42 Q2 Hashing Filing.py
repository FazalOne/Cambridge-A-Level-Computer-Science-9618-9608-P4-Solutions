class Record:
    def __init__(self, pKey, pItem1, pItem2):
        self.Key = pKey #INTEGER
        self.Item1 = pItem1 #INTEGER
        self.Item2 = pItem2 #INTEGER
    def GetKey(self):
        return self.Key
    def GetItem1(self):
        return self.Item1
    def GetItem2(self):
        return self.Item2

def Initialise():
    global HashTable, Spare
    HashTable = [Record(-1,-1,-1) for x in range(200)] #ARRAY OF Records
    Spare = [Record(-1,-1,-1) for x in range(100)] #ARRAY OF Records
def CalculateHash(Key):
    return Key % 200
def InsertIntoHash(TheRecord):
    global HashTable, Spare
    HashValue = CalculateHash(TheRecord.GetKey()) #INTEGER
    if HashTable[HashValue].GetKey() == -1:
        HashTable[HashValue] = TheRecord
    else:
        for x in range(0, 100):
            if Spare[x].GetKey() == -1:
                Spare[x] = TheRecord
                break
def CreateHashTable():
    global HashTable, Spare
    try:
        with open("HashData.txt") as File:
            for Line in File:
                Data = Line.strip().split(",") #ARRAY OF STRINGS
                InsertIntoHash(Record(int(Data[0]), int(Data[1]), int(Data[2])))
    except FileNotFoundError:
        print("Cannot open file")
def PrintSpare():
    global Spare
    X = 0 #INTEGER
    while Spare[X].GetKey() != -1:
        print(Spare[X].GetKey())
        X += 1

Initialise()
CreateHashTable()
PrintSpare()