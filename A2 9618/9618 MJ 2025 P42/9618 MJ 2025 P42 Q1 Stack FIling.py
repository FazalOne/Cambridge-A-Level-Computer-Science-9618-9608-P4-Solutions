def Push(data):
	global Stack, TopOfStack
	if TopOfStack == 19:
		return -1
	TopOfStack += 1
	Stack[TopOfStack] = data
	return 1

def Pop():
	global Stack, TopOfStack
	if TopOfStack == -1:
		return "-1"
	ReturnValue = Stack[TopOfStack] #STRING
	TopOfStack -= 1
	return ReturnValue

def ReadData(filename):
	global Stack, TopOfStack
	try:
		with open(filename, 'r') as file:
			for line in file:
				if Push(line.strip()) == -1:
					print("Stack full")
	except FileNotFoundError:
		print("Cannot open file")

def calculate():
	global Stack, TopOfStack
	total = int(Pop()) #INTEGER
	returnVal = 0 #INTEGER
	prevOperator = "" #STRING
	isOperator = True #BOOLEAN
	while (returnVal != "-1"):
		returnVal = Pop()
		if not isOperator:
			data = int(returnVal) #INTEGER
			match prevOperator:
				case "+": total += data
				case "-": total -= data
				case "*": total *= data
				case "/": total /= data
				case "^": total **= data
			isOperator = True
		else:
			prevOperator = returnVal
			isOperator = False
	return total

Stack = ["-1" for x in range(20)] #ARRAY OF STRINGS
TopOfStack = -1 #INTEGER

filename = input("Enter the filename: ")
ReadData(filename)
result = calculate() #INTEGER
if result is not None:
	print(result)