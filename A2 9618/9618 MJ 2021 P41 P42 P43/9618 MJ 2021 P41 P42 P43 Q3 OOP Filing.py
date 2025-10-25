class treasureChest:
    def __init__(self, questionP, answerP, pointsP):
        self.question = questionP #STRING
        self.answer = answerP #INTEGER
        self.points = pointsP #INTEGER

    def getQuestion(self):
        return self.question
    def checkAnswer(self, answerP):
        if int(self.answer) == answerP:
            return True
        else:
            return False
    def getPoints(self, attempts):
        match attempts:
            case 1: return int(self.points)
            case 2: return int(self.points) // 2
            case 3 | 4: return int(self.points) // 4
            case _: return 0

def readData():
    global arrayTreasure
    arrayTreasure = ["" for x in range(5)] #ARRAY OF treasureChest
    try:
        with open ("TreasureChestData.txt","r") as file:
            count = 0 #INTEGER
            dataFetched = file.readline().strip() #STRING
            while(dataFetched != "" ):
                question = dataFetched
                answer = file.readline().strip() #STRING
                points = file.readline().strip() #STRING
                arrayTreasure[count] = treasureChest(question, answer, points)
                dataFetched = file.readline().strip() #STRING
                count += 1
    except IOError:
        print("Could not find file")

readData()
choice = int(input("Pick a treasure chest to open: ")) #INTEGER
if  0 < choice < 6:
    result = False #BOOLEAN
    attempts = 0 #INTEGER
    while not result:
        answer = int(input(arrayTreasure[choice-1].getQuestion()))
        result = arrayTreasure[choice-1].checkAnswer(answer)
        attempts += 1
        print(int(arrayTreasure[choice-1].getPoints(attempts)))