class LinkedList:
    def __init__(self,NameStr,Ptr):
        self.Surname = NameStr #STRING
        self.Pointer = Ptr #INTEGER
SurnameList = [LinkedList("",-1) for x in range(6)] #ARRAY OF LinkedList
SurnameList[0]=LinkedList("Hashmi",1)
SurnameList[1]=LinkedList("James",2)
SurnameList[2]=LinkedList("Iqbal",3)
SurnameList[3]=LinkedList("Haq",4)
SurnameList[4]=LinkedList("Khan",5)
SurnameList[5]=LinkedList("Syed",-1)
startPointer = 6 #INTEGER
Current = 0 #INTEGER
if startPointer == 0:
    print("Empty List")
else:
    IsFound = False #BOOLEAN
    ThisSurname = input("Enter surname to search: ") #STRING
    while IsFound == False and Current != -1:
        if SurnameList[Current].Surname == ThisSurname:
            IsFound = True
            print("Surname found at position ", Current+1)
        else:
            Current = SurnameList[Current].Pointer
    if IsFound == False:
        print("Not Found")