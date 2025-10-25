import os
def Enqueue(data):
    global EndPointer
    print("EndPointer before enqueue:", EndPointer)
    if EndPointer == len(QueueData):
        return False
    else:
        QueueData[EndPointer] = data
        EndPointer+=1
        return True
        
def Remove():
    global StartPointer
    if(EndPointer - StartPointer < 2):
        return "No Items"
    else:
        Value1 = QueueData[StartPointer]
        StartPointer +=  1
        Value2 = QueueData[StartPointer]
        StartPointer +=  1
        return (Value1 + " " + Value2)

def ReadFile():
    FileName = input("Enter a filename: ") #STRING
    if os.path.isfile(FileName):
        with open(FileName, "r") as f:
            Flag = True #BOOLEAN
            Data = f.readline().strip() #STRING
            while Flag and Data != "":
                Flag = Enqueue(Data)
                Data = f.readline().strip()
            if Flag == False:
                return 1
            else:
                return 2
    else:
        return -1

QueueData = ["" for x in range(20)] #ARRAY OF STRINGS
StartPointer = 0 #INTEGER
EndPointer = 0 #INTEGER

ReturnValue = ReadFile() #INTEGER
match ReturnValue:
    case -1:
        print("The file could not be found")
    case 1:
        print("The queue was full, not all items were read")
    case 2:
        print("All items successfully added")