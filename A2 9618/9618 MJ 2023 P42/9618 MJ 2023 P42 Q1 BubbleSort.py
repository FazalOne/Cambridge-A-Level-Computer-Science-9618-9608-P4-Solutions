Animals = [] #ARRAY OF STRINGS
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

def SortDescending():
    ArrayLength = 10 #INTEGER
    for X in range(0, ArrayLength-1):
        for Y in range(0, ArrayLength-X-1):
            if Animals[Y][0] < Animals[Y+1][0]:
                Temp = Animals[Y] #STRING
                Animals[Y] = Animals[Y + 1]
                Animals[Y + 1] = Temp

SortDescending()
for X in range(0, 10):
    print(Animals[X])