import datetime
class Character:
    def __init__(self, CName, DOB, Intel, CSpeed):
        self.CharacterName = CName #STRING
        self.DateOfBirth = DOB #DATETIME
        self.Intelligence = Intel #REAL
        self.Speed = CSpeed #INTEGER
    def GetIntelligence(self):
        return self.Intelligence
    def GetName(self):
        return self.CharacterName
    def SetIntelligence(self,NewIntel):
        self.Intelligence = NewIntel
    def Learn(self):
        self.Intelligence *= 1.1
    def ReturnAge(self):
        return 2023 - self.DateOfBirth.year
    
class MagicCharacter(Character):
    def __init__(self, CName, DOB, Intel, CSpeed, CElement):
        super().__init__(CName, DOB, Intel,CSpeed)
        self.Element = CElement #STRING
    def Learn(self):
        if self.Element in ["fire", "water"]:
            increase = 1.2 #REAL
        elif self.Element == "earth":
            increase = 1.3
        else:
            increase = 1.1
        self.SetIntelligence(self.GetIntelligence() * increase)

FirstCharacter = Character("Royal", datetime.datetime(2019,1,1), 70, 30) #Character
FirstCharacter.Learn()
print(FirstCharacter.GetName(), "is ", FirstCharacter.ReturnAge(), "years old and has intelligence ", FirstCharacter.GetIntelligence())
FirstMagic = MagicCharacter("Light", datetime.datetime(2018,3, 3), 75, 22, "fire") #MagicCharacter
FirstMagic.Learn()
print(FirstMagic.GetName(), "is ", FirstMagic.ReturnAge(), "years old and has intelligence ", FirstMagic.GetIntelligence())