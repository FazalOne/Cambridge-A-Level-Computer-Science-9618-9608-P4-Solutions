Board = [["" for j in range(8)] for i in range(8)] #ARRAY OF STRING
for Row in range(0, 2) : 
    for Column in range(8) : 
        Board[Row][Column] = "B" 
for Row in range(2, 7) : 
    for Column in range(8) : 
        Board[Row][Column] = "E" 
for Row in range(6, 8) : 
    for Column in range(8) : 
        Board[Row][Column] = "W" 

def ValidMoves(PieceColour, xCurrentP, yCurrentP) : 
    if PieceColour == "B" : 
        StopperColour = "W" #STRING
    else : 
        StopperColour = "B" 
        print("Possible moves are : ") 
    if 0 <= xCurrentP <= 7 and 0 <= yCurrentP <= 7: 
        print("LEFT . . .") 
        x = xCurrentP #INTEGER
        y = yCurrentP #INTEGER
        NoFurther = False #BOOLEAN
        while y > 0 and NoFurther == False : 
            y -= 1
            if Board[x][y] == "E" :
                print(str(x) + " " + str(y) + " EMPTY ") 
            elif Board[x][y] == PieceColour:
                NoFurther = True
            elif Board[x][y] == StopperColour : 
                print(str(x) + " " + str(y) + " REMOVE PIECE") 
                NoFurther = True
             
        print("RIGHT. . .") 
        x = xCurrentP
        y = yCurrentP
        NoFurther = False 
        while y < 7 and NoFurther == False :
            y +=  1 
            if Board[x][y] == "E" :
                print(str(x) + " " + str(y) + " EMPTY ") 
            elif Board[x][y] == PieceColour:
                NoFurther = True
            elif Board[x][y] == StopperColour : 
                print(str(x) + " " + str(y) + " REMOVE PIECE") 
                NoFurther = True

        print("UP. . .") 
        x = xCurrentP
        y = yCurrentP
        NoFurther = False 
        while x > 0 and NoFurther == False : 
            x -= 1
            if Board[x][y] == "E" :
                print(str(x) + " " + str(y) + " EMPTY ") 
            elif Board[x][y] == PieceColour:
                NoFurther = True
            elif Board[x][y] == StopperColour : 
                print(str(x) + " " + str(y) + " REMOVE PIECE") 
                NoFurther = True
             
        print("DOWN. . .") 
        x = xCurrentP
        y = yCurrentP
        NoFurther = False 
        while x < 7 and NoFurther == False :
            x += 1 
            if Board[x][y] == "E" :
                print(str(x) + " " + str(y) + " EMPTY ") 
            elif Board[x][y] == PieceColour:
                NoFurther = True
            elif Board[x][y] == StopperColour : 
                print(str(x) + " " + str(y) + " REMOVE PIECE") 
                NoFurther = True

ValidMoves("B",2,2) #row column
print(Board)