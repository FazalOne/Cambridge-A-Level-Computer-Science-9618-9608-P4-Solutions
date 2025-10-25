def Enqueue(data):
    global HeadPointer, TailPointer
    if TailPointer < 100:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = data   
        TailPointer += 1
        return True
    return False

def Dequeue():
    global HeadPointer, TailPointer
    if TailPointer < 0:
        return False
    else:
        TailPointer -= 1
        return True

def RecursiveOutput(Start):
    if Start == 0:
        return Queue[Start]
    else:
        return Queue[Start] + RecursiveOutput(Start-1)

Queue = [-1 for i in range(100)] #ARRAY OF INTEGER
HeadPointer = -1 #INTEGER
TailPointer = 0 #INTEGER
Success = False #BOOLEAN
for count in range(1,21):
    Success = Enqueue(count)
if Success:
    print("Succesful")
else:
    print("Unsuccesful")
print(str(RecursiveOutput(TailPointer-1)))