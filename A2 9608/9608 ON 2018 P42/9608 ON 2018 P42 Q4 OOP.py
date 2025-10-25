class Performer:
    def __init__(self,FName,LName,SName,SRole,PType):
        self.FirstName = FName #STRING
        self.LastName = LName #STRING
        self.PerformerType = PType #STRING
        self.SecondaryRole = SRole #STRING
        self.StageName = SName #STRING

    def EditSecondaryRole(self, NewRole):
        self.SecondaryRole = NewRole
    def EditStageName(self, NewStageName):
        self.StageName = NewStageName
    def getStageName(self):
        return self.StageName
    def getFirstName(self):
        return self.FirstName
    def getLastName(self):
        return self.LastName
    def getPerformerType(self):
        return self.PerformerType
    def getSecondaryRole(self):
        return self.SecondaryRole
    def Print(self,perfstring):
        print("{} (real name {} {}) is ".format(self.getStageName(),self.getFirstName(),self.getLastName()) + perfstring +"When not performing, {} is a {}.".format(self.getStageName(),self.getSecondaryRole()))

class Acrobat(Performer):
    def __init__(self,FName,LName,SName,SRole,PType,UseFire):
        super().__init__(FName,LName,SName,SRole,PType)
        self.UseFire=UseFire #BOOLEAN

    def Print(self):
        if self.UseFire:
            super().Print("an {}. Fire is part of {}'s act. ".format(self.getPerformerType(),self.getStageName()))
        else:
            super().Print("an {}. Fire is not part of {}'s act. ".format(self.getStageName()))

class Clown(Performer):
    def __init__(self,FName,LName,SName,SRole,PType,Item,Instrument):
        super().__init__(FName,LName,SName,SRole,PType)
        self.ItemType=Item #STRING
        self.MusicalInstrument=Instrument #STRING
    def getItemType(self):
        return self.ItemType
    def getMusicalInstrument(self):
        return self.MusicalInstrument
    def Print(self):
        super().Print("a {}. {} and {} are part of".format(self.getPerformerType(),self.getItemType(),self.getMusicalInstrument()))

class Aerial(Performer):
    def __init__(self,FName,LName,SName,SRole,PType,AType):
        super().__init__(FName,LName,SName,SRole,PType)
        self.AerialType=AType #STRING

    def Print(self):
        if self.AerialType == "Catcher":
            super().Print("an Aerial Catcher. ")
        else:
            super().Print("an Aerial Flyer. ")

Performer1 = Acrobat("Shantanu","Narayen","Adobe","Acrobat Manager","Acrobat","False") #Acrobat
Performer1.Print()
Performer2 = Acrobat("James","Bond","007","Pyrotechnics Handler","Acrobat","True") #Acrobat
Performer2.Print()
Performer3 = Aerial("Clark","Kent","Superman","Safety Officer","Aerial","Flyer") #Aerial
Performer3.Print()