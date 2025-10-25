class Employee:
    def __init__(self, EmpNum, HPay, Job):
        self.HourlyPay = HPay #REAL
        self.EmployeeNumber = EmpNum #STRING 
        self.JobTitle = Job #STRING
        self.PayYear2022 = [0.0 for x in range(52)] #ARRAY OF REAL
    def GetEmployeeNumber(self):
        return self.EmployeeNumber
    def SetPay(self, WeekNum, Hours):
        self.PayYear2022[WeekNum - 1] = Hours*self.HourlyPay
    def GetTotalPay(self):
        TotalPay = 0.0 #REAL
        for x in self.PayYear2022:
            TotalPay += x
        return round(TotalPay,2)
    
class Manager(Employee):
    def __init__(self, EmpNum, HPay, Job, Bonus):
        super().__init__(EmpNum, HPay, Job)
        self.BonusValue = Bonus #REAL

    def SetPay(self, WeekNum, Hours):
        Hours *= 1 + (self.BonusValue/100) #REAL
        super().SetPay(WeekNum, Hours)

def EnterHours():
    try:
        with open("HoursWeek1.txt", "r") as File:
            for x in range(8):
                EmpNum = File.readline().strip("\n") #STRING
                Hours = float(File.readline().strip("\n")) #REAL
                for y in range(8):
                    if EmployeeArray[y].GetEmployeeNumber() == EmpNum:
                        EmployeeArray[y].SetPay(1, Hours)
    except FileNotFoundError:
        print("File not found, please check the file path.")

EmployeeArray = []
try:
    with open("Employees.txt", "r") as File:
        for x in range(8):
            HPay = float(File.readline().strip("\n")) #REAL
            EmpNum = File.readline().strip("\n") #STRING
            Data = File.readline().strip("\n") #STRING
            try:
                Bonus = float(Data) #REAL
                JobTitle = File.readline().strip("\n") #STRING
                EmployeeArray.append(Manager(EmpNum, HPay, JobTitle, Bonus))
            except ValueError:
                JobTitle = Data
                EmployeeArray.append(Employee(EmpNum, HPay, JobTitle))
except FileNotFoundError:
    print("File not found, please check the file path.")

EnterHours()
for x in EmployeeArray:
    print("Employee Number: ", x.GetEmployeeNumber(), "Total Pay: ", x.GetTotalPay())