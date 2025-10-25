def linearSearch(searchValue):
    for x in range(0, 10):
        if arrayData[x] == searchValue:
            return True
    return False

def bubbleSort():
    for x in range(0,len(arrayData)-1):
        for y in range(0, len(arrayData)-x-1):
            if arrayData[y] < arrayData[y+1]:
                temp = arrayData[y] #INTEGER
                arrayData[y] = arrayData[y+1]
                arrayData[y+1] = temp

arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8] #ARRAY OF INTEGER
searchValue = int(input("Enter the number to search for: ")) #INTEGER
returnValue = linearSearch(searchValue) #BOOLEAN
if returnValue:
    print("It was found")
else:
    print("It was not found")
bubbleSort()
print(arrayData)