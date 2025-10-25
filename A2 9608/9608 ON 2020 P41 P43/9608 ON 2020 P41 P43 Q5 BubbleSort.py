DataList = [125, 64, 32, 96, 120, 1] #ARRAY OF INTEGERS
def BubbleSort(DataList):
    for X in range (0, len(DataList)-1):
        for y in range (0, (len(DataList)-X-1)):
            if DataList[y]> DataList[y+1]:
                temp = DataList[y] #INTEGER
                DataList[y]= DataList[y+1]
                DataList[y+1]= temp
    for x in DataList:
        print(x)
BubbleSort(DataList)