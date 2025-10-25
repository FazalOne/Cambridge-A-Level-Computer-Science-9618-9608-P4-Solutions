class Member() :
    def __init__(self):
        self.MemberName = "" #STRING
        self.MemberID = "" #STRING
        self.SubscriptionPaid = False #BOOLEAN
    def SetMemberName(self, Name):
        self.MemberName = Name
    def SetMemberID(self, ID):
        self.MemberID = ID
    def SetSubscriptionPaid(self, Paid):
        self.SubscriptionPaid = Paid
class JuniorMember (Member):
    def __init__(self):
        super().__init__()
    def SetDateOfBirth(self, Date):
        self.DateOfBirth = Date #STRING
NewMember = JuniorMember() # JuniorMemeber
NewMember.SetMemberName("Ahmed")
NewMember.SetMemberID("12347")
NewMember.SetSubscriptionPaid(True)
NewMember.SetDateOfBirth("12/11/2001")