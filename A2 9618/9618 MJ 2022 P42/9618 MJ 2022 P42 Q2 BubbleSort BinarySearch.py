import random
def printArray(ArrayData):
    for x in range(0, len(ArrayData)):
        for y in range(0, len(ArrayData)):
            print(ArrayData[x][y], " ", end='')
        print("")

def BinarySearch(SearchArray, Lower, Upper, SearchValue):
    if Lower < Upper:
        Mid = int((Lower + Upper) / 2) #INTEGER
        if SearchArray[0][Mid] == SearchValue:
            return Mid
        elif SearchArray[0][Mid] > SearchValue:
            return BinarySearch(SearchArray, Lower, Mid-1, SearchValue)
        else:
            return BinarySearch(SearchArray, Mid+1, Upper, SearchValue)
    else:
        return -1

ArrayData= [[random.randint(1, 100) for x in range(10)] for y in range(10)] #2D ARRAY OF INTEGER 
print("Before")
printArray(ArrayData)

for X in range(0, len(ArrayData)): #No of arrays inside ArrayData
    for Y in range(0, len(ArrayData)- 1): #bubblesort each array
        for Z in range(0, len(ArrayData) - Y - 1):
            if(ArrayData[X][Z] > ArrayData[X][Z+1]):
                TempNumber = ArrayData[X][Z] #INTEGER
                ArrayData[X][Z] = ArrayData[X][Z+1]
                ArrayData[X][Z+1] = TempNumber

print("After")
printArray(ArrayData)
SearchValue = int(input("Enter value which is in first line of array: ")) #INTEGER
print(BinarySearch(ArrayData,0,10,SearchValue))
SearchValue = int(input("Enter value which is not in first line of array: ")) #INTEGER
print(BinarySearch(ArrayData,0,10,SearchValue))