s = input("Enter Values Separated By Spaces: ")
a = "1 3 5 7 9"
b = a.split()
for i in range(len(b)):
    b[i] = int(b[i])
for i in range(len(b)):
    print(b[i]) 