DataArray = [0 for x in range(25)] #ARRAY OF INTEGERS
with open("Data.txt","r") as file:
    count = 0 #INTEGER
    data = file.readline().strip("\n") #STRING
    while data != "":
        DataArray[count] = int(data)
        count += 1
        data = file.readline().strip("\n")

def PrintArray(data):
    for number in data:
        print(number, end=" ")
    print()

def LinearSearch(data, searchValue):
    count = 0 #INTEGER
    for number in data:
        if number == searchValue:
            count += 1
    return count

PrintArray(DataArray)
searchValue = -1 #INTEGER
while searchValue < 0 or searchValue > 100:
    searchValue = int(input("Please enter the value to search between 0 and 100: "))
result = LinearSearch(DataArray, searchValue) #INTEGER
print(f"The number {searchValue} is found {result} times.")