CardData = [13, 12, 25, 33, 52, 56, 57, 59, 91, 85] #ARRAY OF INTEGERS
print(CardData)
for Pointer in range (1,len(CardData)):
    ValueToInsert = CardData[Pointer] #INTEGER
    HolePosition = Pointer #INTEGER
    while HolePosition > 1 and CardData[HolePosition-1] > ValueToInsert:
        CardData[HolePosition] = CardData[HolePosition-1]
        HolePosition -= 1
    CardData[HolePosition] = ValueToInsert
print(CardData)
print()
CardData = [11, 12, 25, 33, 52, 56, 57, 59, 85, 91] #ARRAY OF INTEGERS
print(CardData)
SearchValue = int(input("Enter value to search: "))
First =  1 #INTEGER
Last = len(CardData) #INTEGER
Found = False #BOOLEAN
while First <= Last and not Found:
    Midpoint = (First+Last) // 2 #INTEGER
    if CardData[Midpoint] == SearchValue:
        Found = True
        print("Value found at ", Midpoint)
    elif SearchValue < CardData[Midpoint]:
        Last = Midpoint - 1
    else:
        First = Midpoint + 1