NameList = [9, 5, 1, 4, 3, 7, 9, 11, 0, 8] #ARRAY OF INTEGER
for ThisPointer in range(1,10):
    Temp = NameList[ThisPointer] #INTEGER
    Pointer = ThisPointer - 1 #INTEGER
    while (NameList[Pointer] > Temp) and Pointer >= 0:
        NameList[Pointer+1] = NameList[Pointer]
        Pointer -= 1
    NameList[Pointer+1] = Temp
print(NameList)