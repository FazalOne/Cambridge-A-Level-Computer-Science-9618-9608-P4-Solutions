import random
class Character:
    def __init__(self, CharName):
        self.Name = CharName #STRING
        self.Skill = 0 #INTEGER
        self.Health = 50 #INTEGER
        self.Shield = random.randint(1,25) #INTEGER

    def GetName(self):
        return self.Name
    def GetSkill(self):
        return self.Skill
    def GetHealth(self):
        return self.Health
    def GetShield(self):
        return self.Shield
    
    def SetSkill(self, newSkill):
        if 10 <= newSkill <= 25:
            self.Skill += newSkill
            if self.Skill >= 200:
                self.Skill = 200
                return 0
            return 1
        return -1
    def SetHealth(self, newHealth):
        self.Health += newHealth
    def SetShield(self, newShield):
        self.Shield += newShield
            
CharacterArray = [Character("") for x in range(5)] #ARRAY OF Character
CharacterArray[0] = Character("Victory")
print("Character name:", CharacterArray[0].GetName(), "Skill:", CharacterArray[0].GetSkill(), "Health:", CharacterArray[0].GetHealth(), "Shield:", CharacterArray[0].GetShield())