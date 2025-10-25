DataArray = [0 for i in range (100)] #ARRAY OF INTEGERS
def ReadFile():
    global DataArray
    try:
        with open("IntegerData.txt", 'r') as File:
            for X in range(0, 100):
                DataArray[X] = int(File.readline().strip('\n'))
    except FileNotFoundError:
        print("Could not find file")

def FindValues():
    global DataArray
    DataToFind = -1 #INTEGER
    while DataToFind < 1 or DataToFind > 100:
        DataToFind = int(input("Enter a number between 1 and 100"))
    Total = 0 #INTEGER
    for X in range(0, 99):
        if DataArray[X] == DataToFind:
            Total += 1
    return Total

def BubbleSort():
    global DataArray
    N = 100 #INTEGER
    for I in range(N-1):
        for J in range(0, N-I-1):
            if DataArray[J] > DataArray[J+1]:
                DataArray[J], DataArray[J+1] = DataArray[J+1], DataArray[J]

ReadFile()
print("The number appears " + str(FindValues()) + " times")
BubbleSort()
print(DataArray)
ReadFile()
print("The number appears " + str(FindValues()) + " times")