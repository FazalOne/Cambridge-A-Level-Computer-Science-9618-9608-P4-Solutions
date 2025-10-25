class Employee():
    def __init__(self):
        self.EmployeeName = "" #STRING
        self.EmployeeID = "" #STRING
        self.Pay = 0 #INTEGER
    def SetEmployeeName(self, Name):
        self.EmployeeName = Name
    def SetEmployeeID(self, ID):
        self.EmployeeID = ID
    def SetMonthlyPay(self, Amount):
        self.Pay = Amount
    def GetEmployeeName(self):
        return self.EmployeeName
    def GetEmployeeID(self):
        return self.EmployeeID
    def GetMonthlyPay(self):
        return self.Pay
    def Print(self,perfstring):
        print("Employee {} ID {} has monthly pay {}. ".format(self.GetEmployeeName(),self.GetEmployeeID(),self.GetMonthlyPay()) + perfstring )
        return
class HourlyPaidEmployee(Employee):
    def __init__(self): 
        super().__init__()
        self.HourlyPay = 0 
        self.HoursWorked = 0
    def SetHourlyPay(self, Pay):
        self.HourlyPay = Pay
    def SetHoursWorked(self, Hours):
        self.HoursWorked = Hours
    def GetHourlyPay(self):
        return self.HourlyPay
    def GetHoursWorked(self):
        return self.HoursWorked
    def CalculatePay(self):
        super().SetMonthlyPay(self.GetHourlyPay()*self.GetHoursWorked())
    def Print(self):
        self.CalculatePay()
        super().Print("Their Hourly Pay is {}. and their Hours Worked are {}.".format(self.GetHourlyPay(),self.GetHoursWorked()))
        return
class SalariedEmployee(Employee):
    def __init__(self): 
        super().__init__()
        self.AnnualSalary = 0 #INTEGER
    def SetAnnualSalary(self, Salary):
        self.AnnualSalary = Salary
    def GetAnnualSalary(self):
        return self.AnnualSalary
    def CalculatePay(self):
        super().SetMonthlyPay(int(self.GetAnnualSalary()/12))
    def Print(self):
        self.CalculatePay()
        super().Print("Their Annual Salary is {}.".format(self.GetAnnualSalary()))
        return
Employee1 = HourlyPaidEmployee() # HourlyPaidEmployee
Employee1.SetEmployeeName("James")
Employee1.SetEmployeeID("0001")
Employee1.SetHourlyPay(15)
Employee1.SetHoursWorked(180)
Employee1.Print()
Employee2 = SalariedEmployee() # Salaried Employee
Employee2.SetEmployeeName("Amy")
Employee2.SetEmployeeID("0002")
Employee2.SetAnnualSalary(55000)
Employee2.Print()