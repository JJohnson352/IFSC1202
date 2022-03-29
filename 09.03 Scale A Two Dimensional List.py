a = [] 
numbersfile = open("09.03 NumbersList.txt")
x = numbersfile.readline()
while x != "":
	y = x.split(" ")
	for i in range(len(y)):
		y[i] = int(y[i])
	a.append(y)
	x = numbersfile.readline()
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] * 2, end=' ')
    print()