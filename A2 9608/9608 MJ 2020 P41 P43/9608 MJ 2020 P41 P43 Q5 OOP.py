class Lesson:
    def __init__(self, LessonType, Instructor):
        self.LessonType = LessonType #STRING
        self.Instructor = Instructor #STRING
    def GetLessonType(self):
        return self.LessonType
    def GetInstructor(self):
        return self.Instructor
    def GetFee(self, SkillLevel):
        if SkillLevel == "B":
            return 45
        elif SkillLevel == "I":
            return 50
        elif SkillLevel == "A":
            return 55
        else:
            return -1
    def SetLessonType(self, newLessonType):
        self.LessonType = newLessonType
    def SetInstructor(self, newInstructor):
        self.Instructor = newInstructor

LessonArray = [Lesson("","") for x in range(9)] #ARRAY OF Lesson
LessonArray[2] = Lesson("Improve Your Serve","David")
print("The lesson is: ", LessonArray[2].GetLessonType(), "and the instructor is: ", LessonArray[2].GetInstructor())