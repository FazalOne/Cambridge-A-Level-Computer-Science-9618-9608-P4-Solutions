def ReadData():
    DataList = [] #ARRAY OF STRINGS
    try:
        with open(input("Enter the filename: "), 'r') as File:
            DataList = File.read().split()
    except FileNotFoundError:
        print("Check filename, file not found")
    return DataList

def StoreData(DataToStore, FileName):
    try:
        with open(FileName,"a+") as File:
            for Item in DataToStore:
                File.write(Item)
                File.write("\n")
    except FileExistsError:
        print("The file could not be opened")

def SplitData(DataArray):
    Red = [] #ARRAY OF STRINGS
    Green = [] #ARRAY OF STRINGS
    Blue = [] #ARRAY OF STRINGS
    Orange = [] #ARRAY OF STRINGS
    Yellow = [] #ARRAY OF STRINGS
    Pink = [] #ARRAY OF STRINGS
    for Line in DataArray:
        SplitLine = Line.split(",")
        match SplitLine[1].strip():
            case "red": Red.append(SplitLine[0])
            case "green": Green.append(SplitLine[0])
            case "blue": Blue.append(SplitLine[0])
            case "orange": Orange.append(SplitLine[0])
            case "yellow": Yellow.append(SplitLine[0])
            case _: Pink.append(SplitLine[0])
    StoreData(Red, "Red.txt")
    StoreData(Green, "Green.txt")
    StoreData(Blue, "Blue.txt")
    StoreData(Orange, "Orange.txt")
    StoreData(Yellow, "Yellow.txt")
    StoreData(Pink, "Pink.txt")

DataFromFile = ReadData()
SplitData(DataFromFile)