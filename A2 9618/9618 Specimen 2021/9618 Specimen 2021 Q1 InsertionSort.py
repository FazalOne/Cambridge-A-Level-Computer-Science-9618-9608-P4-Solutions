def InsertionSort(TheData):
    for Count in range(1, len(TheData)):
        DataToInsert = TheData[Count] #INTEGER
        NextValue  = Count - 1 #INTEGER
        while(NextValue  >= 0 and DataToInsert < TheData[NextValue ]):
            TheData[NextValue +1] = TheData[NextValue]
            NextValue  = NextValue -1
        TheData[NextValue +1] = DataToInsert
    return TheData    
        
def PrintArray(Array):
    for x in range(len(Array)):
        print(Array[x], end= " ")
    print()

def Search(Array):
    NumberInput = int(input("Enter a whole number: ")) #INTEGER
    for x in range(0, len(Array)):
        if(Array[x] == NumberInput):
            print("Found")
            return True
    print("Not found")
    return False                                

TheData = [20, 3, 4, 8, 12, 99, 4, 26, 4] #ARRAY OF INTEGER
print("Before")
PrintArray(TheData)
TheData = InsertionSort(TheData)
print("After")
PrintArray(TheData)
Search(TheData)