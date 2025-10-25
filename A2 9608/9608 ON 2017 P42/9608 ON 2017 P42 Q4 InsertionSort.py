Numbers = [54,26,93,17,77,31,44,55,20] #ARRAY OF INTEGERS
for Pointer in range (1,len(Numbers)):
    ItemToInsert = Numbers[Pointer] #INTEGER
    CurrentItem = Pointer #INTEGER
    while (CurrentItem > 0) and (Numbers[CurrentItem - 1] > ItemToInsert):
        Numbers[CurrentItem] = Numbers[CurrentItem - 1]
        CurrentItem = CurrentItem - 1
    Numbers[CurrentItem] = ItemToInsert
print(Numbers)