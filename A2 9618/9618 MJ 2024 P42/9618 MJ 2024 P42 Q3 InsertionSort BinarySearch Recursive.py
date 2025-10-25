def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    RecursiveInsertion(IntegerArray,NumberElements - 1)
    LastItem = IntegerArray[NumberElements - 1] #INTEGER
    CheckItem = NumberElements - 2 #INTEGER
    LoopAgain = True #BOOLEAN
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] <= LastItem:
        LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem - 1
    if CheckItem < 0:
        LoopAgain = False
    elif IntegerArray[CheckItem] <= LastItem:
        LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

def IterativeInsertion(IntegerArray, NumberElements):
    while NumberElements > 0:
        LastItem = IntegerArray[NumberElements - 1] #INTEGER
        CheckItem = NumberElements - 2 #INTEGER
        LoopAgain = True #BOOLEAN
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] <= LastItem:
            LoopAgain = False
        while LoopAgain:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem = CheckItem - 1
        if CheckItem < 0:
            LoopAgain = False
        elif IntegerArray[CheckItem] <= LastItem:
            LoopAgain = False
        IntegerArray[CheckItem + 1] = LastItem
        NumberElements -= 1
    return IntegerArray

def BinarySearch(IntegerArray, First, Last, ToFind):
    if First > Last:
        return -1
    else:
        Middle = (Last + First) // 2 #INTEGER
        if IntegerArray[Middle] == ToFind:
            return Middle
        elif IntegerArray[Middle] > ToFind:
            return BinarySearch(IntegerArray, First, Middle - 1, ToFind)
        else:
            return BinarySearch(IntegerArray, Middle + 1, Last, ToFind)

NumberArray = [100, 85, 644, 22, 15, 8, 1] #ARRAY OF INTEGER
SortedArray = RecursiveInsertion(NumberArray, len(NumberArray)) #ARRAY OF INTEGER
print("Recursive", SortedArray)
Sorted2Array = IterativeInsertion(NumberArray, len(NumberArray)) #ARRAY OF INTEGER
print("iterative", Sorted2Array)
Position = BinarySearch(Sorted2Array, 0, len(NumberArray)-1, 644) #INTEGER
if Position == -1:
    print("Not found")
else:
    print(Position)