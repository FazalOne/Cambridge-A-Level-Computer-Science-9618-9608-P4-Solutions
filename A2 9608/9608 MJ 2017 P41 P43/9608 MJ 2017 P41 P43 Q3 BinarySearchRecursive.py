def Find(NameList, Name, Start, Finish):
    if Finish >= Start:
        Middle = (Start + Finish) // 2 #INTEGER
        if NameList[Middle] == Name:
            return Middle
        elif NameList[Middle] > Name:
            return Find(List,Name, Start, Middle - 1)            
        else:
            return Find(List,Name, Middle + 1, Finish)
    else:
        return -1


List = ["Angela" , "Imran" , "James" , "Jason", "Mayu"] #ARRAY OF STRINGS
result = Find(List,"James",0,4) #INTEGER
print("Position is: ", result)