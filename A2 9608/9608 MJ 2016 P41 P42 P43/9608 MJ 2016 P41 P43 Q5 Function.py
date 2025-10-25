def CalculateGrade(Mark):
    if Mark < 40:
        Grade = "FAIL"
    elif Mark < 55:
        Grade = "PASS"
    elif Mark < 70:
        Grade = "MERIT"
    else:
        Grade = "DISTINCTION"
    return Grade
mark = int(input("Enter the exam mark: ")) #INTEGER
grade = CalculateGrade(mark) #STRING
print("Grade awarded:", grade)