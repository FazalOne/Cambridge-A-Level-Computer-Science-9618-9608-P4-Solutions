FileData = [["" for x in range(2)] for i in range(11)] #2D ARRAY OF STRINGS
def ReadHighScores():
    with open("HighScore.txt", 'r') as File:
        for x in range(0, 10):
            FileData[x][0] = File.readline()[:3]
            FileData[x][1] = File.readline()
def OutputHighScores():
    for x in range(0, 11):
        print(str(FileData[x][0]) + " " + str(FileData[x][1]))
def Arrange(Username, Score):
    for x in range(0, 10):
        if Score > int(FileData[x][1]):
            Temp = FileData[x] #STRING
            FileData[x] = [Username,Score]
            Count = x+ 1 #INTEGER
            while Count < 10:
                Second = FileData[Count] #STRING
                FileData[Count] = Temp 
                Temp = Second
                Count += 1
            break
def WriteTopTen():
    with open("NewHighScore.txt", 'w') as Filename:
        for x in range(0, 10):
            Filename.write(str(FileData[x][0]) + '\n')
            Filename.write(str(FileData[x][1]) + '\n')

ReadHighScores()
print("Before")
OutputHighScores()
Username = "" #STRING
while len(Username) != 3:
    Username = input("Enter your Username: ")
Score = -1 #INTEGER
while Score < 1 or Score > 100000:
    Score = int(input("Enter score: "))
Arrange(Username, Score)
print("After")
OutputHighScores()