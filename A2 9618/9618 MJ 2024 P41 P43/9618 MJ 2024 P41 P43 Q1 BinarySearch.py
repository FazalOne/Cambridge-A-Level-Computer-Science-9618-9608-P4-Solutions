def Initialize():
    global DataStored, NumberItems
    items = 0 #INTEGER
    while items < 1 or items > 20:
        items = int(input("Enter the number of items to be stored (1-20): "))
    for x in range(items): #INTEGER
        DataStored[x] = int(input("Enter a number: "))
    NumberItems = items 

def BubbleSort():
    global DataStored, NumberItems
    length = NumberItems - 1 #INTEGER
    for passes in range(length): #INTEGER
        for compares in range(length - passes): #INTEGER
            if DataStored[compares] > DataStored[compares + 1]:
                temp = DataStored[compares] #INTEGER
                DataStored[compares] = DataStored[compares + 1]
                DataStored[compares + 1] = temp

def BinarySearch(DataToFind):
    global NumberItems
    l = 0   #INTEGER
    u = NumberItems-1   #INTEGER
    while l <= u:
        mid = (l+u) // 2    #INTEGER
        if DataStored[mid] == DataToFind:
            return mid
        if DataStored[mid] < DataToFind:
            l = mid+1
        else:
            u = mid-1
    return -1

DataStored = [0 for x in range(20)] #ARRAY OF INTEGER
NumberItems = 0 #INTEGER
Initialize()
BubbleSort()
print(DataStored)
Search = int(input("Enter a number to find: ")) #INTEGER
if Search == -1:
    print("Value not found")
else:
    print("Value found at index ",BinarySearch(Search))