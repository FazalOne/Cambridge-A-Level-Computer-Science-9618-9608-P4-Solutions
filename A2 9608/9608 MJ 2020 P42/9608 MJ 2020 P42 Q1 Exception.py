try:
    file = open('MyData.txt')
except FileNotFoundError:
    print("No file found")