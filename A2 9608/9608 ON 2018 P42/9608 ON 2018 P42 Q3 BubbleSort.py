List = [1,30,4,7,5,21,19,11] #ARRAY OF INTEGERS
print(List)
for Outer in range(len(List)-1,0,-1):
    for Inner in range(0, Outer):
        if List[Inner] > List[Inner + 1]:
            Temp = List[Inner] #INTEGER
            List[Inner] = List[Inner + 1]
            List[Inner + 1] = Temp
print(List)
print()

List = [1,30,4,7,5,21,19,11] #ARRAY OF INTEGERS
print(List)
Outer = len(List)-1 #INTEGER
Swap = True #BOOLEAN
while Swap and Outer > 0:
    Inner = 0 #INTEGER
    Swap = False
    while Inner < Outer:
        if List[Inner] > List[Inner + 1]:
            Temp = List[Inner]
            List[Inner] = List[Inner + 1]
            List[Inner + 1] = Temp
            Swap = True
        Inner += 1
    Outer -= 1
print(List)