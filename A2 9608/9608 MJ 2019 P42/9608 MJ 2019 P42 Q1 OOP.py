class ExaminationPaper:
    def __init__(self, center, candidate):
        self.FinalMark = 0 #INTEGER
        self.Grade = "Fail" #STRING
        self.PaperID = str(center) + str(candidate) #STRING

    def GetFinalMark(self):
        return self.FinalMark
    def GetGrade(self):
        return self.Grade
    def GetPaperID(self):
        return self.PaperID
    
    def SetFinalMark(self, Mark):
        if 0 <= Mark <= 90:
            self.FinalMark = Mark
            return True
        return False
    def SetGrade(self, DistMark, MeritMark, PassMark):
        if self.FinalMark >= DistMark:
            self.Grade = "Distinction"
        elif self.FinalMark >= MeritMark:
            self.Grade = "Merit"
        elif self.FinalMark >= PassMark:
            self.Grade = "Pass"
        else:
            self.Grade = "Fail"

def Main():
    Center = input("Enter center number: ") #STRING
    Candidate = input("Enter candidate number: ") #STRING
    ThisPaper = ExaminationPaper(Center, Candidate)
    while not ThisPaper.SetFinalMark(int(input("Please enter marks (0-90): "))):
        pass
    ThisPaper.SetGrade(80, 75, 55)
    print(ThisPaper.GetGrade())
Main()