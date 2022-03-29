a = []
numbersfile = open("09.06 CityTemps.txt")
x = numbersfile.readline()
while x != "":
	y = x.split()
	a.append(y)
	x = numbersfile.readline()
numbersfile.close()

for i in range(len(a)):
    total = 0
    for j in range(1,len(a[i])):
        total += float(a[i][j])
    ave = total / 7.0
    a[i].append(str(int(ave)))

print(a)