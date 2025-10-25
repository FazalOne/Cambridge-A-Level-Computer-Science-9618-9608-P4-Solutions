def BubbleSort(ItemList):
    MaxIndex = len(ItemList) #INTEGER
    NumberItems = MaxIndex - 1 #INTEGER
    for Outer in range(MaxIndex - 1): #INTEGER
        for Inner in range(NumberItems): #INTEGER
            if ItemList[Inner] > ItemList[Inner+1]:
                Temp = ItemList[Inner]
                ItemList[Inner] = ItemList[Inner+1]
                ItemList[Inner + 1] = Temp
        NumberItems = NumberItems - 1
    return ItemList

ItemList= [5,11,4,2,10,9,10,1,43,4,9,12,15,36,29,69,42,99,76,82,56] #ARRAY OF INTEGER
print(ItemList)
ItemList = BubbleSort(ItemList)
print(ItemList)