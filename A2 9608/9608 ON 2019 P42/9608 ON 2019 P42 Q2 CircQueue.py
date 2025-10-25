def CreateCircularQueue(size):
    return [None for x in range(size)], 0, 0, 0, size 

def IsEmpty():
    global StartPointer, EndPointer
    return StartPointer == EndPointer

def IsFull():
    global StartPointer, EndPointer, size
    return (EndPointer + 1) % size == StartPointer

def enqueue(NumberQueue, StartPointer, EndPointer, size, PrintJob):
    if IsFull():
        return "Queue is full"
    else:
        NumberQueue[EndPointer] = PrintJob
        NumberQueue = (EndPointer + 1) % size
        return StartPointer, EndPointer

def remove(NumberQueue):
    global StartPointer, EndPointer, size
    if IsEmpty():
        return "Empty"
    else:
        PrintJob = NumberQueue[StartPointer]
        NumberQueue[StartPointer] = None
        StartPointer = (StartPointer + 1) % size
        return PrintJob, StartPointer, EndPointer

def AddToQueue(Number):
    global StartPointer, EndPointer, CurrentPointer
    FirstIndex = 0 #INTEGER
    LastIndex = 7 #INTEGER
    if CurrentPointer > LastIndex:
        CurrentPointer = FirstIndex
    if IsFull():
        return False
    else:
        EndPointer = CurrentPointer
        NumberQueue[EndPointer] = Number
        CurrentPointer = EndPointer + 1
        return True

NumberQueue, StartPointer, EndPointer, CurrentPointer, size = CreateCircularQueue(8)

print(IsEmpty())  # True

AddToQueue("Print Job 1")
print(IsEmpty())  # False

AddToQueue("Print Job 2")
AddToQueue("Print Job 3")

print(remove(NumberQueue))  # ('Print Job 1', 1, 3)
print(NumberQueue)