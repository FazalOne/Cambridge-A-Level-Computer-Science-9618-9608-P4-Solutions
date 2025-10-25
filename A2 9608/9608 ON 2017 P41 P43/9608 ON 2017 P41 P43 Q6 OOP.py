import random

class Animal :
    def __init__ (self) :
        self.Across = random.randint(0,39) #INTEGER
        self.Down = random.randint(0,39) #INTEGER
        self.Score = 0 #INTEGER
    def SetAcross(self,A) :
        self.Across = A
    def GetAcross(self) :
        return self.Across

    def Move(self) :
        self.Across = self.GenerateChangeInCoordinate(self.Across)
        self.Down = self.GenerateChangeInCoordinate(self.Down)
        if Sahara.grid[self.Across][self.Down] == "F":
            Sahara.grid[self.Across][self.Down] == ""
            self.EatFood()
        return
    def GenerateChangeInCoordinate(self,Coord):
        lowerBound = -1 #INTEGER
        upperBound = 1 #INTEGER
        if Coord == 0 :
            lowerBound = 0
        elif Coord == 39 :
            upperBound = 0
        return random.randint(lowerBound, upperBound)
    def EatFood(self):
        self.Score += 1
        Sahara.GenerateAnimals(1)
        Sahara.GenerateFood()

class Desert:
    def __init__ (self) :
        self.grid = [['' for i in range(40)] for j in range(40)] #2D ARRAY OF STRINGS
        self.AnimalList = [] #ARRAY OF ANIMALS
        self.StepCounter = 0 #INTEGER
        self.NoAnimals = 0 #INTEGER
        self.GenerateAnimals(5)
        self.GenerateFood()

    def GenerateAnimals(self,Num):
        for i in range(Num) :
            newAnimal =Animal()
            self.NoAnimals  += 1
            self.AnimalList.append(newAnimal)
    def GenerateFood(self):
        x = random.randint(0, 39)
        y = random.randint(0, 39)
        self.grid[x][y] = "F"
    def IncrementStepCounter(self):
        for i in range(self.NoAnimals) :
            self.AnimalList[i].Move()
        self.StepCounter += 1
        return
    def DisplayGrid(self):
        for i in range(40) :
            for j in range(40) :
                print(self.grid[i][j], end=" ")
            print()
        return

Sahara = Desert()
Sahara.DisplayGrid()
Sahara.IncrementStepCounter()
Sahara.DisplayGrid()