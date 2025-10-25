def SearchValue(Root, ValueToFind):
    if Root == -1:
        return -1
    else:
        if ArrayNodes[Root][1] == ValueToFind:
            return Root
        elif ArrayNodes[Root][1] == -1:
            return -1
    if ArrayNodes[Root][1] > ValueToFind:
        return SearchValue(ArrayNodes[Root][0], ValueToFind)
    if ArrayNodes[Root][1] < ValueToFind:
        return SearchValue(ArrayNodes[Root][2], ValueToFind)
    
def PostOrder(Root):
    if ArrayNodes[Root][0] != -1:
        PostOrder(ArrayNodes[Root][0])
    if ArrayNodes[Root][2] != -1:
        PostOrder(ArrayNodes[Root][2])
    print(ArrayNodes[Root][1])

ArrayNodes = [[-1 for x in range(3)] for x in range(20)] #2D ARRAY OF INTEGER
ArrayNodes[0] = [1,20,5]
ArrayNodes[1] = [2,15,-1]
ArrayNodes[2] = [-1,3,3]
ArrayNodes[3] = [-1,9,4]
ArrayNodes[4] = [-1,10,-1]
ArrayNodes[5] = [-1,58,-1]
ArrayNodes[6] = [-1,-1,-1]
FreeNode = 6 #INTEGER
RootPointer = 0 #INTEGER

if SearchValue(RootPointer, 15) == -1:
    print("Value not found!")
else:
    print(SearchValue(RootPointer, 15))
PostOrder(RootPointer)