class Account:
    def __init__(self, AccountTitle, AccountNumber):
        self.AccountTitle = AccountTitle #STRING
        self.AccountNumber = AccountNumber #STRING
        self.Balance = 0 #INTEGER
    def getAccountTitle(self):
        return self.AccountTitle
    def getAccountNumber(self):
        return self.AccountNumber
    def getBalance(self):
        return self.Balance
    def setAccountTitle(self, AccountTitle):
        self.AccountTitle = AccountTitle
    def setAccountNumber(self, AccountNumber):
        self.AccountNumber = AccountNumber
    def setBalance(self, Balance):
        self.Balance += Balance
    def Details(self):
        return "Account Title: {}\nAccount Number: {}\nBalance: {}".format(self.AccountTitle, self.AccountNumber, self.Balance)

class CurrentAccount(Account):
    def __init__(self, AccountTitle, AccountNumber, Level):
        super().__init__(AccountTitle, AccountNumber)
        self.setLevel(Level)
    def getLevel(self):
        return self.Level
    def getFee(self):
        return self.Fee
    def setFee(self):
        if self.Level == "Bronze":
            self.Fee = 20 #INTEGER
        if self.Level == "Silver":
            self.Fee = 50 #INTEGER
        if self.Level == "Gold":
            self.Fee = 100 #INTEGER
    def setLevel(self, Level):
        if Level == 1:
            self.Level = "Bronze" #STRING
        elif Level == 2:
            self.Level = "Silver" #STRING
        elif Level == 3:
            self.Level = "Gold" #STRING
        else:
            return "Incorrect Account Level."
        self.setFee()
    def Details(self):
        return "{}\nLevel: {}\nMonthly Fee: {}".format(super().Details(), self.Level, self.Fee)

class SavingsAccount(Account):
    def __init__(self, AccountTitle, AccountNumber, Deposit, Interval):
        super().__init__(AccountTitle, AccountNumber)
        self.Deposit = Deposit #INTEGER
        self.Interval = Interval #INTEGER
    def getDeposit(self):
        return self.Deposit
    def getInterval(self):
        return self.Interval
    def setDeposit(self, Deposit):
        self.Deposit = Deposit
    def setInterval(self, Interval):
        self.Interval = Interval
    def Details(self):
        return "{}\nDeposit: {}\nInterval: {}".format(super().Details(), self.Deposit, self.Interval)

Account1 = CurrentAccount("John Doe", "1234567890", 1) #CurrentAccount
Account2 = SavingsAccount("Jane Doe", "0987654321", 100, 2) #SavingsAccount
print(Account1.Details())
print(Account2.Details())