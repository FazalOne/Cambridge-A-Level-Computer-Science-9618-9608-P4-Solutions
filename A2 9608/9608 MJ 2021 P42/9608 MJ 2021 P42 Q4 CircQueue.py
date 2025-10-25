MyNumbers = [0 for x in range(10)] #ARRAY OF INTEGERS
NumberInQueue = 0 #INTEGER
HeadIndex = 0 #INTEGER
TailIndex = 0 #INTEGER

def enqueue(DataToInsert):
    global NumberInQueue, TailIndex, MyNumbers
    if NumberInQueue > 9:
        return False
    else:
        MyNumbers[TailIndex] = DataToInsert
        TailIndex = (TailIndex + 1) % 10
        NumberInQueue += 1
        return True

def dequeue():
    global NumberInQueue, HeadIndex, MyNumbers
    if NumberInQueue == 0:
        return -1
    else:
        item_to_return = MyNumbers[HeadIndex]
        HeadIndex = (HeadIndex + 1) % 10
        NumberInQueue -= 1
        return item_to_return

enqueue(1)
enqueue(2)
print(dequeue())
print(dequeue())
enqueue(31)
enqueue(45)
enqueue(89)
enqueue(500)
enqueue(23)
enqueue(2)
enqueue(23)
enqueue(100)
print(dequeue())
print(dequeue())
enqueue(50)