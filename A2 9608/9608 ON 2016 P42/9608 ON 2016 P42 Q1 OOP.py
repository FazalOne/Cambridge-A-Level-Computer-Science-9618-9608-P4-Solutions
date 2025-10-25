class TicketMachine:
    def __init__(self):
        self.amount = 0 #INTEGER
        self.state = "Idle" #STRING
    
    def SetState(self, NewState):
        self.State = NewState
        print(self.State)
    def ReturnCoins(self):
        print(self.Amount)
        self.Amount = 0
    def validCoin(self, s):
        return s in ['10','20','50','100']
    def coinInserted(self, s):
        self.amount += int(s)
    def stateChange(self):
        newInput = input("Insert coin: ") #STRING
        if newInput == "C":
            if self.state == "Counting":
                self.SetState("Cancelled")
                self.ReturnCoins()
                self.SetState("Idle")
        elif newInput == "A":
            if self.amount == 0:
                print("no coins inserted")
            else:
                self.SetState("Accepted")
                self.PrintTicket()
                self.SetState("Idle")
        elif self.validCoin(newInput):
            self.coinInserted(newInput)
            self.SetState("Counting")
        else:
            print("Error - not a valid coin")
    def PrintTicket(self):
        print("Printing ticket for amount: " + str(self.amount))
        self.amount = 0

ParkingMeter = TicketMachine() #TicketMachine
while True:
    ParkingMeter.stateChange()    