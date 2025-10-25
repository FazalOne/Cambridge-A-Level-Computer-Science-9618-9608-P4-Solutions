import random
def InsertionSort():
    global TheArray
    count = 0 #INTEGER
    while count < 10:
        temp = TheArray[count]
        counter = count - 1 #INTEGER
        while counter >= 0 and TheArray[counter] > temp:
            TheArray[counter + 1] = TheArray[counter]
            counter -= 1
        TheArray[counter + 1] = temp
        count += 1

TheArray = [random.randint(1, 100) for _ in range(10)] #ARRAY OF INTEGERS
print(TheArray)
InsertionSort()
print(TheArray)