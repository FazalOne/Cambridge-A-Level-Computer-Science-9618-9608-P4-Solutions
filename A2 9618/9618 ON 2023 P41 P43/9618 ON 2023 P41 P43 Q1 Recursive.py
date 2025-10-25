def IterativeVowels(Value):
    Total = 0 #INTEGER
    for x in range(0,len(Value)):
        if Value[x] in ['a','e','i','o','u']:
            Total += 1
    return Total

def RecursiveVowels(Value): #method 1 using slicing
    if len(Value) == 0:
        return 0
    if Value[0] in ['a','e','i','o','u']:
        return 1 + RecursiveVowels(Value[1:len(Value)])
    return 0 + RecursiveVowels(Value[1:len(Value)]) 

def newRecursiveVowels(Value, x, total): #method 2 using index
    if x == len(Value):
        return total
    if Value[x] in ['a','e','i','o','u']:
        return newRecursiveVowels(Value, x + 1, total + 1)
    return newRecursiveVowels(Value, x + 1, total)

print(IterativeVowels('house'))
print(RecursiveVowels('imagine'))
print(newRecursiveVowels("imagine", 0, 0))