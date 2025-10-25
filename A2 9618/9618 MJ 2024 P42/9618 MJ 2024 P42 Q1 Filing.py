def ReadWords(filename):
    global WordArray, NumberWords
    try:
        with open(filename, "r") as File:
            data = File.readline().strip("\n") #STRING
            while data != "":
                WordArray.append(data)
                data = File.readline().strip("\n")
        NumberWords = len(WordArray) - 1
        Play()
    except FileNotFoundError:
        print("File not found. Check the filepath.")

def Play():
    global WordArray, NumberWords
    print("The main word is: ", WordArray[0])
    print("There are ", NumberWords, "words that can be made with 3 or more letters.")
    Answer = "" #STRING
    FoundWords = 0 #INTEGER
    while Answer != "no":
        Answer = input("Enter a word (or 'no' to quit): ").lower()
        if Answer != "no":
            Found = False #BOOLEAN
            i = 1 #INTEGER
            while not Found and i < NumberWords + 1:
                if Answer == WordArray[i]:
                    Found = True
                    FoundWords += 1
                    WordArray[i] = ""
                i += 1
            if Found:
                print("You found a word")
            else:
                print("Not a correct word")
    print("You found ", round((FoundWords/NumberWords * 100),2), "% " + " words.")
    print("List of words not found: ")
    for word in WordArray:
        if word != "":
            print(word)

difficulty = input("Enter difficulty (easy, medium, hard): ").lower() #STRING
while difficulty not in ["easy", "medium", "hard"]:
    difficulty = input("Invalid choice. Enter difficulty (easy, medium, hard): ").lower()
match difficulty:
    case "easy": filename = "easy.txt"
    case "medium": filename = "medium.txt"
    case "hard": filename = "hard.txt"
WordArray = [] #ARRAY OF STRINGS
NumberWords = 0 #INTEGER
ReadWords(filename)