import random
ArrayData= [0 for i in range(100)] #ARRAY OF INTEGERS
for x in range(0, 100):
    ArrayData[x] = random.randint(1, 100)
print(ArrayData)


def bubbleSort(array):
  for i in range(len(array)):
    swapped = False #BOOLEAN
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j] #INTEGER
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    if not swapped:
      break
bubbleSort(ArrayData)
print('Sorted Array in Ascending Order:')
print(ArrayData)