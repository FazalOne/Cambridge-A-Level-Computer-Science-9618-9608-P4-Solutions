import random
class IslandClass:
    def __init__(self):
        self.SAND = "." #STRING
        self.TREASURE = "T" #STRING
        self.FOUND = "X" #STRING
        self.HOLE = "O" #STRING
        self.Grid = [[self.SAND for x in range(30)] for x in range(10)] #2D ARRAY OF STRING

    def GetSquare(self, Row, Column):
        return self.Grid[Row][Column]
    def HideTreasure(self):
        placed = False #BOOLEAN
        while not placed:
            Row = random.randint(0,9) #INTEGER
            Column = random.randint(0,29) #INTEGER
            if not self.GetSquare(Row, Column) == self.TREASURE:
                self.Grid[Row][Column] = self.TREASURE
                placed = True
    def DigHole(self, Row, Column):
        if self.GetSquare(Row, Column) == self.TREASURE:
            self.Grid[Row][Column] = self.FOUND
        if self.GetSquare(Row, Column) == self.SAND:
            self.Grid[Row][Column] = self.HOLE

def DisplayGrid():
    for Row in range(10):
        for Column in range(30):
            print(Island.GetSquare(Row, Column), end="")
        print()
def StartDig():
    valid = False #BOOLEAN
    while not valid:
        Row = int(input("Enter Row (0-9): ")) #INTEGER
        Column = int(input("Enter column (0-29)")) #INTEGER
        if 0 <= Row <= 9 and 0 <= Column <= 29:
            valid = True
            Island.DigHole(Row, Column)
        else:
            print("Sorry, invalid input. Please re-enter.")
    
#main
Island = IslandClass() #IslandClass
print("Game start!")
DisplayGrid()
for treasure in range(3):
    Island.HideTreasure()
print("Treasure is Hidden, Good luck!")
StartDig()
DisplayGrid()