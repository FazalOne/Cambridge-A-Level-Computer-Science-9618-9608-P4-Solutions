import pickle
class Member:
    def __init__(self,Name,ID):
        self.MemberName = Name #STRING
        self.MemberID = ID #INTEGER

def Hash(MemberID):
    Address = MemberID % 100 #INTEGER
    return Address

def Pickle(MemberRecord):
    NewAddress = Hash(MemberRecord.MemberID) #INTEGER
    try:
        MemberFile = open('MembershipFile.DAT','wb')
        MemberFile.seek(NewAddress)
        pickle.dump (MemberRecord, MemberFile) 
        MemberFile.close()
    except IOError:
        print("Could not find File")

Member1=Member("James", 789) #Member
Pickle(Member1)