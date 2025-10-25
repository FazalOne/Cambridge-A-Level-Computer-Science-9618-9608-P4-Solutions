class GameElement:
    def __init__(self, PositionX, PositionY, Width, Height, ImageFilename):
        self.PositionX = PositionX #INTEGER
        self.PositionY = PositionY #INTEGER
        self.Width = Width #INTEGER
        self.Height = Height #INTEGER
        self.ImageFilename = ImageFilename #STRING

    def ReturnDetails(self):
        return "Position x: " + str(self.PositionX) + " Position y: " + str(self.PositionY) + " Width: " + str(self.Width) + " Height: " + str(self.Height) + " Image Filename: " + self.ImageFilename

class Scenery(GameElement):
    def __init__(self, PositionX, PositionY, Width, Height, ImageFilename, CauseDamage, DamagePoints):
        super().__init__(PositionX, PositionY, Width, Height, ImageFilename)
        self.CauseDamage = CauseDamage #BOOLEAN
        self.DamagePoints = DamagePoints #INTEGER

    def GiveDamagePoints(self):
        if self.CauseDamage == "True":
            return self.DamagePoints
        else:
            return 0

    def GetScenery(self):
        return super().ReturnDetails() + " Causes Damage: " + self.CauseDamage + " Damage Points: " + str(self.DamagePoints)

class AnimatedElement(GameElement):
    def __init__(self, PositionX, PositionY, Width, Height, ImageFilename, Health, Strength, Direction):
        super().__init__(PositionX, PositionY, Width, Height, ImageFilename)
        self.Health = Health #INTEGER
        self.Strength = Strength #INTEGER
        self.Direction = Direction #STRING
        self.AnimationFrames = [] #ARRAY OF GameElement

    def AdjustHealth(self,newHealth):
        self.Health += newHealth
    def AdjustStrength(self,newStrength):
        self.Strength += newStrength
    def DisplayAnimation(self):
        for x in self.AnimationFrames:
            print(x.ReturnDetails())

class Player(AnimatedElement):
    def __init__(self, PositionX, PositionY, Width, Height, ImageFilename, Health, Strength, Direction):
        super.__init__(PositionX, PositionY, Width, Height, ImageFilename, Health, Strength, Direction)
    def MoveLeft(self, distance):
        self.PositionX -= distance
    def MoveLeft(self, distance):
        self.PositionX += distance
    def JumpUp(self, distance):
        self.PositionY += distance

GiftBox = Scenery(150, 150, 50, 75, "box.png", "True", 50) #Scenery
print(GiftBox.GetScenery())