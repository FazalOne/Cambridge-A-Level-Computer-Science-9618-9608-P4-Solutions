class Balloon:
    def __init__(self, DefItem, Colour):
        self.Health = 100 #INTEGER
        self.Colour = Colour #STRING
        self.DefenceItem = DefItem #STRING
    def GetDefenceItem(self):
        return self.DefenceItem
    def ChangeHealth(self, change):
        self.Health += change
    def CheckHealth(self):
        return self.Health <= 0

def Defend(balloon):
    Strength = int(input("Enter the opponent strength: ")) #INTEGER
    balloon.ChangeHealth(-Strength)
    print(balloon.GetDefenceItem())
    if balloon.CheckHealth():
        print("Your Balloon has been destroyed!")
    else:
        print("Your Balloon has sustained damage.")
    return balloon

DefItem = input("Enter the defence item: ") #STRING
Colour = input("Enter the color: ") #STRING
Balloon1 = Balloon(DefItem, Colour) #Balloon
Balloon1 = Defend(Balloon1)