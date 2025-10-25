class Player:
    def __init__(self):
        self.Score = 0 # INTEGER
        self.Category = "" # STRING
        self.SetPlayerID()
    
    def GetScore(self):
        return self.Score
    def GetCategory(self):
        return self.Category
    def GetPlayerID(self):
        return self.PlayerID
    
    def SetPlayerID(self):
        self.PlayerID = input("Enter Player ID:") #STRING
        while not 4 <= len(self.PlayerID) <= 15:
            self.PlayerID = input("Invalid Player ID, please enter between 4 and 15 characters:")
    def SetScore(self, ScoreInput):
        if 0 <= ScoreInput <= 150:
            self.Score = ScoreInput
            return True
        print("Sorry, the score is not valid.")
        return False
    def SetCategory(self):
        if self.Score > 120:
            self.Category = "Advanced"
        elif 80 < self.Score <= 120:
            self.Category = "Intermediate"
        elif 50 <= self.Score <= 80:
            self.Category = "Beginner"
        else:
            self.Category = "Not Qualified"

def CreatePlayer():
    JoannePlayer = Player() #Player
    while not JoannePlayer.SetScore(int(input("Enter a valid player score between 0 and 150: "))):
        pass
    JoannePlayer.SetCategory()
    print(JoannePlayer.GetCategory())
CreatePlayer()