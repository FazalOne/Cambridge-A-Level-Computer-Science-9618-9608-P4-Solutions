class EventItem:
    def __init__(self, name, event, difficulty):
        self.EventName = name #STRING
        self.Type = event #STRING
        self.Difficulty = difficulty #INTEGER
    
    def GetName(self):
        return self.EventName
    def GetEventType(self):
        return self.Type
    def GetDifficulty(self):
        return self.Difficulty
    
class Character:
    def __init__(self, CName, JSkill, SSkill, RSkill, DSkill):
        self.CharacterName = CName #STRING
        self.Jump = JSkill #INTEGER
        self.Swim = SSkill #INTEGER
        self.Run = RSkill #INTEGER
        self.Drive = DSkill #INTEGER

    def GetName(self):
        return self.CharacterName
    def CalculateScore(self, event, difficulty):
        difference = 0 #INTEGER
        match event:
            case "jump":
                difference = difficulty - self.Jump
            case "swim":
                difference = difficulty - self.Swim
            case "run":
                difference = difficulty - self.Run
            case "drive":
                difference = difficulty - self.Drive

        match difference:
            case 1: return 80
            case 2: return 60
            case 3: return 40
            case 4: return 20
            case _ if difference <= 0: return 100

Group = [EventItem("Bridge","jump",3),
         EventItem("Water wade","swim",4),
         EventItem("100 mile run","run",5),
         EventItem("Gridlock","drive",2),
         EventItem("Wall on wall","jump",4)] #ARRAY OF EventItems

Tarz = Character("Tarz",5,3,5,1) #Character
Geni = Character("Geni",2,2,3,4) #Character

TarzScore = 0 #INTEGER
GeniScore = 0 #INTEGER
for x in range(5):
    TarzChance = Tarz.CalculateScore(Group[x].GetEventType(),Group[x].GetDifficulty())
    GeniChance = Geni.CalculateScore(Group[x].GetEventType(),Group[x].GetDifficulty())
    if TarzChance == GeniChance:
        print(Group[x].GetEventType(), "is a draw!")
    elif TarzChance > GeniChance:
        TarzScore += 1
        print(Group[x].GetEventType(), "is won by Tarz!")
    else:
        GeniScore += 1
        print(Group[x].GetEventType(), "is won by Geni!")
if TarzScore > GeniScore:
    print("Tarz wins the group with a score of", TarzScore)
elif GeniScore > TarzScore:
    print("Geni wins the group with a score of", GeniScore)
else:
    print("The group is a draw with both players scoring", TarzScore)