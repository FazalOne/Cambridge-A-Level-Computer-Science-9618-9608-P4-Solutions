def setUpStack(Array, pointer):
    global topOfStack, stackArray
    stackArray = [-1 for x in range(1000)] #ARRAY OF INTEGERS
    topOfStack = pointer #INTEGER

def push(stackArray, data):
    global topOfStack
    if topOfStack >= 999:
        return False
    else:
        topOfStack += 1
        stackArray[topOfStack] = data
        return True

def pop(stackArray):
    global topOfStack
    if topOfStack < 0:
        return -1
    else:
        dataToReturn = stackArray[topOfStack] #INTEGER
        topOfStack -= 1
        return dataToReturn

stackArray = [] #ARRAY OF INTEGERS
setUpStack(stackArray, -1)
push(stackArray,10)
push(stackArray,20)
push(stackArray,30)
print(pop(stackArray))
print(pop(stackArray))
print(pop(stackArray))
print(pop(stackArray))