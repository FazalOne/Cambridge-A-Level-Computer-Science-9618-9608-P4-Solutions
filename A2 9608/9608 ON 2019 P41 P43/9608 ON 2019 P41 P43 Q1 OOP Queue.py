class CircularQueue:
    def __init__(self, Size):
        self.Size = Size #INTEGER
        self.Queue = ["" for x in range(Size)] #ARRAY OF STRINGS
        self.StartPointer = 0 #INTEGER
        self.EndPointer = 0 #INTEGER

    def isEmpty(self):
        return self.StartPointer == self.EndPointer
    def isFull(self):
        return (self.EndPointer + 1) % self.Size == self.StartPointer

    def enqueue(self, printJob):
        if self.isFull():
            return "Queue is full"
        else:
            self.Queue[self.EndPointer] = printJob
            self.EndPointer = (self.EndPointer + 1) % self.Size

    def remove(self):
        if self.isEmpty():
            return "Empty"
        else:
            printJob = self.Queue[self.StartPointer]
            self.Queue[self.StartPointer] = None
            self.StartPointer = (self.StartPointer + 1) % self.Size
            return printJob

Queue = CircularQueue(6) #CircularQueue
Queue.enqueue("Job1")
Queue.enqueue("Job2")
Queue.enqueue("Job3")

print(Queue.remove())  
print(Queue.remove())  

Queue.enqueue("Job4")
Queue.enqueue("Job5")

print(Queue.remove())  
print(Queue.remove())  
print(Queue.remove())  
print(Queue.remove())  

class PrintAccount:
    def __init__(self, FNParam, LNParam, PIDParam):
        self.PrintID = PIDParam #STRING
        self.FirstName = FNParam #STRING
        self.LastName = LNParam #STRING
        self.Credits = 50 #INTEGER
    
    def GetName(self):
        return self.FirstName + " " + self.LastName
    def GetPrintID(self):
        return self.PrintID
    
    def SetFirstName(self, FNParam):
        self.FirstName = FNParam
    def SetLastName(self, LNParam):
        self.LastName = LNParam
    def SetPrintID(self, PIDParam):
        self.PrintID = PIDParam
    def AddCredits(self, MoneyInput):
        CreditPerDollar = 25 #INTEGER
        FreeCredit10 = 25 #INTEGER
        FreeCredit20 = 50 #INTEGER
        Twenty = 20 #INTEGER
        Ten = 10 #INTEGER
        if MoneyInput >= Twenty:
            self.Credits += (MoneyInput * CreditPerDollar) + FreeCredit20
        elif MoneyInput >= Ten:
            self.Credits += (MoneyInput * CreditPerDollar) + FreeCredit10
        else:
            self.Credits += (MoneyInput * CreditPerDollar)
    def RemoveCredits(self, CredParam):
        self.Credits -= CredParam

def CreateID(FNParam, LNParam):
    global numberStudents
    count = 0 #INTEGER
    PrintID = FNParam[:3].lower() + LNParam[:3].lower() + "1" #STRING
    studentAdd = numberStudents #INTEGER

    for x in range(0, numberStudents):
        if StudentAccounts[x].GetPrintID() == PrintID:
            count += 1
            PrintID = PrintID[:6].lower() + str(count)

    StudentAccounts[studentAdd] = PrintAccount(FNParam, LNParam, PrintID)
    numberStudents += 1

numberStudents = 0 #INTEGER
StudentAccounts = [PrintAccount("", "", "") for _ in range(999)] #ARRAY OF PrintAccounts