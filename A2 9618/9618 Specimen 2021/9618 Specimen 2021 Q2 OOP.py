class HiddenBox:
    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation): 
        self.BoxName = NewBoxName   #STRING
        self.Creator = NewCreator   #STRING
        self.DateHidden = NewDateHidden #DATE
        self.GameLocation = NewLocation #STRING
        self.LastFinds = [["" for i in range(0, 2)] for j in range(0, 10)] #2D ARRAY OF STRING
        self.Active = False #BOOLEAN
    
    def GetBoxName(self):
        return self.BoxName
    def GetLocation(self):
        return self.GameLocation

class PuzzleBox(HiddenBox): 
    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewLocation, NewPuzzleText, NewSolution): 
        super().__init__(NewBoxName, NewCreator, NewDateHidden, NewLocation) 
        self.PuzzleText = NewPuzzleText #STRING
        self.Solution = NewSolution #STRING

def NewBox(): 
    BoxName = input("Enter the name of the box: ") #STRING
    Creator = input("Enter the creator's name: ") #STRING
    DateHidden = input("Enter the date the box was hidden: ") #STRING
    GameLocation = input("Enter the location of the box: ") #STRING
    TheBoxes.append(HiddenBox(BoxName, Creator, DateHidden, GameLocation))

TheBoxes = [HiddenBox("","","","") for i in range(0, 10000)] #ARRAY OF HiddenBoxes
NewBox()