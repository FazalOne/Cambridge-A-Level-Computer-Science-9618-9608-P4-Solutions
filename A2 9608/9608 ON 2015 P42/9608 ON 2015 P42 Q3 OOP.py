class Student:
    def __init__(self, name, DOB):
        self.StudentName = name #STRING
        self.DOB = DOB #STRING
    
    def ShowStudentName(self):
        return self.StudentName
    def ShowDOB(self):
        return self.DOB
    def ShowDetails(self):
        return "Student Name: {}, DOB: {}".format(self.StudentName, self.DOB)
    
class FullTimeStudent(Student):
    def __init__(self, name, DOB, address, tel):
        super().__init__(name, DOB)
        self.Address = address #STRING
        self.Telephone = tel #STRING

    def ShowAddress(self):
        return self.Address
    def ShowTelephone(self):
        return self.Telephone
    def SetAddress(self, newAddress):
        self.Address = newAddress
    def SetTelephone(self, newTel):
        self.Telephone = newTel
    def ShowDetails(self):
        return "{}\nAddress: {}, Telephone: {}".format(super().ShowDetails(), self.Address, self.Telephone)

class PartTimeStudent(Student):
    def __init__(self, name, DOB):
        super().__init__(name, DOB)
        self.NoOfCourses = 0 #INTEGER
        self.TotalFee = 0 #INTEGER
        self.FeePaid = False #BOOLEAN

    def ShowCourses(self):
        return self.NoOfCourses
    def ShowTotalFee(self):
        return self.TotalFee
    def ShowFeePaid(self):
        return self.FeePaid
    def SetCourses(self, newCourses):
        self.NoOfCourses = newCourses
    def SetTotalFee(self, newFee):
        self.TotalFee = newFee
    def SetFeePaid(self):
        self.FeePaid = not self.FeePaid
    def ShowDetails(self):
        return "{}\nCourses: {}, Total Fee: {}, Fee Paid? {}".format(super().ShowDetails(), self.NoOfCourses, self.TotalFee, self.FeePaid)

NewStudent1 = FullTimeStudent("A. Nyone", "12/11/1990","123 Street", "099111") #FullTimeStudent
print(NewStudent1.ShowDetails())
NewStudent2 = PartTimeStudent("B. Two", "01/01/1995") #PartTimeStudent
print(NewStudent2.ShowDetails())