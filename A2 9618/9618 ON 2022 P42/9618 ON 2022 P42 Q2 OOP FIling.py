class Character:
    def __init__(self, Name, XCoord, YCoord):
        self.Name = Name #STRING
        self.XCoordinate = int(XCoord) #INTEGER
        self.YCoordinate = int(YCoord) #INTEGER
    def GetName(self):
        return self.Name
    def GetX(self):
        return self.XCoordinate
    def GetY(self):
        return self.YCoordinate
    def ChangePosition(self, XChange, YChange):
        self.XCoordinate += XChange
        self.YCoordinate += YChange

#variant 1, check other variants in the previous notebook file
try:
    with open("Characters.txt","r") as file:
        data = file.read().split() #ARRAY OF STRING
    CharArray = [Character(data[x*3],data[x*3+1],data[x*3+2]) for x in range(10)] #ARRAY OF Character
    found = False #BOOLEAN
    while not found:
        searchValue = input("Enter the name of character to find: ").lower() #STRING
        for x in range(10):
            if CharArray[x].GetName().lower() == searchValue:
                pos = x #INTEGER
                found = True
                break
        if not found:
            print("Character does not exist, please search again.")

    direction = "" #STRING
    while direction not in ["a","w","s","d"]:
        direction = input("Enter A,W,S,D for left, up, down, right: ").lower()
    match direction:
        case "a": CharArray[pos].ChangePosition(-1,0)
        case "w": CharArray[pos].ChangePosition(0,1)
        case "s": CharArray[pos].ChangePosition(0,-1)
        case "d": CharArray[pos].ChangePosition(1,0)
    print("{} has changed coordinates to X = {} and Y = {}".format(CharArray[pos].GetName(), CharArray[pos].GetX(), CharArray[pos].GetY()))
except (FileNotFoundError, IOError):
    print("FileNotFoundError: Sorry, an error occurred. Please check the filepath and try again.")