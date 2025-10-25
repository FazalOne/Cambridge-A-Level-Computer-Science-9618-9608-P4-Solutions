class QuestionClass:
    def __init__(self, QuestionP, AnswerP, DifficultyP): 
        self.Question = QuestionP #STRING
        self.Answer = AnswerP #STRING
        self.Difficulty = DifficultyP #INTEGER

    def GetQuestion(self):
        return self.Question
    def GetAnswer(self):
        return self.Answer
    def GetDifficulty(self):
        return self.Difficulty

class QuizClass:
    def __init__(self):
        self.NumberOfQuestions = 0 #INTEGER
        self.CurrentQuestion = 0 #INTEGER
        self.Questions = [QuestionClass("","",0) for x in range(20)] #ARRAY OF QuestionClass

    def AddQuestion(self, question):
        if self.NumberOfQuestions < 20:
            self.Questions[self.NumberOfQuestions] = question
            self.NumberOfQuestions += 1
            return True
        else:
            print("Maximum number of questions reached")
            return False
    
    def GetQuestion(self):
        return self.Questions[self.CurrentQuestion].GetQuestion()
    
    def CheckAnswer(self, answer):
        if self.Questions[self.CurrentQuestion].GetAnswer() == answer:
            self.CurrentQuestion += 1
            return True
        return False
    
FirstQuiz = QuizClass() #QuizClass
Question1 = QuestionClass("What is 100 / 5?", "20", 1) #QuestionClass
FirstQuiz.AddQuestion(Question1)
Question2 = QuestionClass("What is 100 * 5?", "500", 1) #QuestionClass
FirstQuiz.AddQuestion(Question2)
for x in range(FirstQuiz.NumberOfQuestions):
    print("Q" + str(x+1) + ": " +FirstQuiz.Questions[x].GetQuestion())
    while not FirstQuiz.CheckAnswer(input("Your answer: ")):
        print("Incorrect. Please try again.")
    print("Correct!")