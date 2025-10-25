class Employee:
    def __init__(self,ID,NewName,NewAddress,NewDateOfBirth):
        self.EmployeeID= ID #INTEGER
        self.Name = NewName #STRING
        self.Address = NewAddress #STRING
        self.DateOfBirth = NewDateOfBirth #STRING
    
    def SetEmployeeID(self, NewID): 
        self.EmployeeID = NewID
    def SetName(self,NewName):
        self.Name = NewName
    def SetAddress(self,Address):
        self.Address = Address
    def SetDateOfBirth(self, NewDOB):
        self.DateOfBirth = NewDOB

    def GetEmployeeID(self): 
        return self.EmployeeID
    def GetName(self):
        return self.Name
    def GetAddress(self):
        return self.Address
    def GetDateOfBirth(self):
        return self.DateOfBirth

class SalaryEmployee(Employee):
    def __init__(self,ID,NewName,NewAddress,NewDateOfBirth,MonthlyPayment,HoursThisMonth,PublicHoliday,Pension):
        super().__init__(ID,NewName,NewAddress,NewDateOfBirth)
        self.MonthlyPayment = MonthlyPayment #INTEGER
        self.HoursThisMonth = HoursThisMonth #INTEGER
        self.PublicHoliday = PublicHoliday #INTEGER
        self.Pension = Pension #BOOLEAN

    def SetMonthlyPayment(self,MonthlyPayment):
        self.MonthlyPayment = MonthlyPayment
    def SetHoursThisMonth(self,HoursThisMonth):
        self.HoursThisMonth = HoursThisMonth
    def SetPublicHoliday(self,PublicHoliday):
        self.PublicHoliday = PublicHoliday
    def SetPension(self, NewPension): 
        if NewPension == True or NewPension == False: 
            self.Pension = NewPension 
            return True
        else: 
            print("Incorrect input")
            return False

    def GetMonthlyPayment(self):
        return self.MonthlyPayment
    def GetHoursThisMonth(self):
        return self.HoursThisMonth
    def GetPublicHoliday(self):
        return self.PublicHoliday
    def GetPension(self):
        return self.Pension
    def CalculateMonthlySalary(self): 
        BonusPayment = 0 
        PensionPayment = 0 
        HoursBonus = 0.05 
        HoursMonthBonus = 160 
        PensionCost = 0.04 
        PublicHolidayBonus = 0.03 
        BasicSalary = self.GetMonthlyPayment() 
        if self.GetHoursThisMonth() >= HoursMonthBonus: 
            BonusPayment = BasicSalary * HoursBonus
        if self.GetPension() == True: 
            PensionPayment = BasicSalary * PensionCost 
        if self.GetPublicHoliday() != 0: 
            BonusPayment = BonusPayment + (BasicSalary * PublicHolidayBonus * self.GetPublicHoliday())
        print("The pension payment is ", str(PensionPayment)) 
        print("The bonus payment is ", str(BonusPayment)) 
        MonthlySalary = BasicSalary + BonusPayment - PensionPayment 
        return MonthlySalary  

class ApprenticeshipEmployee(Employee):
    def __init__(self,ID,NewName,NewAddress,NewDateOfBirth,HourlyRate, HoursThisWeek):
        super().__init__(ID,NewName,NewAddress,NewDateOfBirth)
        self.HourlyRate = HourlyRate #INTEGER
        self.HoursThisWeek = HoursThisWeek #INTEGER

    def SetHoursThisWeek(self, NewHours):
        self.HoursThisWeek = NewHours
    def SetHourlyRate(self,NewHourlyRate):
        self.HourlyRate = NewHourlyRate
        
    def GetHoursThisWeek(self):
        return self.HoursThisWeek
    def GetHourlyRate(self):
        return self.HourlyRate
    
TheEmployee = SalaryEmployee(2500,"Ali","SaudiArabia","12-2-2000",1000,240,3,True) #SalaryEmployee
print("Employees monthly salary is: " + str(TheEmployee.CalculateMonthlySalary()))
TheApprentice = ApprenticeshipEmployee(3500,"Omar","Egypt","5-6-2002",15,40) #ApprenticeshipEmployee
print("The apprentice's hourly rate is: " + str(TheApprentice.GetHourlyRate()))