def ReadData():
    try:
        global HighScores
        with open("HighScoreTable.txt", "r") as File:
            for x in range(7):
                for y in range(3):
                    HighScores[x][y] = File.readline().strip("\n")
        return HighScores
    except FileNotFoundError:
        print("File not found... Please check the filepath.")

def OutputHighScores(Scores):
    for x in range(len(Scores)):
        print(Scores[x][0] + " reached level " + Scores[x][1] + " with a score of " + Scores[x][2])

def SortScores(Scores):
    ArrayLength = len(Scores) #INTEGER
    for x in range(ArrayLength - 1):
        for y in range(ArrayLength - x - 1):
            if int(Scores[y][1]) < int(Scores[y+1][1]):
               Scores[y], Scores[y+1] = Scores[y+1], Scores[y]
            elif int(Scores[y][1]) == int(Scores[y+1][1]):
                if int(Scores[y][2]) < int(Scores[y+1][2]):
                    Scores[y], Scores[y+1] = Scores[y+1], Scores[y]
    return Scores

HighScores = [["" for x in range(3)] for y in range(7)] #2D ARRAY OF STRINGS
HighScores = ReadData()
print("Before: ")
OutputHighScores(HighScores)
HighScores = SortScores(HighScores)
print("After: ")
OutputHighScores(HighScores)