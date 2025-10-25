def insert(data):
    global FreeNode
    if FreeNode == 0:
        ArrayNodes.append([-1,data,-1])
    else:
        Placed = False
        CurrentNode = 0 #INTEGER
        ArrayNodes.append([-1,data,-1])
        while Placed == False:
            if data < ArrayNodes[CurrentNode][1]:
                if ArrayNodes[CurrentNode][0] == -1:
                    ArrayNodes[CurrentNode][0] = FreeNode
                    Placed = True
                else:
                    CurrentNode = ArrayNodes[CurrentNode][0]
            else:
                if ArrayNodes[CurrentNode][2] == -1:
                    ArrayNodes[CurrentNode][2] = FreeNode
                    Placed = True
                else:
                    CurrentNode = ArrayNodes[CurrentNode][2]
    FreeNode += 1

def InOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][0])
    print("CurrentPointer: {} | LeftPointer: {} | Data: {} | RightPointer: {}".format(RootNode,ArrayNodes[RootNode][0],ArrayNodes[RootNode][1],ArrayNodes[RootNode][2]))
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootNode][2])

def PreOrder(ArrayNodes, RootNode):
    print("CurrentPointer: {} | LeftPointer: {} | Data: {} | RightPointer: {}".format(RootNode,ArrayNodes[RootNode][0],ArrayNodes[RootNode][1],ArrayNodes[RootNode][2]))
    if ArrayNodes[RootNode][0] != -1:
        PreOrder(ArrayNodes, ArrayNodes[RootNode][0])
    if ArrayNodes[RootNode][2] != -1:
        PreOrder(ArrayNodes, ArrayNodes[RootNode][2])

def PostOrder(ArrayNodes, RootNode):
    if ArrayNodes[RootNode][0] != -1:
        PostOrder(ArrayNodes, ArrayNodes[RootNode][0])
    if ArrayNodes[RootNode][2] != -1:
        PostOrder(ArrayNodes, ArrayNodes[RootNode][2])
    print("CurrentPointer: {} | LeftPointer: {} | Data: {} | RightPointer: {}".format(RootNode,ArrayNodes[RootNode][0],ArrayNodes[RootNode][1],ArrayNodes[RootNode][2]))

def Search(RootNode,data):
    if ArrayNodes[RootNode][1] == data:
        print("CurrentPointer: {} | LeftPointer: {} | Data: {} | RightPointer: {}".format(RootNode,ArrayNodes[RootNode][0],ArrayNodes[RootNode][1],ArrayNodes[RootNode][2]))
    elif ArrayNodes[RootNode][1] > data and ArrayNodes[RootNode][0] != -1:
        Search(ArrayNodes[RootNode][0],data)
    elif ArrayNodes[RootNode][2] != -1:
        Search(ArrayNodes[RootNode][2],data)
    else:
        print("Sorry, data does not exist")

ArrayNodes=[] #2D LIST OF INTEGERS AND STRINGS
RootNode = 0 #INTEGER
FreeNode = 0 #INTEGER

insert('M')
insert('C')
insert('A')
insert('G')
insert('R')
insert('L')
insert('W')
insert('J')
insert('D')
insert('P')
insert('H')

print("InOrder\n")
InOrder(ArrayNodes,0)
print("\nPreOrder\n")
PreOrder(ArrayNodes,0)
print("\nPostOrder\n")
PostOrder(ArrayNodes,0)