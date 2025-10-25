MyList = [3,5,8,9,13,16,27,0,0,0] #ARRAY OF INTEGER
def X(Index, Item):
    if MyList[Index] > 0:
        if MyList[Index] >= Item:
            MyList[Index] = MyList[Index + 1]
        X(Index + 1, Item)
print(MyList)
X(0,9)
print(MyList)