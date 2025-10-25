def PushData(letter):
    global VowelTop, ConsonantTop
    if letter in "aeiou":
        if VowelTop < 100:
            StackVowel[VowelTop] = letter
            VowelTop += 1
        else:
            print("Stack is full")
    else:
        if ConsonantTop < 100:
            StackConsonant[ConsonantTop] = letter
            ConsonantTop += 1
        else:
            print("Stack is full")

def PopVowel():
    global VowelTop
    if VowelTop == 0:
        return "No data"
    VowelTop -= 1
    return StackVowel[VowelTop]

def PopConsonant():
    global ConsonantTop
    if ConsonantTop == 0:
        return "No data"
    ConsonantTop -= 1
    return StackConsonant[ConsonantTop]

def ReadData():
    try:
        with open ("StackData.txt","r") as File:
            for Line in File:
                PushData(Line.strip("\n"))
    except FileNotFoundError:
        print("File does not exist, please check filepath or check filename")

StackVowel = ["" for x in range(100)] #ARRAY OF STRING
StackConsonant = ["" for x in range(100)] #ARRAY OF STRING
VowelTop = 0 #INTEGER
ConsonantTop = 0 #INTEGER

ReadData()
outputStr = "" #STRING
for x in range(5):
    choice = input("Enter vowel or consonant: ")
    if choice == "vowel":
        returnVal = PopVowel() #STRING
    elif choice == "consonant":
        returnVal = PopConsonant() #STRING
    if returnVal == "No Data":
        print("Stack is empty!")
    else:
        outputStr += returnVal
print(outputStr)