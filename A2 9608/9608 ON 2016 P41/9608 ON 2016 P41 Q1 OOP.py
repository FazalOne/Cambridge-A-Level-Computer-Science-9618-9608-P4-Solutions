class SafetyDepositBox:
    def __init__(self):
        self.code = "" #STRING
        self.state = "Open-NoCode" #STRING

    def Reset(self):
        self.code = ""
    def SetState(self,NewState):
        self.state = NewState
        print(self.state)
    def SetNewCode(self, NewCode):
        self.code = NewCode
        print("New code set: ", self.code)
    def valid(self, s):
        return len(s) == 4 and (s[0] in '0123456789') and (s[1] in '0123456789') and (s[2] in '0123456789') and (s[3] in '0123456789')
    def StateChange(self):
        Chars = input("Enter code: ") #STRING
        if Chars == "R":
            if self.state == "Open-CodeSet":
                self.Reset()
                self.SetState("Open-NoCode")
        elif Chars == self.code:
            if self.state == "Locked":
                self.SetState("Open-CodeSet")
            elif self.state == "Closed":
                self.SetState("Locked")
        elif (Chars == "") & (self.state == "Open-CodeSet"):
            self.SetState("Closed")
        elif self.valid(Chars):
            if self.state == "Open-NoCode":
                self.SetNewCode(Chars)
                self.SetState("Open-CodeSet")
            else:
                print("Error - does not match set code")
        else:
            print("Error - Code format incorrect")

ThisSafe = SafetyDepositBox() #SafetyDepositBox
while True:
    ThisSafe.StateChange()