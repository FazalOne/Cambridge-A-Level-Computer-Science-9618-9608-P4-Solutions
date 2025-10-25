class Member: 
    def __init__(self, Fname, Lname, DOB, GenderVal): 
        self.FirstName = Fname #STRING
        self.LastName = Lname #STRING
        self.DateOfBirth = DOB #STRING
        self.Gender = GenderVal #STRING
    def Introduction(self): 
        return "Hello, I am ", self.FirstName, " ",  self.LastName 
    def DisplayFullnameAndDateofbirth(self): 
        print (self.FirstName, self.LastName, self.DateOfBirth)

class Competitor(Member): 
    def __init__(self, Fname, Lname, DOB, GenderVal, MySport): 
        Member.__init__(self, Fname, Lname, DOB, GenderVal) 
        self.Sport = MySport #STRING
    def Introduction(self): 
        print ("Hello, I am {} {} and my sport is {}".format(self.FirstName,self.LastName, self.Sport))

class Official(Member):
    def __init__(self, Fname, Lname, DOB, GenderVal, JobTitle, FirstAidTrained): 
        Member.__init__(self,Fname, Lname, DOB, GenderVal)
        self.JobTitle = JobTitle #STRING
        self.FirstAidTrained = FirstAidTrained #BOOLEAN
    def Introduction(self): 
        print ("Hello, I am {} {} and my Job is {}".format(self.FirstName,self.LastName, self.JobTitle))

BMXJudge = Official("Omar", "Ellaboudy", "17/03/1993", "Male", "Judge", True) #Official
BMXJudge.Introduction()