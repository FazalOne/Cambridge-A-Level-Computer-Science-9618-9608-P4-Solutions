class PuzzlePlayer:
    def __init__(self):
        self.PID="PL12a3" #STRING
        self.Name="" #STRING
        self.Score=0 #INTEGER
    
    def GetPlayerID(self):
        return self.PID
    def GetName(self):
        return self.Name
    def GetScore(self):
        return self.Score

    def SetName(self,NewName):
        self.Name = NewName
    def SetScore(self,NewScore):
        self.Score = NewScore
    def SetPlayerID(self,NewPID):
        if len(NewPID) == 6 and NewPID[0:2] == "PL":
            self.PID = NewPID
            return True
        return False

class Quiz:
    def __init__(self, QName, Diff, NoQs):
        self.QuizName = QName #STRING
        self.Difficulty = Diff #STRING
        self.QuizQs = ["" for x in range(NoQs)] #ARRAY OF Questions

class Question(Quiz):
    def __init__(self, QName, Question, NoQs, Diff, Ans):
        super.__init__(QName, Diff, NoQs)
        self.Question = Question #STRING
        self.Answer = Ans #STRING

QuizBank = ["" for x in range(100)] #ARRAY OF Quizzes
QuizBank[0] = Quiz("Famous people", "Low", 10)