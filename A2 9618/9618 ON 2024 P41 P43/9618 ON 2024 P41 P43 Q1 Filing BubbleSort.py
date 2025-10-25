def ReadData():
    DataArray = ["" for x in range(45)] #ARRAY OF STRING
    with open("Data.txt","r") as file:
        for x in range(len(DataArray)):
            DataArray[x] = file.readline().strip("\n")
    return DataArray

def FormatArray(DataArray):
    str1 = "" #STRING
    for x in range(len(DataArray)):
        str1 += DataArray[x] + " "
    return str1

def CompareStrings(str1, str2):
    if len(str1) < len(str2):
        min = len(str1) #INTEGER
    else:
        min = len(str2)
    for i in range(min):
        if str1[i] < str2[i]:
            return 1
        elif str1[i] > str2[i]:
            return 2
        
def Bubble(DataArray):
    for x in range(len(DataArray)-1):
        for y in range(len(DataArray)-1-x):
            if CompareStrings(DataArray[y],DataArray[y+1]) == 2:
                DataArray[y], DataArray[y+1] = DataArray[y+1], DataArray[y]
    return DataArray

Array = ReadData() #ARRAY OF STRING
Array = Bubble(Array) #ARRAY OF STRING
print(FormatArray(Array))